from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render



def formulaire(request):
	# construction du formulaire vide
	form = formulaire(request.POST)
	# si le formulaire est ok, recuperation des donnees
	if form.is_valid():
		text = form.cleaned_data['text']
		return HttpResponse("Merci")
		
	return render(request,'ex02/formulaire.html',{'form' : form})
		