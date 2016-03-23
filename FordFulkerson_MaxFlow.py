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

    def edgeAdd(self, vertex1, vertex2, edgeCapacity):
        forwardEdge = Edge(vertex1, vertex2, edgeCapacity) #creating forward edges
        reverseEdge = Edge(vertex2, vertex1, 0) #creating back edges
        forwardEdge.reverseEdge = forwardEdge # the back edge is a forward edge for a reverse network
        self.adjascent[vertex1].append(forwardEdge) #adding a forward edge from vertex1 to adjascent vertices
        self.adjascent[vertex2].append(reverseEdge) #adding a back edge from the adjascent vertices to vertex1
        self.flow[forwardEdge], self.flow[reverseEdge] = 0,0 #initially flow through every edge is 0

    def vertexAdd(self, vertex):
        self.adjascent[vertex]=[] #list of vertices adjascent ot given vertices

    def getEdge(self, vertex):
        return(self.adjascent[vertex])

    def searchPath(self, source, sink, path):
        if(source==sink):
            return(path)
        for edge in getEdge(source) :
            resflow = edge.edgeCapacity - self.flow[edge] #calculating residual flow for each edge
            #initially residual flow is capacity of edge itself as flow is 0.

            if(resflow>0 and edge not in path):
                searchPath(edge.sink, sink, path+[edge])#adding that edge to current path
                if(result!=None):
                    return(path)

    def findMaxFlow(self, source, sink):
        path=self.searchPath(source, sink, [])
        while(path!=None):
            for edge in path :#calculate residuals for all edges in that path
                residualSetPath=edge.capacity - self.flow[edge]
            flow=min(residualSetPath)
            for edge in path:
                self.flow[edge] = self.flow[edge] + flow
                self.flow[edge.reverseEdge] = self.flow[edge.reverseEdge] - flow
            path=self.searchPath(source, sink, [])
            print(self.flow)
            return ("max flow: %s " %(sum(self.flow[edge] for edge in self.get_edges(source))))



'''
add_edge('s','a',9)
add_edge('s','c',9)
add_edge('a','t',10)
add_edge('c','t',7)
(max_flow('s','t')
'''
