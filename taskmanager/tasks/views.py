from rest_framework import viewsets, filters
from .models import Task
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import NotFound

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['category', 'priority']
    ordering_fields = ['created_at', 'priority', 'deadline']
    
    def get_object(self):
        try:
            return super().get_object()
        except Exception:
            raise NotFound("Task does not exist.")