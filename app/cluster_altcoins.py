import numpy as np
import pandas as pd
from sklearn.cluster import SpectralClustering
import os
from datetime import datetime

directory = os.getcwd() + '/data'

filenames = []
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    df = pd.read_csv(f, header=None)
    timestamps = datetime.utcfromtimestamp(df[0][0]).strftime('%Y-%m-%d %H:%M:%S')
    filenames.append(filename[:-7])

df = pd.DataFrame({'coin' : filenames, 'start' : timestamps})

print(df)

df = pd.DataFrame({1 : [1,2,3], 2: [1,2,3], 3 : [1,2,3], 4 : [1,2,3]})

X = np.array(df.values.tolist())

print(X)

clustering = SpectralClustering(n_clusters=3, assign_labels='discretize', random_state=0).fit(X)

print(clustering.labels_)