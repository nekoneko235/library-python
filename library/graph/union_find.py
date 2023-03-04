class UnionFind():
    # Initialize
    def __init__(self, n):
        # Used to track the sze of each find
        self.sz = [1] * n
        # id[i] points to the ident of i, if id[i] = i then i is a root node
        self.id = [i for i in range(n)]
        # Tracks the number of components in the union find
        self.num_components = n

    # Find which component/set 'p'belongs to, takes amortized constant time
    def find(self, p):
        # Find the root of the component/set
        root = p
        while root != self.id[root]:
            root = self.id[root]

        # Compress the path leading back to the root
        # Doing this operation is called 'path compression'
        # and is what gives us amortized time complexity
        while p != root:
            nxt = self.id[p]
            self.id[p] = root
            p = nxt

        return root

    # Unify the components/sets containing elements 'p' and 'q'
    def unify(self, p, q):
        # These elements are already in the same group
        if self.connected(p, q):
            return

        root1 = self.find(p)
        root2 = self.find(q)

        # merge smaller component/set into the larger one
        if self.sz[root1] < self.sz[root2]:
            self.sz[root2] += self.sz[root1]
            self.id[root1] = root2
        else:
            self.sz[root1] += self.sz[root2]
            self.id[root2] = root1

        self.num_components -= 1

    # Return whether or not the elements 'p' and 'q' are in the same components/set
    def connected(self, p, q):
        return self.find(p) == self.find(q)

    # Return the size of the components/set 'p' belongs to
    def component_size(self, p):
        return self.sz[self.find(p)]

    # Returns the number of remaining components/sets
    def components(self):
        return self.num_components
