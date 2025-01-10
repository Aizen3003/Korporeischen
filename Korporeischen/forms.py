from django import forms
from Korporeischen import models

class Forms_Event(forms.ModelForm):
    class Meta:
        model = models.Event
        fields = ["name", "guests", "budget", "description", "date"]

class Swas_form(forms.Form):
    team = forms.ModelChoiceField(queryset=models.Team.objects.all(), label="Выберите команду")
    event = forms.ModelChoiceField(queryset=models.Event.objects.all(), label="Выберите событие")
