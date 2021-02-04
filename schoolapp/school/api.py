from .models import Students, Teachers
from rest_framework import viewsets, permissions
from .serializers import StudentsSerializer, TeachersSerializer


class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StudentsSerializer


class TeachersViewSet(viewsets.ModelViewSet):
    queryset = Teachers.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TeachersSerializer
