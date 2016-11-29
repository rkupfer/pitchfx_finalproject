from django import forms
from .models import Input, Pitcher_Race
from django.forms import ModelForm

class InputForm(forms.ModelForm):

    Pitcher_Race = forms.ChoiceField(choices="Pitcher_Race", required=False,
                              widget=forms.Select())

attrs = {'class ' : 'form-nav-control',
             'onchange ' : 'this.form.submit()'}

class Meta:
    mode = Input
    fields = ['Pitcher_Race']


class InputForm(forms.ModelForm):

    Pitcher_Ethnicity = forms.ChoiceField(choices="Hispanic",required=False,
                          widget=forms.Select())
attrs = {'class ' : 'form-nav-control',
             'onchange ' : 'this.form.submit()'}

class Meta:
    mode = Input
    fields = ['Pitcher_Race']


class InputForm(forms.ModelForm):

    Park_Name = forms.ChoiceField(choices="park_name", required=False,
                          widget=forms.Select())

attrs = {'class ' : 'form-nav-control',
             'onchange ' : 'this.form.submit()'}

class Meta:
    mode = Input
    fields = ['Pitcher_Race']


class InputForm(forms.ModelForm):

    Home_or_Away = forms.ChoiceField(choices="bat_home_id", required=False,
                          widget=forms.Select())

attrs = {'class ' : 'form-nav-control',
             'onchange ' : 'this.form.submit()'}

class Meta:
    mode = Input
    fields = ['Pitcher_Race']

#Umpire Race = forms.ChoiceField(choices=UMPRACE, required=False,
                          #widget=forms.Select())
#League = forms.ChoiceField(choices=LEAGUE, required=False,
                          #widget=forms.Select())
