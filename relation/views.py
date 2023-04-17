from django.shortcuts import render
from rest_framework import viewsets
from .models import Employer,Tag
from .serializers import EmployerSerializer,UserSerializer
from django.contrib.auth.models import User

# Create your views here.
class EmployerviewSet(viewsets.ModelViewSet):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = UserSerializer