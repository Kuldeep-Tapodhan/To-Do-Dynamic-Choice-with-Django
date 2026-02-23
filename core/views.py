from django.shortcuts import render
from .models import Status, Task, CustomUser
from rest_framework import viewsets, permissions, generics, status as drf_status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TaskSerializer, StatusSerializer, RegisterSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# --- Imports ---
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm


# --- Secure the HTML Page ---
@login_required
def task_board_page(request):
    # Superuser can view any user's tasks by selecting from dropdown
    viewing_user = request.user

    if request.user.is_superuser:
        selected_user_id = request.GET.get('user_id')
        all_users = CustomUser.objects.filter(is_superuser=False).order_by('username')

        if selected_user_id:
            try:
                viewing_user = CustomUser.objects.get(id=selected_user_id)
            except CustomUser.DoesNotExist:
                viewing_user = request.user
    else:
        all_users = None

    # Get tasks for the viewing user
    user_tasks = Task.objects.filter(user=viewing_user).order_by('-created_at')

    # Get unassigned tasks
    unassigned_tasks = user_tasks.filter(status__isnull=True)

    # Get all statuses, prefetch the viewing user's tasks
    all_statuses = Status.objects.prefetch_related(
        Prefetch('tasks', queryset=user_tasks)
    ).all()

    statuses_json = StatusSerializer(all_statuses, many=True).data

    context = {
        'statuses': all_statuses,
        'unassigned_tasks': unassigned_tasks,
        'statuses_json': statuses_json,
        'user': request.user,
        'viewing_user': viewing_user,
        'all_users': all_users,
        'is_viewing_own': viewing_user == request.user,
    }
    return render(request, 'core/task_board.html', context)


# --- API: Task CRUD ---
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        # Superuser can query any user's tasks via ?user_id=
        if user.is_superuser:
            user_id = self.request.query_params.get('user_id')
            if user_id:
                return Task.objects.filter(user_id=user_id).order_by('-created_at')
            return Task.objects.all().order_by('-created_at')

        return user.tasks.all().order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# --- API: User Registration (returns JWT tokens) ---
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Generate JWT tokens for the new user
        refresh = RefreshToken.for_user(user)

        return Response({
            'user': UserSerializer(user).data,
            'tokens': {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        }, status=drf_status.HTTP_201_CREATED)


# --- API: User Profile ---
class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


# --- Template: Registration View ---
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'