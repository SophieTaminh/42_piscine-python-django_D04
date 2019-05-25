from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def formulaire(request):
	if (request.method == "POST"):
		form = my_form(request.POST)
		if form.is_valid():
			text = form.cleaned_data['text']
			return HttpResponse("Merci")
		else:
			form = my_form()
		return render(request,'ex02/formulaire.html',{'form' : form})
	