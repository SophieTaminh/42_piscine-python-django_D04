from django import forms

class my_form(forms.Form):
	text = forms.CharField(label='commentaire',max_length=100)
