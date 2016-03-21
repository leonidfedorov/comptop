###in 'the Dutch' Computational Geometry book - very first algortihm
###Complexity bounded by O(n *log n) sorting, but otherwise is just O(n)
def convexHull(points):
    points = sorted(set(points))
    
    if len(points) <= 1:
        return points
        
    crossProduct = lambda o, a, b: (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    def goAround(points):
      branch = []
      for p in points:
          while len(lower) >= 2 and crossProduct(branch[-2], branch[-1], p) <= 0:
              branch.pop()
          branch.append(p)
      return branch[:-1]

    return goAround(points) + goAround(reversed(points))
#example check
assert convexHull([(i//10, i%10) for i in range(100)]) == [(0, 0), (9, 0), (9, 9), (0, 9)]
