from Heap import Heap
import logging
logging.basicConfig(level=logging.DEBUG)

# infile = "infile.txt"  # TODO make this dynamic with a script
infile = "test2.txt"  # S1 T2 X3 Y4 Z5
with open(infile, "r") as file1:
    fileAsList = file1.readlines()

nV = int(fileAsList[0])

nE = len(fileAsList) - 1

print("Number of Vertices: %d", nV)
print("Number of Edges: %d", nE)

adjList = []
i = 0
while (i <= nV):
    adjList.append([])
    i += 1
print(adjList)

idMap = {}  # Dictionary that will be used to translate back and forth between the ordered pair of each edge and its id.
i = 1
while(i <= nE):
    # logging.debug(i)
    splitString = fileAsList[i].split()
    # logging.debug(splitString)
    edgeOrigin = int(splitString[0])
    edgeDestination = int(splitString[1])
    weight = int(splitString[2])
    adjList[edgeOrigin].append((edgeDestination, weight))
    idMap[i] = (edgeOrigin, edgeDestination)
    idMap[(edgeOrigin, edgeDestination)] = i
    i += 1

print(adjList)

print("Printing the input graph in adjacency list representation...")
i = 1
while(i <= nV):  # iterate through vertices
    for edge in adjList[i]:  # iterate through the edges of each vertex
        print("(", i, "->", edge[0], "):", edge[1], end="\t\t")  # TODO clean up formatting if time permits
    print()
    i += 1

d = {}
pi = {}
i = 1
while(i <= nV):  # loop performs Initialize_Single_Source()
    d[i] = float('inf')
    pi[i] = None
    i += 1
d[1] = 0

print("keys: ", d)

pQ = Heap(d, nV)
