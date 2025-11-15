from rest_framework import serializers
from .models import Status, Task

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'name']

class TaskSerializer(serializers.ModelSerializer):
    status = serializers.PrimaryKeyRelatedField(
        queryset=Status.objects.all(), 
        allow_null=True
    )

    class Meta:
        model = Task
        fields = ['id', 'title', 'status']
        read_only_fields = ['id']