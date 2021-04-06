# CS3340B       Winter 2021 Assignment 3    Due: Apr 6, 2021
# James Walsh   jwalsh57    250481718

import sys
from heap import Heap
import logging
logging.basicConfig(level=logging.WARNING)

nArgs = len(sys.argv)
logging.debug("Num args passed: " + str(nArgs))
infile = sys.argv[1]
with open(infile, "r") as file1:
    fileAsList = file1.readlines()

nV = int(fileAsList[0])
nE = len(fileAsList) - 1
print("\nNumber of Vertices: ", nV)
print("Number of Edges: ", nE)

adjList = []
i = 0
while (i <= nV):
    adjList.append([])
    i += 1

i = 1
while(i <= nE):
    splitString = fileAsList[i].split()
    edgeOrigin = int(splitString[0])
    edgeDestination = int(splitString[1])
    weight = int(splitString[2])
    adjList[edgeOrigin].append((edgeDestination, weight))
    i += 1
# print(adjList)

print("\nPrinting the input graph in adjacency list representation...")
i = 1
while(i <= nV):  # iterate through vertices
    for edge in adjList[i]:  # iterate through the edges of each vertex
        print("(", i, "->", edge[0], "):", edge[1], end="\t\t")  # TODO clean up formatting if time permits
    print()
    i += 1
print()

keys = [None]
d = {}
pi = {}
i = 1
while(i <= nV):  # loop performs Initialize_Single_Source()
    d[i] = float('inf')
    keys.append(float('inf'))
    pi[i] = None
    i += 1
d[1] = 0
keys[1] = 0
pi[1] = "Source"

# print("keys: ", keys)
pQ = Heap(keys, nV)
extractionOrder = []  # Lists the vertices in the order they were extracted so that the edges can be printed in the correct order later.

# print("\nd: ", d)
# print("pi: ", pi)
logging.debug("Starting Dijkstra outer loop...")
while (0 < pQ.nDyn):
    # print()
    uID = pQ.min_id()
    extractionOrder.append(uID)
    uValue = pQ.delete_min()
    # pQ.printAandH()
    # print("uID: ", uID, "\t uValue: ", uValue)
    # print("adjList[uid]: ", adjList[uID])
    for edge in adjList[uID]:
        vID = edge[0]
        wUV = edge[1]
        # print("vID: ", vID, "\tw(u,v): ", wUV)
        if (pQ.in_heap(vID)):
            if (d[vID] > d[uID] + wUV):  # Relax(u,v,w):
                d[vID] = d[uID] + wUV
                pi[vID] = uID
                # print("(", uID, ", ", vID, ") : ", d[vID])
            pQ.decrease_key(vID, d[uID] + wUV)  # Update v in Q:
    # pQ.printAandH()
    # print("d: ", d)
    # print("pi: ", pi)

logging.debug("Dijkstra's algorithm complete.")
# print("d: ", d)
# print("pi: ", pi)
logging.info("\tExtraction Order: " + str(extractionOrder))
srcList = list(pi.values())

adjListSSP = {}  # similar to adjList but will only contain the shortest path tree edges
i = 1
while(i <= nV):
    adjListSSP[i] = []
    i += 1

i = 2  # skip 1 because that's the source
while(i <= len(srcList)):
    if (d[i] < float('inf')):  # check to make sure a path was found
        adjListSSP[pi[i]].append((i, d[i]))
    i += 1
# print(adjListSSP)

print("\nFINAL RESULT: SHORTEST PATH TREE EDGES IN ORDER PRODUCED BY DIJKSTRA'S ALGORITHM")
for vertexID in extractionOrder:
    i = vertexID
    if (0 < i) and (d[i] < float('inf')):  # check to make sure a path was found
        for edge in adjListSSP[vertexID]:
            j = edge[0]
            w = edge[1]
            print("(", i, ",\t", j, ") :\t", w)

print("\n\nProgram complete.")
