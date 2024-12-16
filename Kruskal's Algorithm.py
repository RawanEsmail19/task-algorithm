         # Kruskal's Algorithm
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.edges = []  # List to store graph edges

    # Add an edge to the graph
    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))

    # Find set of an element (with path compression)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # Perform union of two sets
    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        # Attach smaller rank tree under root of larger rank tree
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    # Kruskal's algorithm to find MST
    def kruskal_mst(self):
        #  Sort edges by weight
        self.edges.sort()  # Sort by first element of tuples (weight)

        parent = []  # Parent array for union-find
        rank = []  # Rank array for union-find

        # Initialize union-find structures
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        mst = []  # To store the MST edges

        # Step 2: Iterate through edges
        for edge in self.edges:
            weight, u, v = edge
            root_u = self.find(parent, u)
            root_v = self.find(parent, v)

            # If adding this edge doesn't form a cycle
            if root_u != root_v:
                mst.append(edge)
                self.union(parent, rank, root_u, root_v)

        return mst


# Example Usage
if __name__ == "__main__":
    g = Graph(4)  # Create a graph with 4 vertices
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)

    mst = g.kruskal_mst()
    print("Edges in the Minimum Spanning Tree:")
    for weight, u, v in mst:
        print(f"{u} -- {v} == {weight}")
