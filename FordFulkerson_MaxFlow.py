class Edge(object):
    def __init__(self, vertex1, vertex2, edgeCapacity):
        self.vertex1 = vertex1
        self.vertex2=vertex2
        self.capacity = capacity
    def __repr__(self): #used to print objects.
        print
        return "edge: %s->%s; capacity: %s; flow: %s" %(self.vertex1, self.vertex2, self.capacity) #returning edges with flow


class fordFulkersonMaxFlow(object):
    adjascent={}
    edgeFlow={} # flow of each edge
