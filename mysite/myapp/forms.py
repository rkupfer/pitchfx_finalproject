from django import forms
from .models import Input, PITCHER_RACE, PITCHER_ETHNICITY, HOME_OR_AWAY
# PARK_NAME,

from django.forms import ModelForm

class InputForm(forms.ModelForm):

    pitcher_race = forms.ChoiceField(choices=PITCHER_RACE, required=False,
                              widget=forms.Select())

    pitcher_ethnicity = forms.ChoiceField(choices=PITCHER_ETHNICITY,required=False,
                              widget=forms.Select())

    # park_name = forms.ChoiceField(choices=PARK_NAME, required=False,
                            #   widget=forms.Select())

    home_or_away = forms.ChoiceField(choices=HOME_OR_AWAY, required=False,
                               widget=forms.Select())

    attrs = {'class' : 'form-nav-control',
             'onchange ' : 'this.form.submit()'}

    class Meta:
        model = Input
        fields = ['pitcher_race', 'pitcher_ethnicity', 'home_or_away']
        # 'park_name',




# class RaceForm(forms.ModelForm):
#
#     Pitcher_Race = forms.ChoiceField(choices="Pitcher_Race", required=False,
#                               widget=forms.Select())
#
# attrs = {'class ' : 'form-nav-control',
#              'onchange ' : 'this.form.submit()'}
#
# class Meta:
#     mode = Input
#     fields = ['Pitcher_Race']
#
#
# class EthnicityForm(forms.ModelForm):
#
#     Pitcher_Ethnicity = forms.ChoiceField(choices="Hispanic",required=False,
#                           widget=forms.Select())
# attrs = {'class ' : 'form-nav-control',
#              'onchange ' : 'this.form.submit()'}
#
# class Meta:
#     mode = Input
#     fields = ['Pitcher_Race']
#
#
# class ParkForm(forms.ModelForm):
#
#     Park_Name = forms.ChoiceField(choices="park_name", required=False,
#                           widget=forms.Select())
#
# attrs = {'class ' : 'form-nav-control',
#              'onchange ' : 'this.form.submit()'}
#
# class Meta:
#     mode = Input
#     fields = ['Pitcher_Race']
#
#
# class HomeAwayForm(forms.ModelForm):
#
#     Home_or_Away = forms.ChoiceField(choices="bat_home_id", required=False,
#                           widget=forms.Select())
#
# attrs = {'class ' : 'form-nav-control',
#              'onchange ' : 'this.form.submit()'}
#
# class Meta:
#     mode = Input
#     fields = ['Pitcher_Race']

#Umpire Race = forms.ChoiceField(choices=UMPRACE, required=False,
                          #widget=forms.Select())
#League = forms.ChoiceField(choices=LEAGUE, required=False,
                          #widget=forms.Select())
