import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
data=pd.read_csv('C:/Users/AKASH/Django/myprojects/auto4you/proj1/final2.csv')
df=DataFrame(data,columns=['Cost','Number'])
kmeans=KMeans(n_clusters=5).fit(df)
centroids=kmeans.cluster_centers_
plt.scatter(df['Cost'],df['Number'],c=kmeans.labels_.astype(float),s=100,alpha=0.5)
plt.scatter(centroids[:,0],centroids[:,1],c='red',s=100)
plt.legend()
plt.show()