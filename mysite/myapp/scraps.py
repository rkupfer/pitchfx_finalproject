# logit_cols = sm.(df[["px","pz"]].values)
  # logit = sm.Logit(df["strike"].astype(float), logit_cols)
  model = logit(formula = 'strike ~ px + pz', data = df)
  result = model.fit()
  df["probability_strike"] = result.fittedvalues
  df["probability_strike"] = 1/(1+np.exp(-df.probability_strike))

  num_pixels = 4
  heat_map = [[0 for i in range(num_pixels)] for j in range(num_pixels)]

  min_x = np.amin(df["px"])
  max_x = np.amax(df["px"])
  x_range = max_x - min_x
  min_z = np.amin(df["pz"])
  max_z = np.amax(df["pz"])
  z_range = max_z - min_z
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


      def nearest_neighbor(x_target, y_target, data):

          nearest_dist = float("inf")
          nearest_prob = 0
          for i, row in data.iterrows():
              x = row['px']
              y = row['pz']
              z = row['probability_strike']
              d = sq_dist(x_target, y_target, x, y)
              if d < nearest_dist:
                  nearest_dist = d
                  nearest_prob = z
          return nearest_prob

      def sq_dist(x_0, y_0, x_1, y_1):
          return (x_0 - x_1)**2 + (y_0 - y_1)**2
