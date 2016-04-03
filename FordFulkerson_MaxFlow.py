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
1) Can there be multiple source nodes or sink nodes??
2) Loops?? cus a path like s-a-b-a-c might exist but aba is a loop
3) Can there be multiple edges between the same 2 vertices???
does not handle multiple entries of wrong inputs. Only till count of e !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''
ff=fordFulkersonMaxFlow()
# see below for sample input
flag=1
while True:
    n=int(input("enter number of vertices: "))
    v=str(input("enter vertex labels(Note: first vertex will be source and last vertex will be sink). eg- sabcdt: "))
    setV=[]
    if(len(v)!=n): #checking if number of vertices is correct.
        print("incorrect number of vertices. Enter again \n")
        continue
    if(len(v)!=len(set(v))): #checking for duplicate vertices
        print("Duplicate vertices. Try again\n")
        continue
    print("source node: ", v[0])
    print("sink node: ", v[len(v)-1])
    v1List=[] #Stores all v1's entered. Used to ensure that source node is entered.
    v2List=[] #Stores all v2's entered. Used to ensure that sink node is entered
    [ff.vertexAdd(vertex) for vertex in v]
    e=int(input("enter number of edges: "))
    #count=e
    while(e!=0):
        v1=input("enter starting vertex of edge: ")
        if((v1 not in v) or v1==v[len(v)-1]): #the vertex must be present and cannot be sink node
            #count-=1
            print("ERROR: Invalid vertex.\n")#Attempts left= ",count )
            continue
        else:
            v1List.append(v1)
        v2=input("enter ending vertex of edge: ")
        if(v2 not in v or v2==v[0]): #the vertex must be present and cannot be source node.
            #count-=1
            print("ERROR: Invalid vertex.\n")#Attempts left= ",count)
            continue
        else:
            v2List.append(v2)
        c=int(input("enter edge capacity: "))
        if(c<0):
            #count-=1
            print("ERROR: edge capacity cannot be negative.\n")#Attempts left= ",count)
            continue
        else:
            if(len(setV)!=len(set(setV))):
                print("Edge already exists. Try again")
                continue
            e-=1
            ff.edgeAdd(v1, v2, c)

    if(v[0] not in v1List):
        print("\nSource node not entered. Start again \n")
        continue
    elif(v[len(v)-1] not in v2List):
        print("\nSink node not entered. Start again \n")
        continue
    else:
        print("maximum flow across the given graph:", (ff.findMaxFlow(v[0],v[len(v)-1])))

    print("")
    exit()

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
