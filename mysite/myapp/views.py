# import modules
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from .forms import InputForm
from os.path import join
from django.conf import settings
from .forms import InputForm
from .models import RACE_DICT, ETHNICITY_DICT, HOME_DICT
# ,PARK_NAME_DICT
# we could have included park name, but it results in too small n for plots
# park name stuff is commented out throughout
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.patches import Rectangle
import sqlite3
import statsmodels.api as sm
from statsmodels.formula.api import logit as logit
from io import BytesIO


# defining a form where user can select parameters to filter data for plot
def form(request):
    pitcher_race = request.GET.get('pitcher_race', '')
    if not pitcher_race: pitcher_race = request.POST.get('pitcher_race', 'White')   # defaults

    pitcher_ethnicity = request.GET.get('pitcher_ethnicity', '')
    if not pitcher_ethnicity: pitcher_ethnicity = request.POST.get('pitcher_ethnicity', '0')

    # park_name = request.GET.get('park_name', '')
    # if not park_name: park_name = request.POST.get('park_name', 'Petco Park')

    home_or_away = request.GET.get('home_or_away', '')
    if not home_or_away: home_or_away = request.POST.get('home_or_away', '0')

    img_name = 'current_img.png'
    plot(pitcher_race, pitcher_ethnicity,
    # park_name,
    home_or_away, img_name)
    params = {'form_action': reverse_lazy('myapp:form'),
              'form_method' : 'get',
              'form' : InputForm({'pitcher_race' : pitcher_race, 'pitcher_ethnicity' : pitcher_ethnicity,
                                #   'park_name' : park_name,
                                'home_or_away' : home_or_away}),
              'pitcher_race' : RACE_DICT[pitcher_race],
              'pitcher_ethnicity' : ETHNICITY_DICT[pitcher_ethnicity],
            #   'park_name' : PARK_NAME_DICT[park_name],
              'home_or_away' : HOME_DICT[home_or_away],
              'img_name' : img_name}


    return render(request, 'form.html', params)

# defining a form class
from django.views.generic import FormView
class FormClass(FormView):

    template_name = 'form.html'
    form_class = InputForm


    def get(self, request):

      pitcher_race = request.GET.get('pitcher_race', 'Black')

      return render(request, self.template_name, {'form_action': reverse_lazy('myapp:form'),
                                                    'form_method' : 'get',
                                                    'form' : InputForm({'pitcher_race' : pitcher_race, 'pitcher_ethnicity' : pitcher_ethnicity,
                                                                        'park_name' : park_name, 'home_or_away' : home_or_away}),
                                                    'pitcher_race' : RACE_DICT[pitcher_race],
                                                    'pitcher_ethnicity' : ETHNICITY_DICT[pitcher_ethnicity],
                                                    # 'park_name' : PARK_NAME_DICT[park_name],
                                                    'home_or_away' : HOME_DICT[home_or_away],
                                                    'img_name' : img_name})

    def post(self, request):

      pitcher_race = request.POST.get('pitcher_race', 'Black')

      return render(request, self.template_name, {'form_action': reverse_lazy('myapp:form'),
                                                    'form_method' : 'get',
                                                    'form' : InputForm({'pitcher_race' : pitcher_race, 'pitcher_ethnicity' : pitcher_ethnicity,
                                                                        'park_name' : park_name, 'home_or_away' : home_or_away}),
                                                    'pitcher_race' : RACE_DICT[pitcher_race],
                                                    'pitcher_ethnicity' : ETHNICITY_DICT[pitcher_ethnicity],
                                                    # 'park_name' : PARK_NAME_DICT[park_name],
                                                    'home_or_away' : HOME_DICT[home_or_away],
                                                    'img_name' : img_name})


# our homepage
def index (request):
    return HttpResponse("baseball.")

# plotting a heatmap
def plot(pitcher_race, pitcher_ethnicity, home_or_away, img_name):

    IMGROOT = settings.BASE_DIR + '/myapp/static/'
    filename = join(settings.STATIC_ROOT, 'myapp/selected_pitches.csv')     # pulling in the .csv
    df = pd.read_csv(filename)

    # We ran the website with a SQL database, but it was much slower.
    # The SQL database is 260mb, while the .csv is 12mb.
    # The code for the SQL database is below:

    # con = sqlite3.connect("pitch_tables.sql")
    # query = ""
    # for l in open("pitch_extract.sql"): query += l
    # df = pd.read_sql_query(query,con)
    # con.close()
    # df.px = df.px.astype(float).fillna(0.0)
    # df.pz = df.pz.astype(float).fillna(0.0)

    # applying masks based on user selections
    maskrace = df.Race == pitcher_race
    maskethnicity = df.Hispanic == int(pitcher_ethnicity)
    # maskname = df.park_name == park_name
    maskhome = df.bat_home_id == int(home_or_away)
    df = df.loc[maskrace]
    df = df.loc[maskethnicity]
    df = df.loc[maskhome]
    # df = df[maskname]

    # applying masks on pitch type: only called strikes and balls
    maskpitch = (df.pitch_res == "C") | (df.pitch_res == "B")
    df = df.loc[maskpitch]
    df["strike"] = df.pitch_res == "C"
    df["strike"] = df["strike"].astype(float)
    maskc = df.pitch_res=="C"
    maskb = df.pitch_res=="B"
    # two dataframes allows for overlaid plots
    dfc = df[maskc]
    dfb = df[maskb]
    # dataframes for plots - need x and z locations, know pitch outcome based on df
    plot_dfc = dfc[["px", "pz"]]
    plot_dfb = dfb[["px", "pz"]]

    # defining heatmaps using histograms
    heatmapc, xedgesc, yedgesc = np.histogram2d(plot_dfc.px, plot_dfc.pz, bins=(32,32))
    heatmapb, xedgesb, yedgesb = np.histogram2d(plot_dfb.px, plot_dfb.pz, bins=(32,32))

    extentc = [xedgesc[0], xedgesc[-1], yedgesc[0], yedgesc[-1]]
    extentb = [xedgesb[0], xedgesb[-1], yedgesb[0], yedgesb[-1]]

    # Plot heatmap
    plt.clf()
    someX, someY = 0, 2.5
    fig, ax = plt.subplots()

    # overlaying strike zones, one for lefties and one for righties
    currentAxis = plt.gca()
    currentAxis.add_patch(Rectangle((someX - 0.6, someY - 1), 1.2, 2,
                          alpha=1, facecolor='none'))
    currentAxis.add_patch(Rectangle((someX - 1, someY - 1), 1.6, 2,
                          alpha=1, facecolor='none', linestyle = 'dashed'))


    plt.title('Pitch Locations')
    # two images, overlaid
    img1 = plt.imshow(heatmapc.T, cmap=plt.cm.Blues, alpha=1, interpolation='spline16', origin = 'lower', extent=extentc)
    plt.hold(True)
    img2 = plt.imshow(heatmapb.T, cmap=plt.cm.Reds, alpha=0.65, interpolation='spline16', origin = 'lower', extent=extentb)

    plt.ylim(0,4.5)
    plt.xlim(-3.5,3.5)
    # saving plot as an image, overwriting old request with new one
    figfile = open(IMGROOT + img_name, 'w+b')

    plt.savefig(figfile, format = "png", bbox_inches='tight', pad_inches=0)

