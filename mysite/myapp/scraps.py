# This document contains attemps at improving our plot that didn't work out
# Namely, we wanted to plot heatmaps of probability density
# This would involve looping through every pixel in the display,
# finding the nearest data point, and assigning a probability to the pixel.
# This takes a very, very long time.

# first, build a simple logit model
import statsmodels.api as sm
from statsmodels.formula.api import logit as logit
  model = logit(formula = 'strike ~ px + pz', data = df)
  result = model.fit()
  df["probability_strike"] = result.fittedvalues
  df["probability_strike"] = 1/(1+np.exp(-df.probability_strike))

# create a 100x100 grid
  num_pixels = 100
  heat_map = [[0 for i in range(num_pixels)] for j in range(num_pixels)]

  min_x = np.amin(df["px"])
  max_x = np.amax(df["px"])
  x_range = max_x - min_x
  min_z = np.amin(df["pz"])
  max_z = np.amax(df["pz"])
  z_range = max_z - min_z
  # printing each pixel
  for i in range(num_pixels):
      for j in range(num_pixels):
          x = (i + 0.5)/num_pixels * x_range + min_x
          z = (j + 0.5)/num_pixels * z_range + min_z
          heat_map[i][j] = nearest_neighbor(x, z, df)
          print(heat_map[i][j])

  N = int(len(df.probability_strike)**.5)
  df.probability_strike = df.probability_strike.reshape(N, N)
  plt.plot(df["probability_strike"],
      extent = [-7,7,-7,7],
      # extent=(np.amin(df["px"]), np.amax(df["px"]), np.amin(df["pz"]), np.amax(df["pz"])),
      cmap=cm.hot)

      # a nearest neighbor function
      def nearest_neighbor(x_target, y_target, data):

          nearest_dist = float("inf")
          nearest_prob = 0
          for i, row in data.iterrows():        # using square distance to find closest data point
              x = row['px']
              y = row['pz']
              z = row['probability_strike']
              d = sq_dist(x_target, y_target, x, y)
              if d < nearest_dist:
                  nearest_dist = d              # assigning nearest probability
                  nearest_prob = z
          return nearest_prob
      # a square distance function for use in nearest_neighbor
      def sq_dist(x_0, y_0, x_1, y_1):
          return (x_0 - x_1)**2 + (y_0 - y_1)**2
