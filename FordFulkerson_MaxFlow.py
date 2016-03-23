class Edge(object):
    def __init__(self, vertex1, vertex2, edgeCapacity):
        if(vertex1!=vertex2):
            self.vertex1 = vertex1
            self.vertex2=vertex2
            self.edgeCapacity = edgeCapacity
        elif(vertex1==vertex2):
            print("ERROR: check graph for loops")
            exit()
    def __repr__(self): #used to print objects.
        print
        return("edge: %s->%s; capacity: %s; flow: %s" %(self.vertex1, self.vertex2, self.capacity)) #returning edges with flow


class fordFulkersonMaxFlow(object):
    def __init__(self):
        self.adjascent = {}
        self.edgeFlow = {}

    def vertexAdd(self, vertex):
        self.adjascent[vertex]=[] #list of vertices adjascent ot given vertices

    def getEdge(self, vertex):
        return(self.adjascent[vertex])

    def edgeAdd(self, vertex1, vertex2, edgeCapacity):
        forwardEdge = Edge(vertex1, vertex2, edgeCapacity) #creating forward edges
        reverseEdge = Edge(vertex2, vertex1, 0) #creating back edges
        forwardEdge.reverseEdge = forwardEdge # the back edge is a forward edge for a reverse network
        self.adjascent[vertex1].append(forwardEdge) #adding a forward edge from vertex1 to adjascent vertices
        self.adjascent[vertex2].append(reverseEdge) #adding a back edge from the adjascent vertices to vertex1
        self.edgeFlow[forwardEdge], self.edgeFlow[reverseEdge] = 0,0 #initially flow through every edge is 0

    def searchPath(self, source, sink, path):
        if(source==sink):
            return(path)
        for edge in self.getEdge(source) :
            resflow = edge.edgeCapacity - self.edgeFlow[edge] #calculating residual flow for each edge
            #initially residual flow is capacity of edge itself as flow is 0.

            if(resflow>0 and edge not in path):
                result=self.searchPath(edge.vertex2, sink, path+[edge])#adding that edge to current path
                if(result!=None):
                    return(path)

    def findMaxFlow(self, source, sink):
        path=self.searchPath(source, sink, [])
        while(path!=None):
            
            print(edge.edgeCapacity for edge in path)
            residualSetPath = [edge.edgeCapacity - self.edgeFlow[edge] for edge in path]#calculate residuals for all edges in that path
            flow=min(residualSetPath)
            for edge in path:
                self.edgeFlow[edge] = self.edgeFlow[edge] + flow
                self.edgeFlow[edge.reverseEdge] = self.edgeFlow[edge.reverseEdge] - flow
            path=self.searchPath(source, sink, [])
            print(self.edgeFlow)
            return ("max flow: %s " %(sum(self.edgeFlow[edge] for edge in self.get_edges(source))))


g = fordFulkersonMaxFlow()
[g.vertexAdd(v) for v in "sabcdt"]
g.edgeAdd('s','a',9)
g.edgeAdd('s','c',9)
g.edgeAdd('a','b',8)
g.edgeAdd('b','t',10)
g.edgeAdd('c','d',3)
g.edgeAdd('d','t',7)
g.edgeAdd('c','b',1)
print("maximum flow across the given graph:", (g.findMaxFlow('s','t')))
