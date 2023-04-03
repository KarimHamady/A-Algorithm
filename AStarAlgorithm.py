import heapq

class Node:
    def __init__(self, name, h):
        self.name = name
        self.h = h

    def __lt__ (self, other):
        return self.h < other.h

class Graph:
    def __init__(self) -> None:
        self.dict = {}

    def addNode(self, node):
        self.dict[node] = []

    def addEdge(self, nodeFrom, nodeTo, cost):
        self.dict[nodeFrom].append((nodeTo, cost))
        self.dict[nodeTo].append((nodeFrom, cost))

    def getPath(self, startNode, queueNode, closedSet, fToGoal, path=[]):
        if queueNode[1] == startNode:
            path.reverse()
            return path, fToGoal
        path.append(queueNode[3].name)
        return self.getPath(startNode, closedSet[queueNode[3]], closedSet,  fToGoal, path)

    def aStar(self, start, goal):
        # [(f, node, hFromPrevious, previousNode)]
        pqueue = []
        heapq.heapify(pqueue)
        closedSet = {}
        heapq.heappush(pqueue, (start.h, start, 0, start))
        while pqueue:

            current = heapq.heappop(pqueue)
            print(current, current[1].name)
            for node in pqueue:
                print(node, node[1].name)
            print("")
            if current[1] not in closedSet.keys():
                if not current[1].h:  # if distance to goal = 0
                    return self.getPath(start, current, closedSet, current[0], [current[1].name])
                for child in self.dict[current[1]]:
                    f = child[1] + child[0].h + current[0] - current[1].h
                    heapq.heappush(pqueue, (f, child[0], child[1], current[1]))
                closedSet[current[1]] = current
            
            
def main():

    Graph1 = Graph()

    S = Node("S", 10)
    B = Node("B", 7)
    A = Node("A", 9)
    H = Node("H", 6)
    D = Node("D", 8)
    G = Node("G", 3)
    F = Node("F", 6)
    E = Node("E", 0)
    C = Node("C", 8)
    L = Node("L", 6)
    I = Node("I", 4)
    J = Node("J", 4)
    K = Node("K", 3)

    Graph1.addNode(S)
    Graph1.addNode(B)
    Graph1.addNode(A)
    Graph1.addNode(H)
    Graph1.addNode(D)
    Graph1.addNode(G)
    Graph1.addNode(F)
    Graph1.addNode(E)
    Graph1.addNode(C)
    Graph1.addNode(L)
    Graph1.addNode(I)
    Graph1.addNode(J)
    Graph1.addNode(K)

    Graph1.addEdge(S, B, 2)
    Graph1.addEdge(S, A, 7)
    Graph1.addEdge(A, B, 3)
    Graph1.addEdge(B, D, 4)
    Graph1.addEdge(A, D, 4)
    Graph1.addEdge(B, H, 1)
    Graph1.addEdge(D, F, 5)
    Graph1.addEdge(H, F, 3)
    Graph1.addEdge(H, G, 2)
    Graph1.addEdge(G, E, 2)
    Graph1.addEdge(S, C, 3)
    Graph1.addEdge(C, L, 2)
    Graph1.addEdge(L, I, 4)
    Graph1.addEdge(L, J, 4)
    Graph1.addEdge(I, K, 4)
    Graph1.addEdge(J, K, 4)
    Graph1.addEdge(I, J, 6)
    Graph1.addEdge(K, E, 5)

    print(Graph1.aStar(S, E))


main()
