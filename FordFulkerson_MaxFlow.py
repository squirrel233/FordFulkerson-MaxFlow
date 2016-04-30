# written in python3. 

import time

class fordFulkersonMaxFlow(object):
    def __init__(self):
        self.adjascent = {}
        self.edgeFlow = {}

    def vertexAdd(self, vertex):
        self.adjascent[vertex]=[] #list of vertices adjascent to given vertices

    def getEdge(self, vertex):
        return(self.adjascent[vertex])

    def edgeAdd(self, vertex1, vertex2, edgeCapacity):
        forwardEdge = edgeInfo(vertex1, vertex2, edgeCapacity) #creating forward edges
        reverseEdge = edgeInfo(vertex2, vertex1, 0) #creating back edges
        forwardEdge.reverseEdge = reverseEdge 
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
            path=self.searchPath(source, sink, [])
        f2.write(str(self.edgeFlow))
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

ff=fordFulkersonMaxFlow()

#CHANGE FILENAMES HERE
f1=open('TestInput1.csv','r')
f2=open('TestOutput1.csv','w')

line=f1.readlines()[0:4]
line[0]=line[0].strip()
numNodes = line[0]
line[1]=line[1].strip()
numEdges= line[1]
line[2]=line[2].strip()
sourceNode=str(line[2])
line[3]=line[3].strip()
sinkNode=str(line[3])

f2.write("number of nodes  "), f2.write(numNodes)
f2.write("\nnumber of edges: "), f2.write(numEdges)
f2.write("\nsource node: "),f2.write(sourceNode)
f2.write("\nsink node: "), f2.write(sinkNode)
f1.close()
v1=[] #list of nodes at starting of edge
v2=[] #list of nodes at ending of edge
cap=[] #list of capacities of edge

#CHANGE FILENAME HERE
with open('TestInput1.csv') as f1:
	line=f1.readlines()[4:]
for item in line:
	node=item.split(",") #splitting each line to get startingNodes,endingNodes,capacity
	node[-1]=node[-1].strip()
	v1.append(str(node[0])) 
	v2.append(str(node[1]))
	cap.append(int(node[2]))

if(sourceNode in v2):
    f2.write("\nSource node cannot be an ending node for an edge")
    exit()
elif(sinkNode in v1):
    f2.write("\nSink node cannot be a starting node for an edge")
    exit()

[ff.vertexAdd(vertex) for vertex in v1]
[ff.vertexAdd(vertex) for vertex in v2]

for i in range(0,len(v1)):
	ff.edgeAdd(v1[i], v2[i], cap[i])
f2.write("\nmaximum flow across the given graph: ")
f2.write('\n')
start=time.time() #to measure start time of Ford-Fulkerson
f2.write(str(ff.findMaxFlow(sourceNode,sinkNode)))
end=time.time() #to measure end time of Ford-Fulkerson
totaltime=str(end-start)
f2.write("\n")
f2.write("\nTime Taken = ")
f2.write(totaltime)
