
class DynamicLCA:
    def __init__(self, max_nodes):
        import math
        self.LOG = math.ceil(math.log2(max_nodes)) + 1
        self.depth = [0]     # depth[0] = 0 for root
        self.up = [[-1] * self.LOG]  # up[0][k] = -1 for root
        self.n = 1  # current number of nodes

    def parent(self, idx):
        return self.up[idx][0]

    def add_node(self, parent):
        """Add a new node with given parent index."""
        v = self.n
        self.n += 1

        # Extend arrays
        self.depth.append(self.depth[parent] + 1)
        self.up.append([0] * self.LOG)

        # Fill binary lifting table
        self.up[v][0] = parent
        for k in range(1, self.LOG):
            self.up[v][k] = self.up[self.up[v][k-1]][k-1]

        return v  # Return index of the new node

    def lca(self, u, v):
        if self.depth[u] < self.depth[v]:
            u, v = v, u

        # Bring u up to depth of v
        for k in reversed(range(self.LOG)):
            if self.depth[u] - (1 << k) >= self.depth[v]:
                u = self.up[u][k]

        if u == v:
            return u

        # Binary lift both until LCA found
        for k in reversed(range(self.LOG)):
            if self.up[u][k] != self.up[v][k]:
                u = self.up[u][k]
                v = self.up[v][k]

        return self.up[u][0]
    
    def all_edges_in_tree(self):
        res = set()
        for i in range(1, self.n):
            res.add((i, self.up[i][0]))
        return res