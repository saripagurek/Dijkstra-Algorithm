
V = [0,1,2,3]
E = [(0,1), (1,2), (2,3), (3,0)]
print("Vertices:")
print(V)
print("Edges:")
print(E)
startNode = 0
print("Starting Vertex: " + str(startNode))
endNode = 2
print("Final Vertex: " + str(endNode))

dictNeighbours = {}

for vert in V:
    neighbours = []
    for edge in E:
        for i in range(2):
            if edge[i] == vert:
                if i == 0:
                    neighbours.append(edge[1])
                elif i == 1:
                    neighbours.append(edge[0])
    dictNeighbours[vert] = neighbours


def findEdge(currentNode, findV):
    if (findV,currentNode) in E:
        return (findV,currentNode)
    elif (currentNode,findV) in E:
        return (currentNode, findV)
    else:
        return False


posPaths = []
def search(currentNode, path, length):
    if endNode in dictNeighbours[currentNode]:
        path.append(findEdge(currentNode, endNode))
        posPaths.append(path)
        return
    for neighbour in dictNeighbours[currentNode]:
        path.append(findEdge(currentNode, neighbour))
        length = length + 1
        for x in findEdge(currentNode, neighbour):
            if x != currentNode:
                latestNode = x
        if endNode not in findEdge(currentNode, neighbour):
            search(latestNode, path, length)
            path = []
        else:
            return


search(startNode, [], 0)

length = len(posPaths[0])
shortest = posPaths[0]
for i in range(1, len(posPaths)):
    if len(posPaths[i]) < length:
        length = len(posPaths[i])
        shortest = posPaths[i]
print("Shortest Path:")
print(shortest)
print("Length: " + str(length))