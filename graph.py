"""Implement Graph class"""


class Graph:
    """Help on class Graph:

    class Graph(object)
    Graph(verts_num, edges=None, /)
        Creates undirected graph.

        edges is sequence of pairs of integers each represent one edge:
        integers in pair are numbers of vertices incident to edge.
        If edges not given create empty graph(that is without edges) with verts_num
        vertices.

        e.g: Graph(2, [(0, 1)]) creates graph with two vertices and
        an edge between them.
    """

    def __init__(self, verts_num, edges=None):
        self.verts = [[] for _ in range(verts_num)]
        if not edges:
            return
        for v, u in edges:
            self.verts[v].append(u)
            self.verts[u].append(v)

    def __repr__(self):
        res = 'Graph\n'
        for i, vert_i_edges in enumerate(self.verts):
            res += str(i) + '\t:'
            for adjacent in vert_i_edges:
                res += str(adjacent) + ', '
            res += '/\n'
        return res

    def add_edge(self, vert_u, vert_v):
        self.verts[vert_v].append(vert_u)
        self.verts[vert_u].append(vert_v)