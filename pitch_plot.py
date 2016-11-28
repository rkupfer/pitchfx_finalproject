%matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

df = pd.read_csv("selected_pitches.csv")

mask = df.pitch_res=="C"
df = df[mask]

plot_df = df[["px", "pz"]]
plt.hist(plot_df.pz)

heatmap, xedges, yedges = np.histogram2d(plot_df.px, plot_df.pz, bins=(64,64))
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]


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

colors = plt.cm.Greys

plt.imshow(heatmap, cmap=plt.cm.Greys, alpha=.9, interpolation='bilinear', extent=extent)
plt.show()
