from django.shortcuts import render
from rest_framework import viewsets,pagination
from .models import Employer,Tag,Job,Skill,JobSkill,QuickJobApplication,Student,JobApplication,JobApplicationComment,JobApplicationStatus
from .serializers import EmployerSerializer,UserSerializer,TagSerializer,JobSerializer,SkillSerializer,JobSkillSerializer,QuickJobApplicationSerializer,StudentSerializer,JobApplicationSerializer,JobApplicationCommentSerializer,JobApplicationStatusSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class LazyPagination(pagination.PageNumberPagination):
    page_size = 4  # Change this as per your requirement
    page_size_query_param = 'page_size'
    max_page_size = 1000  # Change this as per your requirement


# Global Authentication provided in settings 
# All view will be affected 
# GLobal settings can we overrided by Local 



# Create your views here.
class EmployerviewSet(viewsets.ModelViewSet):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer
    pagination_class = LazyPagination
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = LazyPagination
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = LazyPagination
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    pagination_class = LazyPagination
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    pagination_class = LazyPagination
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

class JobSkillViewSet(viewsets.ModelViewSet):
    queryset = JobSkill.objects.all()
    serializer_class = JobSkillSerializer
    pagination_class = LazyPagination
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

class QuickJobApplicationViewSet(viewsets.ModelViewSet):
    queryset = QuickJobApplication.objects.all()
    serializer_class = QuickJobApplicationSerializer
    pagination_class = LazyPagination
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = LazyPagination
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    pagination_class = LazyPagination
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

class JobApplicationCommentViewSet(viewsets.ModelViewSet):
    queryset = JobApplicationComment.objects.all()
    serializer_class = JobApplicationCommentSerializer
    pagination_class = LazyPagination
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

class JobApplicationStatusViewSet(viewsets.ModelViewSet):
    queryset = JobApplicationStatus.objects.all()
    serializer_class = JobApplicationStatusSerializer
    pagination_class = LazyPagination
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]