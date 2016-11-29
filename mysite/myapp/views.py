# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect

from django.shortcuts import render

# from django.urls import reverse # future versions.
from django.core.urlresolvers import reverse_lazy
from .forms import InputForm


from os.path import join
from django.conf import settings

from .forms import InputForm

def form(request):
    #Races = request.GET.get('Race', '')
    params = {'form_action': reverse_lazy('myapp:form'),
        'form_method' : 'get',
        'form' : InputForm()}
    return render(request, 'form.html', params)

#from .forms import Plot

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(font_scale = 1.7)
#from matplotlib.patches import Rectangle

def index (request):
    return HttpResponse("baseball.")


def plot(request):

    filename = join(settings.STATIC_ROOT, 'myapp/selected_pitches.csv')
    df = pd.read_csv(filename)

    maskc = df.pitch_res=="C"
    maskb = df.pitch_res=="B"
    dfc = df[maskc]
    dfb = df[maskb]

    plot_dfc = dfc[["px", "pz"]]
    plot_dfb = dfb[["px", "pz"]]

    heatmapc, xedgesc, yedgesc = np.histogram2d(plot_dfc.px, plot_dfc.pz, bins=(64,64))

    heatmapb, xedgesb, yedgesb = np.histogram2d(plot_dfb.px, plot_dfb.pz, bins=(64,64))

    extentc = [xedgesc[0], xedgesc[-1], yedgesc[0], yedgesc[-1]]
    extentb = [xedgesb[0], xedgesb[-1], yedgesb[0], yedgesb[-1]]

    # Plot heatmap
    plt.clf()
    someX, someY = 0, 2.5
    fig,ax = plt.subplots()
    currentAxis = plt.gca()
    currentAxis.add_patch(Rectangle((someX - 0.6, someY - 1), 1.2, 2,
                          alpha=1, facecolor='none'))
    currentAxis.add_patch(Rectangle((someX - 1, someY - 1), 1.6, 2,
                          alpha=1, facecolor='none'))
    plt.title('Pitch Locations')
    # plt.ylabel('pz')
    # plt.xlabel('px')

    img1 = plt.imshow(heatmapc.T, cmap=plt.cm.Blues, alpha=1, interpolation='bilinear', extent=extentc)
    plt.hold(True)
    img2 = plt.imshow(heatmapb.T, cmap=plt.cm.Reds, alpha=0.7, interpolation='bilinear', extent=extentb)
    plt.ylim(0,4.5)
    plt.xlim(-3.5,3.5)
    #plt.show()

    return HttpResponse(Plot)
