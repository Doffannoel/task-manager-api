from rest_framework import serializers
from .models import Task
from django.utils import timezone

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'category', 'priority', 'status', 
                 'deadline', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def validate_deadline(self, value):
        if value and value < timezone.now():
            raise serializers.ValidationError("Deadline cannot be in the past.")
        return value

