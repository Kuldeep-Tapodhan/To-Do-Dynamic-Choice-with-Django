from rest_framework import serializers
from .models import Status, Task, CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id', 'username', 'email',
            'first_name', 'last_name',
            'phone', 'bio',
            'date_joined',
        ]
        read_only_fields = ['id', 'date_joined']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    password2 = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = CustomUser
        fields = [
            'username', 'email', 'password', 'password2',
            'first_name', 'last_name', 'phone', 'bio',
        ]

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password2': 'Passwords do not match.'})
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'name', 'created_at', 'modified_at']
        read_only_fields = ['id', 'created_at', 'modified_at']


class TaskSerializer(serializers.ModelSerializer):
    status = serializers.PrimaryKeyRelatedField(
        queryset=Status.objects.all(),
        allow_null=True
    )
    # user is read-only — assigned automatically, cannot be changed via API
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Task
        fields = [
            'id', 'user', 'title', 'description',
            'status', 'priority', 'due_date',
            'is_completed', 'created_at', 'modified_at',
        ]
        read_only_fields = ['id', 'user', 'created_at', 'modified_at']