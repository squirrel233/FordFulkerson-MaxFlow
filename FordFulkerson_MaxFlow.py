class Edge(object):
    def __init__(self, vertex1, vertex2, edgeCapacity):
        self.vertex1 = vertex1
        self.vertex2=vertex2
        self.capacity = capacity
    def __repr__(self): #used to print objects.
        print
        return "edge: %s->%s; capacity: %s; flow: %s" %(self.vertex1, self.vertex2, self.capacity) #returning edges with flow


class fordFulkersonMAxFlow(object):
    adjascent={} # edges or vertex!?!?!!?
    edgeFlow={} # flow of each edge

    def vertexAdd(self, vertex):
        self.adjascent[vertex]=[] #list of vertices adjascent ot given vertices

    def edgeAdd(self, vertex1, vertex2, edgeCapacity):
        if(vertex1 != vertex2):
            forwardEdge = Edge(vertex1, vertex2, capacity) #creating forward edges
            reverseEdge = Edge(vertex2, vertex1, 0) #creating back edges