def form2(request):
    pitcher_name= request.GET.get('pitcher_name', '')
    if not pitcher_race: pitcher_race = request.POST.get('pitcher_name', 'Aaron Sanchez')

    img_name = 'current_img.png'

    plot2(pitcher_name, img_name)
    params = {'form_action': reverse_lazy('myapp:form'),
            'form_method' : 'get',
            'form' : InputForm({'pitcher_name' : pitcher_name}),
            'pitcher_name' : NAME_DICT[pitcher_name],
            'img_name' : img_name}
    return render(request, 'form2.html', params)



def plot2(pitcher_name, img_name):

    # print(settings.STATIC_ROOT)
    IMGROOT = settings.BASE_DIR + '/myapp/static/'
    # print(IMGROOT)
    # print(pitcher_race, pitcher_ethnicity, park_name, home_or_away)
    filename = join(settings.STATIC_ROOT, 'myapp/selected_pitches.csv')
    df = pd.read_csv(filename)
    # con = sqlite3.connect("pitch_tables.sql")
    # query = ""
    # for l in open("pitch_extract.sql"): query += l
    # df = pd.read_sql_query(query,con)
    # con.close()
    # df.px = df.px.astype(float).fillna(0.0)
    # df.pz = df.pz.astype(float).fillna(0.0)

    maskname = (df.Name == pitcher_name)
    df = df[maskname]

    maskpitch = (df.pitch_res == "C") | (df.pitch_res == "B")
    df = df.loc[maskpitch]
    df["strike"] = df.pitch_res == "C"
    df["strike"] = df["strike"].astype(float)

    maskc = df.pitch_res=="C"
    maskb = df.pitch_res=="B"
    dfc = df[maskc]
    dfb = df[maskb]
    plot_dfc = dfc[["px", "pz"]]
    plot_dfb = dfb[["px", "pz"]]

    heatmapc, xedgesc, yedgesc = np.histogram2d(plot_dfc.px, plot_dfc.pz, bins=(32,32))

    heatmapb, xedgesb, yedgesb = np.histogram2d(plot_dfb.px, plot_dfb.pz, bins=(32,32))

    extentc = [xedgesc[0], xedgesc[-1], yedgesc[0], yedgesc[-1]]
    extentb = [xedgesb[0], xedgesb[-1], yedgesb[0], yedgesb[-1]]

    # Plot heatmap
    plt.clf()
    someX, someY = 0, 2.5
    fig, ax = plt.subplots()
    currentAxis = plt.gca()
    currentAxis.add_patch(Rectangle((someX - 0.6, someY - 1), 1.2, 2,
                          alpha=1, facecolor='none'))
    currentAxis.add_patch(Rectangle((someX - 1, someY - 1), 1.6, 2,
                          alpha=1, facecolor='none', linestyle = 'dashed'))


    plt.title('Pitch Locations')

    img1 = plt.imshow(heatmapc.T, cmap=plt.cm.Blues, alpha=1, interpolation='spline16', origin = 'lower', extent=extentc)
    plt.hold(True)
    img2 = plt.imshow(heatmapb.T, cmap=plt.cm.Reds, alpha=0.65, interpolation='spline16', origin = 'lower', extent=extentb)

    plt.ylim(0,4.5)
    plt.xlim(-3.5,3.5)

    from io import BytesIO
    figfile = open(IMGROOT + img_name, 'w+b')

    plt.savefig(IMGROOT + img_name, format = "png", , bbox_inches='tight', pad_inches=0)

def our_data(request):
    return render(request, "our_data.html")

def display_table(request):

    import pandas as pd
    import numpy as np

    df = pd.DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e'])
    table = df.to_html(float_format = "%.3f", classes = "table table-striped", index_names = False)
    table = table.replace('border="1"','border="0"')
    table = table.replace('style="text-align: right;"', "") # control this in css, not pandas.

    return render(request, 'view_table.html', {"title" : "An astounding table", "html_table" : table})
