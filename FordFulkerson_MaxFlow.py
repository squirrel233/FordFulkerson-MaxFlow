class edgeInfo(object):
    def __init__(self, vertex1, vertex2, edgeCapacity):
        if(vertex1!=vertex2):
            self.vertex1 = vertex1
            self.vertex2=vertex2
            self.edgeCapacity = edgeCapacity
        elif(vertex1==vertex2):
            print("ERROR: check graph for self-loops")
            exit()
    def __repr__(self): #used to print objects.
        return("\n edge: %s->%s; capacity: %s; flow: " %(self.vertex1, self.vertex2, self.edgeCapacity)) #returning edges with flow


class fordFulkersonMaxFlow(object):
    def __init__(self):
        self.adjascent = {}
        self.edgeFlow = {}

    def vertexAdd(self, vertex):
        self.adjascent[vertex]=[] #list of vertices adjascent ot given vertices

    def getEdge(self, vertex):
        return(self.adjascent[vertex])

    def edgeAdd(self, vertex1, vertex2, edgeCapacity):
        forwardEdge = edgeInfo(vertex1, vertex2, edgeCapacity) #creating forward edges
        reverseEdge = edgeInfo(vertex2, vertex1, 0) #creating back edges
        forwardEdge.reverseEdge = reverseEdge # the back edge is a forward edge for a reverse network
        reverseEdge.reverseEdge = forwardEdge
        self.adjascent[vertex1].append(forwardEdge) #adding a forward edge from vertex1 to adjascent vertices
        self.adjascent[vertex2].append(reverseEdge) #adding a back edge from the adjascent vertices to vertex1
        self.edgeFlow[forwardEdge], self.edgeFlow[reverseEdge] = 0,0 #initially flow through every edge is 0

    def searchPath(self, source, sink, path):
        if(source==sink):
            return(path)
        for edge in self.getEdge(source) :
            #initially residual flow is capacity of edge itself as flow is 0.
            resflow = edge.edgeCapacity - self.edgeFlow[edge] #calculating residual flow for each edge
            if(resflow>0 and edge not in path):
                result=self.searchPath(edge.vertex2, sink, path+[edge])#adding that edge to current path
                if(result!=None):
                    return(result)

    def findMaxFlow(self, source, sink):
        path=self.searchPath(source, sink, [])
        while(path!=None):
            residualSetPath = [edge.edgeCapacity - self.edgeFlow[edge] for edge in path]#calculate residuals for all edges in that path
            flow=min(residualSetPath)
            for edge in path:
                self.edgeFlow[edge] += flow
                self.edgeFlow[edge.reverseEdge] -= flow
                #print(edge, self.edgeFlow[edge], self.edgeFlow[edge.reverseEdge]) #prints each edge along with the forward flow and reverse flow
            path=self.searchPath(source, sink, [])
        print(self.edgeFlow)
        return (sum(self.edgeFlow[edge] for edge in self.getEdge(source)))


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
