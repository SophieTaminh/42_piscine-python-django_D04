from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .forms import my_form



def formulaire(request):
	# construction du formulaire vide
	form = my_form(request.POST)
	# si le formulaire est ok, recuperation des donnees
	if form.is_valid():
		text = form.cleaned_data['text']
		return HttpResponse("Merci")
		
	return render(request,'ex02/formulaire.html',{'form' : form})
		