from django.contrib import admin
from django.urls import path,include
from .views import EmployerviewSet,UserViewSet,TagViewSet,JobViewSet
from rest_framework import routers
from django.contrib.auth.models import User


router = routers.DefaultRouter()
router.register(r'employees',EmployerviewSet)
router.register(r'users',UserViewSet)
router.register(r'tags',TagViewSet)
router.register(r'jobs',JobViewSet)


urlpatterns = [

    path('',include(router.urls)),

]


