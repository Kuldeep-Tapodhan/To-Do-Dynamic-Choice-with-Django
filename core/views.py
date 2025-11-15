from django.shortcuts import render
from django.http import HttpResponse
from .models import Status, Task
from rest_framework import viewsets, permissions
from .serializers import TaskSerializer, StatusSerializer 

def task_board_page(request):
    all_statuses = Status.objects.prefetch_related('tasks').all()
    unassigned_tasks = Task.objects.filter(status__isnull=True)
    
    statuses_json = StatusSerializer(all_statuses, many=True).data

    context = {
        'statuses': all_statuses,
        'unassigned_tasks': unassigned_tasks,
        'statuses_json': statuses_json,
    }
    return render(request, 'core/task_board.html', context)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.AllowAny]
