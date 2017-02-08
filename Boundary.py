###Boundary class to implement Varshney, Ramamurthy ICASSP2015 'Persistent Topology of Descision Boundaries'###
###version 0.1 basic data structure: 
###---------------------------------initializes with 2 lists of points given by tuples of coordinates, 
###---------------------------------a distance function and an open ball radius###
###---------------------------------computes their adjacency matrix so there's an edge only between classes and only within radius


import numpy as np

class Boundary:

    def __init__(self, y1pts, y2pts, distfun, radius):
        self.y1pts = y1pts
        self.y2pts = y2pts
        self.radius = radius
        self.metric = distfun
        self.adjacency = np.empty((len(y1pts), len(y2pts), )

    def metric(self, distfun):
        self.metric = distfun
        return self.metric

    def distance(self, pt1, pt2):
        return self.metric(pt1, pt2)

    def connect(self):
        for pt1, pt2 in pairwise(self.y1pts, self.y2pts):
            if distance(pt1, pt2) <= self.radius:
                self.adjacency[y1pts.index(pt1), y2pts.index(pt2)] = 1
            else
                self.adjacency[y1pts.index(pt1), y2pts.index(pt2)] = 0

        return self.adjacency
