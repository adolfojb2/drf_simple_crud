from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializers

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all() #consulta todos los datos de la tabla
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializers
