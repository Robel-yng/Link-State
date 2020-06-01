#Robel Yemane 170838920
import sys
class LinkState:

    def __init__(self, vertices):
        self.vertices = vertices
        self.GR = []
        self.adjacencyMatrix = []
        self.track = 0
        for p in range(vertices):
            self.adjacencyMatrix.append([-1 for p in range(vertices)])

    # helper function to find the minimum distance for every vertex
    def dijkstra_algo(self, Matrix):

        # this for loop is used to print every forwarding table at each vertex
        for i in range(self.vertices):

            # if the vertex is the gateway router skip that vertex, if it isnt continue
            if i + 1 not in self.GR:

                hop = [-1] * self.vertices
                weight = [1000000] * self.vertices

                # this list checks the parent function will help when we want to calculate the next hop
                next_vertex = []
                weight[i] = 0
                # h = 0
                # from itself is always 0



                # this list will check to see if which vertices have been checked off

                for j in range(self.vertices):
                    next_vertex.append(j)

                # while loop continues until all elements in the next vertex list are used
                while next_vertex:

                    # find the next vertex to find shortest distance
                    z = self.shortest_distance(weight, next_vertex)

                    if z != -1:
                        next_vertex.remove(z)
                    elif z == -1:
                        for t in range(len(next_vertex)):
                            z = next_vertex[t]
                            next_vertex.remove(next_vertex[t])
                            break

                    # finds shortest distance from source which is z
                    for v in range(self.vertices):
                        # this means that if there if -1 doesnt exist then there is an connection
                        if Matrix[z][v] != -1:
                            if Matrix[z][v] and v in next_vertex:
                                #if the weight of the matrix element is lower then element of weight
                                #replace weight elment with new path and the keep track of the hop
                                if weight[z] + Matrix[z][v] < weight[v]:
                                    weight[v] = weight[z] + Matrix[z][v]
                                    hop[v] = z

                # This prints the forwarding table for each vertex once I have finished executing the code above,
                # calculates the minimum distance for each vertex and the index of the vertex is the number of which
                # the vertex so if my index is 0 that is the first vertex and the second index would be second vertex
                print("Forwarding Table for ", i + 1)
                print("{:>10} {:>10} {:>10}".format("To", "Cost", "Next Hop"))
                for edge in range(len(weight)):
                    self.track = 0
                    if edge + 1 in self.GR:
                        # if weight element is styll 1000000 then that means there is no possible way to get to vertex
                        if weight[edge] == 1000000:
                            hop[edge] = -1
                            print("{:>10} {:>10} {:>10}".format(edge + 1, -1, -1))

                        else:
                            # print the gateway router and shortest path
                            print("{:>10} {:>10}".format(edge + 1, weight[edge]), end='')
                            # j = j + 1
                            # find next hop
                            self.next_hop(hop, edge)

#helper function
    def shortest_distance(self, weight, num_vertices):
        vertex_1 = -1
        max_num = 1000000
        # this is used to find the minimum distance of every vertex adjacent to source
        for i in range(len(weight)):
            if i in num_vertices and weight[i] < max_num:
                max_num = weight[i]
                vertex_1 = i
        return vertex_1

    # used recursion to find the next hop for the forwarding tables, helper function
    def next_hop(self, hop, ind):

        # if the hop list has element of -1, it goes back in memory to where it found the last
        if hop[ind] == -1:
            return
        self.next_hop(hop, hop[ind])
        # i used self.track because this will only print the next hop and nothing else
        if self.track == 0:
            print("{:>10}".format(ind + 1))
            self.track = self.track + 1




#This takes care of the file input
first_line = 0
for line in sys.stdin:
    take_of = line.strip()
    # print(stripped)
    if not take_of: break
    first_line = int(take_of)
    break
#I have gotten number of vertices in adjaceny matrix
g = LinkState(first_line)
i = 0
for line in sys.stdin:
    if 0 <= i < first_line:
        # stripped = line.strip()
        take_of = line.split()
        # print(stripped)
        for j in range(first_line):
            # print(stripped)
            g.adjacencyMatrix[i][j] = int(take_of[j])

    elif i == first_line:

        take_of = line.split()

        num_of_gr = len(take_of)
        # print("number of gr: ", num_of_gr)
        for i in range(num_of_gr):
            # print(stripped[i])
            g.GR.append(int(take_of[i]))
        break

    i = i + 1

# print(g.adjacencyMatrix)
# print(g.GR)
g.dijkstra_algo(g.adjacencyMatrix)
