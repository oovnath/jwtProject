from rest_framework import serializers
from todo.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    model = Todo
    exclude =['created_at', 'updated_at']