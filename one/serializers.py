from rest_framework import serializers
from .models import Client, Project

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_by', 'created_at']
        read_only_fields = ['created_by', 'created_at']
class ProjectSerializer(serializers.ModelSerializer):
    #client_name = serializers.ReadOnlyField(source='client.client_name')

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_at']