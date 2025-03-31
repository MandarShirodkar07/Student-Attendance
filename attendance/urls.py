
from django.urls import path
from .views import *

app_name = 'attendance'

urlpatterns = [
    # API-based registration and login views (Class-based views)
    path('api/register/', RegisterFacultyView.as_view(), name='api-register'),
    path('api/login/', LoginView.as_view(), name='api-login'),

    # Web-based registration and login views (Function-based views)
    path("",home, name="home"),
    path("login/",faculty_login, name="faculty_login"),
    path("register/", register, name="register"),
    path("dashboard/<int:faculty_id>/", dashboard, name="dashboard"),
    path("logout/", faculty_logout, name="faculty_logout"),
]

