import requests
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.core.files.base import ContentFile


def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('attendance:home')
		else:
			return view_func(request, *args, **kwargs)
	return wrapper_func