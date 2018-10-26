from django.shortcuts import render
from .models import Project

def list_chunk(inputx, size):
	if len(inputx) and size != 0:
		return [inputx[i : i + size] for i in range(0, len(inputx), size)]
	else:
		return None
# Create your views here.

def portfolio(request):
	p = Project.objects.all()
	projects = list_chunk(p, 3)
	
	return render(request, "portfolio/portfolio.html", {'projects':projects})


	