from django.conf import settings

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
	return render(request, 'index.html')
	