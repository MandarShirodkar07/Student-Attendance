from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout, authenticate, get_user_model 
from django.contrib.auth.models import update_last_login
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from .helper import *
from .models import *
from .serializers import *

User = get_user_model()


class RegisterFacultyView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = FacultySerializer
    permission_classes = [AllowAny]

class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        # Authenticate user using email
        user = authenticate(email = email, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            update_last_login(None, user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "email": user.email
            }, status=status.HTTP_200_OK)

        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


def home(request):
    return render(request, "attendance_base.html")

@unauthenticated_user
def faculty_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(email=email, password=password)
        
        if user is not None:
            faculty_id = user.id
            auth_login(request, user)
            faculty = Faculty.objects.get(id=faculty_id)
            return redirect("attendance:dashboard", faculty.id)  # Redirect to dashboard after login
        else:
            messages.error(request, "Invalid email or password.")
            return render(request, "faculty_login.html")
    return render(request, "faculty_login.html")

@unauthenticated_user
def register(request):
    departments = Department.objects.all()  # Fetch all departments
    degrees = Degree.objects.all()  # Fetch all degrees

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        department_id = request.POST.get("department")
        degree_id = request.POST.get("degree")

        # Check if email already exists
        if Faculty.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
        else:
            department = Department.objects.get(id=department_id) if department_id else None
            degree = Degree.objects.get(id=degree_id) if degree_id else None

            user = Faculty.objects.create_user(
                username=username, 
                email=email, 
                password=password,
                first_name=first_name,
                last_name=last_name,
                department=department,
                degree=degree
            )
            user.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect("attendance:faculty_login")
    return render(request, "register.html", {"departments": departments, "degrees": degrees})

@login_required
def dashboard(request, faculty_id):
    faculty = get_object_or_404(Faculty, id=faculty_id)
    return render(request, "dashboard.html", {"faculty": faculty})

def faculty_logout(request):
    logout(request)
    return redirect("attendance:faculty_login")
