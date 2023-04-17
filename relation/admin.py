from django.contrib import admin
from .models import Employer,Tag,Job,Skill,JobSkill,QuickJobApplication,Student,JobApplication,JobApplicationComment


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'email', 'website', 'created_at', 'updated_at')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'employer', 'close_date', 'is_published']
    list_filter = ['is_published', 'employment_type']
    search_fields = ['title', 'employer', 'description']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(JobSkill)
class JobSkillAdmin(admin.ModelAdmin):
    list_display = ('job', 'skill', 'relevance', 'created_at', 'updated_at')
    list_filter = ('job', 'skill')
    search_fields = ('job__title', 'skill__name')
    ordering = ('-created_at',)


@admin.register(QuickJobApplication)
class QuickJobApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'job', 'name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('job', 'created_at')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'job', 'student', 'created_at')


@admin.register(JobApplicationComment)
class JobApplicationCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'job_application', 'author', 'comment', 'parent', 'created_at', 'updated_at')
    list_filter = ('job_application', 'author', 'parent', 'created_at', 'updated_at')
    search_fields = ('comment',)
    ordering = ('-created_at',)
