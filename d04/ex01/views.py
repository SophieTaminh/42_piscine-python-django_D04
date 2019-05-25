from django.http import HttpResponse
from django.template import loader


def django(request):
	template = loader.get_template('ex01/django.html')
	context = {}
	return HttpResponse(template.render(context, request))

def affichage(request):
	template = loader.get_template('ex01/affichage.html')
	context = {}
	return HttpResponse(template.render(context, request))

def templates(request):
	template = loader.get_template('ex01/templates.html')
	context = {}
	return HttpResponse(template.render(context, request))