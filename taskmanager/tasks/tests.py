from django.test import TestCase
from rest_framework.test import APIClient
from .models import Task
from django.utils import timezone
from datetime import timedelta

class TaskTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.deadline = timezone.now() + timedelta(days=2)
        self.task_data = {
            'title': 'Test Task',
            'description': 'Testing...',
            'category': 'Work',
            'priority': 'High',
            'deadline': self.deadline,
        }

    def test_create_task(self):
        response = self.client.post('/api/tasks/', self.task_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['title'], 'Test Task')
