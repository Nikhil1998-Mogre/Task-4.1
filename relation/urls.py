from django.contrib import admin
from django.urls import path,include
from .views import EmployerviewSet,UserViewSet,TagViewSet,JobViewSet,SkillViewSet,JobSkillViewSet,QuickJobApplicationViewSet,StudentViewSet,JobApplicationViewSet,JobApplicationCommentViewSet,JobApplicationStatusViewSet
from rest_framework import routers
from django.contrib.auth.models import User


router = routers.DefaultRouter()
router.register(r'employees',EmployerviewSet)
router.register(r'users',UserViewSet)
router.register(r'tags',TagViewSet)
router.register(r'jobs',JobViewSet)
router.register(r'skills',SkillViewSet)
router.register(r'jobskills',JobSkillViewSet)
router.register(r'quickjobapplications',QuickJobApplicationViewSet)
router.register(r'students',StudentViewSet)
router.register(r'jobapplications',JobApplicationViewSet)
router.register(r'jobapplicationcomments',JobApplicationCommentViewSet)
router.register(r'jobapplicationstatus',JobApplicationStatusViewSet)





urlpatterns = [

    path('',include(router.urls)),    

]


