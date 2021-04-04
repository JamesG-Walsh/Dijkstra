from heap import heap
import logging
logging.basicConfig(level=logging.DEBUG)

infile = "infile.txt"  # TODO make this dynamic with a script
with open(infile, "r") as file1:
    fileAsList = file1.readlines()

nV = int(fileAsList[0])

nE = len(fileAsList) - 1

logging.info("Number of Vertices: %d", nV)
logging.info("Number of Edges: %d", nE)

adjList = []
i = 0
while (i <= nV):
    adjList.append([])
    i += 1

# adjList[1].append(1)
# adjList[24].append(24)
logging.debug(adjList)

i = 1
while(i <= nE):
    # logging.debug(i)
    splitString = fileAsList[i].split()
    # logging.debug(splitString)
    edgeOrigin = int(splitString[0])
    edgeDestination = int(splitString[1])
    weight = int(splitString[2])
    adjList[edgeOrigin].append((edgeDestination, weight))
    i += 1

logging.debug(adjList)

print("Printing the input graph in adjacency list representation...")
i = 1
while(i <= nV): # iterate through vertices
    for edge in adjList[i]: #iterate through the edges of each vertex
        print("(", i, "->", edge[0], "):", edge[1], end="\t\t")
    print()
    i += 1