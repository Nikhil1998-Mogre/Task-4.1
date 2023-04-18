from django.shortcuts import render
from rest_framework import viewsets
from .models import Employer,Tag,Job,Skill,JobSkill,QuickJobApplication,Student,JobApplication,JobApplicationComment,JobApplicationStatus
from .serializers import EmployerSerializer,UserSerializer,TagSerializer,JobSerializer,SkillSerializer,JobSkillSerializer,QuickJobApplicationSerializer,StudentSerializer,JobApplicationSerializer,JobApplicationCommentSerializer,JobApplicationStatusSerializer
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
    serializer_class = TagSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class JobSkillViewSet(viewsets.ModelViewSet):
    queryset = JobSkill.objects.all()
    serializer_class = JobSkillSerializer


class QuickJobApplicationViewSet(viewsets.ModelViewSet):
    queryset = QuickJobApplication.objects.all()
    serializer_class = QuickJobApplicationSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer


class JobApplicationCommentViewSet(viewsets.ModelViewSet):
    queryset = JobApplicationComment.objects.all()
    serializer_class = JobApplicationCommentSerializer


class JobApplicationStatusViewSet(viewsets.ModelViewSet):
    queryset = JobApplicationStatus.objects.all()
    serializer_class = JobApplicationStatusSerializer
