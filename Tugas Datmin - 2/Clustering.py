from turtle import distance
from sklearn import cluster
from sklearn.cluster import AgglomerativeClustering as AC
import numpy as np
import sys
class Clustering:
    np.set_printoptions(threshold=sys.maxsize)
    def buildCluster(self,Vector,dt):
        Clustering=AC(n_clusters=None,
        affinity='Cosine',
        linkage='single',
        distance_threshold=dt)
        Clustering.fit(Vector)
        return Clustering
        