from django import forms
from .models import Input, PITCHER_RACE, PITCHER_ETHNICITY, HOME_OR_AWAY, PITCHER_NAME
from django.forms import ModelForm

class InputForm(forms.ModelForm):

    pitcher_race = forms.ChoiceField(choices=PITCHER_RACE, required=False,
                              widget=forms.Select())

    pitcher_ethnicity = forms.ChoiceField(choices=PITCHER_ETHNICITY,required=False,
                              widget=forms.Select())

    home_or_away = forms.ChoiceField(choices=HOME_OR_AWAY, required=False,
                               widget=forms.Select())
    attrs = {'class' : 'form-nav-control',
             'onchange ' : 'this.form.submit()'}

    class Meta:
        model = Input
        fields = ['pitcher_race', 'pitcher_ethnicity', 'home_or_away']

class NameForm(forms.ModelForm):

    pitcher_name = forms.ChoiceField(choices=PITCHER_NAME, required=False,
                              widget=forms.Select())

    attrs = {'class' : 'form-nav-control',
             'onchange ' : 'this.form.submit()'}
    class Meta:
        model = Input
        fields = ['pitcher_name']
