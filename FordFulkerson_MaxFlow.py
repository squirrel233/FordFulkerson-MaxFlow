# written in python3

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


'''HANDLE WRONG INPUT CASES!!!!!!!!!!!!!!!!!!!!
1) number of edges must be greater than number of vertices??
2) Can there be multiple source nodes or sink nodes??
4) Loops?? cus a path like sabac might exist but aba is a loop
'''
ff=fordFulkersonMaxFlow()
# see below for sample input
n=int(input("enter number of vertices: "))
v=str(input("enter vertex labels(Note: first vertex will be source and last vertex will be sink). eg- sabcdt: "))
if(len(v)!=n):
    print("incorrect number of vertices")
    exit()
print("source node: ", v[0])
print("sink node: ", v[len(v)-1])
v1List=[] #Stores all v1's entered. Used to ensure that source node is entered.
v2List=[] #Stores all v2's entered. Used to ensure that sink node is entered
[ff.vertexAdd(vertex) for vertex in v]
e=int(input("enter number of edges: "))
for i in range(0,e):
    v1=input("enter starting vertex of edge: ")
    if(v1 not in v or v1==v[len(v)-1]): #the vertex must be present and cannot be sink node
        print("ERROR: Invalid vertex")
        exit()
    else:
        v1List.append(v1)
    v2=input("enter ending vertex of edge: ")
    if(v2 not in v or v2==v[0]): #the vertex must be present and cannot be source node.
        print("ERROR: Invalid vertex")
        exit()
    else:
        v2List.append(v2)
    c=int(input("enter edge capacity: "))
    if(c>0):
        ff.edgeAdd(v1, v2, c)
    else:
        print("ERROR: edge capacity cannot be negative ")
if(v[0] not in v1List):
    print("Source node not entered.")
    exit();
elif(v[len(v)-1] not in v2List):
    print("Sink node not entered")
    exit();
else:
    print("maximum flow across the given graph:", (ff.findMaxFlow(v[0],v[len(v)-1])))


'''
enter number of vertices: 6
enter vertex labels(Note: first vertex will be source and last vertex will be sink). eg- sabcdt: sabcdt
source node:  s
sink node:  t
enter number of edges: 7
enter starting vertex of edge: s
enter ending vertex of edge: a
enter edge capacity: 9
enter starting vertex of edge: s
enter ending vertex of edge: c
enter edge capacity: 8
enter starting vertex of edge: a
enter ending vertex of edge: b
enter edge capacity: 8
enter starting vertex of edge: b
enter ending vertex of edge: t
enter edge capacity: 10
enter starting vertex of edge: c
enter ending vertex of edge: d
enter edge capacity: 3
enter starting vertex of edge: d
enter ending vertex of edge: t
enter edge capacity: 7
enter starting vertex of edge: c
enter ending vertex of edge: b
enter edge capacity: 1
'''
