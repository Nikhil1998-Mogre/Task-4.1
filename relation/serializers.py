from rest_framework import serializers
from .models import Employer,Tag,Job,Skill,JobSkill,QuickJobApplication,Student,JobApplication,JobApplicationComment,JobApplicationStatus
from django.contrib.auth.models import User


# create serilizers 
class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"

class JobSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSkill
        fields = "__all__"


class QuickJobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuickJobApplication
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = "__all__"


class JobApplicationCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplicationComment
        fields = "__all__"


class JobApplicationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplicationStatus
        fields = "__all__"