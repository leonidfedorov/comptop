class DisjointSets:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [0 for x in range(n)]
 
    def findSet(self, v):
        if not v == self.parent[v]:
            self.parent[v] = self.findSet(self.parent[v])
        return self.parent[v]
 
    def uniteSets(self, x, y):
        xLabel = self.findSet(x)
        yLabel = self.findSet(y)
        if xLabel == yLabel:
            return
        if self.size[xLabel] > self.size[yLabel]:
            self.parent[yLabel] = xLabel
        else:
            self.parent[xLabel] = yLabel
            if self.size[xLabel] == self.size[yLabel]:
                self.size[yLabel] += 1
 
    def getParent(self):
        #this will return a list of parents to every vertex, useful for testing
        return self.parent
 
#Test
 
if __name__ == '__main__':
    #we create a graph by initiating vertices
    uf = DisjointSets(9)
    print uf.getParent()
    #we create edges between vertices pairwise
    uf.uniteSets(1, 2)
    print uf.getParent() #we can see how list of parents changed after Union of vertice sets
    uf.uniteSets(3, 4)
    print uf.getParent()
    uf.uniteSets(4, 1)
    print uf.getParent()
    uf.uniteSets(7, 8)
    print uf.getParent()
    uf.uniteSets(5, 8)
    print uf.getParent()
 
    #check the components in resulting graph, because of DisjointSets data structure,
    #each component has a unique vertex(which we can call 'label' of the set)
    graph = {}
    for vertex in range(9): #go through each vertex
        label = uf.findSet(vertex) #find the 'label' of the set this vertex belongs to
        if not label in graph: #add component to graph if not already there
            graph[label] = set([vertex])
        else: #add vertex to component if it's 'label' vertex is already in the graph
            graph[label].add(vertex)
    print("\n Graph has", len(graph), "components: ")
    for component in graph.values():
        print(component)