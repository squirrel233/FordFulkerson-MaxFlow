# written in python3. 

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
'''
ff=fordFulkersonMaxFlow()

# see below for sample input

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
    v1List=[] #Stores all v1's entered. Used to ensure that source node is entered and sink node cannot be entered.
    v2List=[] #Stores all v2's entered. Used to ensure that sink node is entered and source node cannot be entered.
    [ff.vertexAdd(vertex) for vertex in v]
    e=int(input("enter number of edges: "))
    while(e!=0):
        v1=input("enter starting vertex of edge: ")
        if((v1 not in v) or v1==v[len(v)-1]): #the vertex must be present and cannot be sink node
            print("ERROR: Invalid vertex.\n")
            continue
        else:
            v1List.append(v1)
        v2=input("enter ending vertex of edge: ")
        if(v2 not in v or v2==v[0]): #the vertex must be present and cannot be source node.
            print("ERROR: Invalid vertex.\n")
            continue
        else:
            v2List.append(v2)
        c=int(input("enter edge capacity: "))
        if(c<0):
            #count-=1
            print("ERROR: edge capacity cannot be negative.\n")
            continue
        else:
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

#Sample input and output. Input based on figure "SampleInput.jpeg which is in the compressed folder"
#sample input taken from http://lpsolve.sourceforge.net/5.5/DIMACS_maxf.htm
'''
enter number of vertices: 6
enter vertex labels(Note: first vertex will be source and last vertex will be sink). eg- sabcdt: abcdef
source node:  a
sink node:  f
enter number of edges: 8
enter starting vertex of edge: a
enter ending vertex of edge: b
enter edge capacity: 5
enter starting vertex of edge: a
enter ending vertex of edge: c
enter edge capacity: 15
enter starting vertex of edge: b
enter ending vertex of edge: d
enter edge capacity: 5
enter starting vertex of edge: b
enter ending vertex of edge: e
enter edge capacity: 5
enter starting vertex of edge: c
enter ending vertex of edge: d
enter edge capacity: 5
enter starting vertex of edge: c
enter ending vertex of edge: e
enter edge capacity: 5
enter starting vertex of edge: d
enter ending vertex of edge: f
enter edge capacity: 15
enter starting vertex of edge: e
enter ending vertex of edge: f
enter edge capacity: 5
{
 edge: d->f; capacity: 15; flow: : 10, 
 edge: e->c; capacity: 0; flow: : -5, 
 edge: c->d; capacity: 5; flow: : 5, 
 edge: a->b; capacity: 5; flow: : 5, 
 edge: b->a; capacity: 0; flow: : -5, 
 edge: c->e; capacity: 5; flow: : 5, 
 edge: a->c; capacity: 15; flow: : 10, 
 edge: c->a; capacity: 0; flow: : -10, 
 edge: f->e; capacity: 0; flow: : -5, 
 edge: f->d; capacity: 0; flow: : -10, 
 edge: e->b; capacity: 0; flow: : 0, 
 edge: b->d; capacity: 5; flow: : 5, 
 edge: d->b; capacity: 0; flow: : -5, 
 edge: e->f; capacity: 5; flow: : 5, 
 edge: d->c; capacity: 0; flow: : -5, 
 edge: b->e; capacity: 5; flow: : 0}
maximum flow across the given graph: 15

'''
