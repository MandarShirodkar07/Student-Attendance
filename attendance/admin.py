from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Faculty, Department, Degree
from rest_framework.authtoken.models import Token

@admin.register(Faculty)
class FacultyAdmin(UserAdmin):  # Use UserAdmin to manage Faculty like a user
    list_display = ('id', 'username', 'email', 'department', 'degree', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('department', 'degree', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Academic Info', {'fields': ('department', 'degree')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'department', 'degree', 'is_staff', 'is_active')}
        ),
    )
    ordering = ('id',)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Degree)
class DegreeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    

