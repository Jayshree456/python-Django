from rest_framework import viewsets, permissions # type: ignore
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['get'])
    def projects(self, request, pk=None):
        client = self.get_object()
        projects = client.projects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(users=self.request.user)
