class ufds:
    parent_node = {}
    rank = {}

    def make_set(self, u):
        for i in u:
            self.parent_node[i] = i
            self.rank[i] = 0

    def op_find(self, k):
        if self.parent_node[k] != k:
            self.parent_node[k] = self.op_find(self.parent_node[k])
        return self.parent_node[k]

    def op_union(self, a, b):
        x = self.op_find(a)
        y = self.op_find(b)

        if x==y:
            return
        
        if self.rank[x] > self.rank[y]:
            self.parent_node[y] = x
        elif self.rank[x] < self.rank[y]:
            self.parent_node[x] = y
        else:
            self.parent_node[x] = y
            self.rank[y] += 1

def display(u, data):
    print([data.op_find(i) for i in u])

if __name__ == "__main__":
    u = [1, 3, 5, 7]
    data = ufds()
    data.make_set(u)
    print("\nSet is: ")
    display(u, data)
    data.op_union(1, 5)
    print("\nSet is: ")
    display(u, data)
    data.op_union(1, 7)
    print("\nSet is: ")
    display(u, data)