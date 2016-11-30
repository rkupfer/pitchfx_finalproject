# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect

from django.shortcuts import render

# from django.urls import reverse # future versions.
from django.core.urlresolvers import reverse_lazy
from .forms import InputForm


from os.path import join
from django.conf import settings

from .forms import InputForm
from .models import RACE_DICT, ETHNICITY_DICT, PARK_NAME_DICT, HOME_DICT
# Pitcher_Ethnicity, Park_Name, Home_or_Away,
def form(request):
    pitcher_race = request.GET.get('pitcher_race', '')
    if not pitcher_race: pitcher_race = request.POST.get('pitcher_race', 'Black')

    pitcher_ethnicity = request.GET.get('pitcher_ethnicity', '')
    if not pitcher_ethnicity: pitcher_ethnicity = request.POST.get('pitcher_ethnicity', '0')

    park_name = request.GET.get('park_name', '')
    if not park_name: park_name = request.POST.get('park_name', 'Petco Park')

    home_or_away = request.GET.get('home_or_away', '')
    if not home_or_away: home_or_away = request.POST.get('home_or_away', '0')

    # plot = "<p> hi there </p>"
    params = {'form_action': reverse_lazy('myapp:form'),
              'form_method' : 'get',
              'form' : InputForm({'pitcher_race' : pitcher_race, 'pitcher_ethnicity' : pitcher_ethnicity,
                                  'park_name' : park_name, 'home_or_away' : home_or_away}),
              'pitcher_race' : RACE_DICT[pitcher_race],
              'pitcher_ethnicity' : ETHNICITY_DICT[pitcher_ethnicity],
              'park_name' : PARK_NAME_DICT[park_name],
              'home_or_away' : HOME_DICT[home_or_away],
              'plot' : plot(pitcher_race, pitcher_ethnicity, park_name, home_or_away)}


    return render(request, 'form.html', params)

from django.views.generic import FormView
class FormClass(FormView):

    template_name = 'form.html'
    form_class = InputForm


    def get(self, request):

      pitcher_race = request.GET.get('pitcher_race', 'Black')

      return render(request, self.template_name, {'form_action': reverse_lazy('myapp:form'),
                                                  'form_method' : 'get',
                                                  'form' : InputForm({'Race' : Race}),
                                                  'pitcher_race' : RACE_DICT[pitcher_race]})

    def post(self, request):

      pitcher_race = request.POST.get('pitcher_race', 'Black')

      return render(request, self.template_name, {'form_action': reverse_lazy('myapp:form'),
                                                  'form_method' : 'get',
                                                  'form' : InputForm({'Race' : Race}),
                                                  'pitcher_race' : RACE_DICT[pitcher_race]})


#from .forms import Plot

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt, mpld3
from matplotlib.patches import Rectangle

def index (request):
    return HttpResponse("baseball.")


def plot(pitcher_race, pitcher_ethnicity, park_name, home_or_away):
    # print(pitcher_race, pitcher_ethnicity, park_name, home_or_away)
    filename = join(settings.STATIC_ROOT, 'myapp/selected_pitches.csv')
    df = pd.read_csv(filename)
    # print(df.head())
    maskrace = df.Race == pitcher_race
    maskethnicity = df.Hispanic == int(pitcher_ethnicity)
    maskname = df.park_name == park_name
    maskhome = df.bat_home_id == int(home_or_away)

    print("check")
    df = df[maskrace & maskethnicity & maskname & maskhome]
    print("check2")
    maskc = df.pitch_res=="C"
    print("check3")
    maskb = df.pitch_res=="B"
    print("check4")
    dfc = df[maskc]
    print("check5")
    dfb = df[maskb]
    print("check6")
    plot_dfc = dfc[["px", "pz"]]
    print("check7")
    plot_dfb = dfb[["px", "pz"]]
    print("check8")

    heatmapc, xedgesc, yedgesc = np.histogram2d(plot_dfc.px, plot_dfc.pz, bins=(64,64))

    heatmapb, xedgesb, yedgesb = np.histogram2d(plot_dfb.px, plot_dfb.pz, bins=(64,64))

    extentc = [xedgesc[0], xedgesc[-1], yedgesc[0], yedgesc[-1]]
    extentb = [xedgesb[0], xedgesb[-1], yedgesb[0], yedgesb[-1]]

    # Plot heatmap
    plt.clf()
    someX, someY = 0, 2.5
    fig, ax = plt.subplots()
    # currentAxis = plt.gca()
    # currentAxis.add_patch(Rectangle((someX - 0.6, someY - 1), 1.2, 2,
    #                       alpha=1, facecolor='none'))
    # currentAxis.add_patch(Rectangle((someX - 1, someY - 1), 1.6, 2,
    #                       alpha=1, facecolor='none'))
    #plt.add_patch(Rectangle((someX - 0.6, someY - 1), 1.2, 2,
                          #alpha=1, facecolor='none'))
    #plt.add_patch(Rectangle((someX - 1, someY - 1), 1.6, 2,
                          #alpha=1, facecolor='none'))

    plt.title('Pitch Locations')
    # plt.ylabel('pz')
    # plt.xlabel('px')

    img1 = plt.imshow(heatmapc.T, cmap=plt.cm.Blues, alpha=1, interpolation='bilinear', extent=extentc)
    plt.hold(True)
    img2 = plt.imshow(heatmapb.T, cmap=plt.cm.Reds, alpha=0.7, interpolation='bilinear', extent=extentb)

    print("check9")

    plt.ylim(0,4.5)
    plt.xlim(-3.5,3.5)

    print("check10")
    plt.show()
    print("check11")
    return "<p> hi </p>"
    #
    # from io import BytesIO
    # figfile = BytesIO
    #
    # plt.savefig(figfile, format = "png")
    # figfile.seek(0)
    return HttpResponse(figfile.read(), content_type = "image/png")
