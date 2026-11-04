class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Time: O(V + E), Space: O(V)
        n = len(edges) + 1
        # initialize parent to be their own
        par = [i for i in range(n)]
        # initialize rank to all start at depth 1
        rank = [1] * n

        def find(n):
            # return the root parent of node n
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]

        def union(n1, n2):
            # union n1 and n2
            p1, p2 = find(n1), find(n2)
            # immediately return False if they are already connected
            if p1 == p2:
                return False
            # attach the shallower to the longer and increase the rank(size) by added tree
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        # return the first edge that is going to create a cycle
        for n1, n2 in edges:
            # if not union, it is already connexted and adding current edge will create a cycle
            if not union(n1, n2):
                return [n1, n2]

