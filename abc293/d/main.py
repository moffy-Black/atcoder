#!/opt/homebrew/bin/python
import sys

class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n
        self.rank = [0] * n
        self.sizes = [1] * n

    def root(self, x):
        if self.parent[x] == -1:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    def is_same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        root_x = self.root(x);root_y = self.root(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] < self.rank[root_y]:
            root_x,root_y = root_y, root_x
        self.parent[root_y] = root_x
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        self.sizes[root_x] += self.sizes[root_y]
        return True

    def size(self, x):
        return self.sizes[self.root(x)]

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N,M = map(int, lines[0].split())
    uf = UnionFind(2*N)
    for i in range(N):
        uf.unite(2*i, 2*i+1)
    merged_num = 0;all_num = 0
    for line in lines[1:]:
        a,b,c,d = line.split();a,c = map(int, (a,c));a,c = a-1,c-1
        if b == "R":
            rope_a = 2*a
        else:
            rope_a = 2*a+1
        if d == "R":
            rope_c = 2*c
        else:
            rope_c = 2*c+1
        union_flag = uf.unite(rope_a, rope_c)
        if not union_flag:
            merged_num+=1
    for i in range(2*N):
        if uf.root(i) == i:
            all_num += 1
    print(f"{merged_num} {all_num-merged_num}")