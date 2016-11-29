from django import forms

class Plot(forms.ModelForm):

    Pitcher_Race = forms.ChoiceField(choices="Race", required=False,
                              widget=forms.Select())

    Pitcher_Ethnicity = forms.ChoiceField(choices="Hispanic",required=False,
                              widget=forms.Select())

    #League = forms.ChoiceField(choices=LEAGUE, required=False,
                              #widget=forms.Select())

    Park_Name = forms.ChoiceField(choices="park_name", required=False,
                              widget=forms.Select())

    Home_or_Away = forms.ChoiceField(choices="bat_home_id", required=False,
                              widget=forms.Select())

    #Umpire Race = forms.ChoiceField(choices=UMPRACE, required=False,
                              #widget=forms.Select())

    attrs = {'class ' : 'form-nav-control',
             'onchange ' : 'this.form.submit()'}
