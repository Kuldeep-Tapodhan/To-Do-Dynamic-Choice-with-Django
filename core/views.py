from django.shortcuts import render
# from django.http import HttpResponse (No longer needed)
from .models import Status, Task
from rest_framework import viewsets, permissions
from .serializers import TaskSerializer, StatusSerializer 

# --- New Imports ---
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm


# --- Secure the HTML Page ---
@login_required # This decorator automatically redirects to the login page
def task_board_page(request):
    # Get tasks ONLY for the logged-in user
    user_tasks = Task.objects.filter(user=request.user)
    
    # Get unassigned tasks for THIS user
    unassigned_tasks = user_tasks.filter(status__isnull=True)

    # Get all statuses, but prefetch ONLY the user's tasks for each status
    all_statuses = Status.objects.prefetch_related(
        Prefetch('tasks', queryset=user_tasks)
    ).all()
    
    statuses_json = StatusSerializer(all_statuses, many=True).data

    context = {
        'statuses': all_statuses,
        'unassigned_tasks': unassigned_tasks,
        'statuses_json': statuses_json,
        'user': request.user # Pass the user to the template for the "Logout" button
    }
    return render(request, 'core/task_board.html', context)


# --- Secure the API ---
class TaskViewSet(viewsets.ModelViewSet):
    # --- ADD THIS LINE ---
    # This is required for makemigrations and the router to work
    queryset = Task.objects.all() 
    
    serializer_class = TaskSerializer
    
    # --- Change permissions ---
    permission_classes = [permissions.IsAuthenticated] # Was: [permissions.AllowAny]

    # --- New Function: Filter tasks by user ---
    def get_queryset(self):
        # Only return tasks for the current logged-in user
        return self.request.user.tasks.all()

    # --- New Function: Assign new tasks to the user ---
    def perform_create(self, serializer):
        # When a new task is created, automatically set its user to the current user
        serializer.save(user=self.request.user)

# --- New: Add a Registration View ---
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login') # Redirect to login page on successful signup
    template_name = 'registration/signup.html'