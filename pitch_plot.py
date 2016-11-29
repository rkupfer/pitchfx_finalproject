%matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

df = pd.read_csv("selected_pitches.csv")

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
plt.show()
