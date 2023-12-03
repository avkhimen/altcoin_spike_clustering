import numpy as np
import pandas as pd
from sklearn.cluster import SpectralClustering

df = pd.DataFrame({1 : [1,2,3], 2: [1,2,3], 3 : [1,2,3], 4 : [1,2,3]})

X = np.array(df.values.tolist())

print(X)

clustering = SpectralClustering(n_clusters=3, assign_labels='discretize', random_state=0).fit(X)

print(clustering.labels_)