from django.shortcuts import render
from sites import models

def homepage(request):
	return render(request, 'index.html',{})

