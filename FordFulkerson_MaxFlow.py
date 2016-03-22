class createEdge(object):
    def __init__(self, vertex1, vertex2, edgeCapacity):
        self.vertex1 = vertex1
        self.vertex2=vertex2
        self.edgeCapacity = edgeCapacity
    def __repr__(self): #used to print objects.
        print
        return "edge: %s->%s; capacity: %s; flow: %s" %(self.vertex1, self.vertex2, self.capacity) #returning edges with flow


class fordFulkersonMaxFlow(object):
    adjascent={}
    edgeFlow={}

    def edgeAdd(self, vertex1, vertex2, edgeCapacity):
        if(vertex1 != vertex2):
            forwardEdge = createEdge(vertex1, vertex2, capacity) #creating forward edges
            reverseEdge = createEdge(vertex2, vertex1, 0) #creating back edges
            forwardEdge.reverseEdge = forwardEdge # the back edge is a forward edge for a reverse network
            self.adjascent[vertex1].append(forwardEdge) #adding a forward edge from vertex1 to adjascent vertices
            self.adjascent[vertex2].append(reverseEdge) #adding a reverse edge from the adjascent vertices to vertex1
            self.flow[forwardEdge], self.flow[reverseEdge] = 0,0 #initially flow through every edge is 0
        else: #both vertices are same.
            print("ERROR: check graph as loop cannot occur")
            exit()

    def vertexAdd(self, vertex):
        self.adjascent[vertex]=[] #list of vertices adjascent ot given vertices
