class Graph:

    def __init__(self):
        self.Nodes = {}
        self.Edges = []

    def nodes(self):
        '''Return a list of all of the nodes in the graph.'''
        return self.Nodes.keys()

    def edges(self):
        '''Return a list of all of the edges in the graph.'''
        return self.Edges

    def add_node(self, n):
        '''Add node 'n' to the graph.'''
        self.Nodes.setdefault(n, set([]))

    def add_edge(self, n1, n2):
        '''Add an edge to the graph that connects 'n1' and 'n2'.'''
        edge = set((n1, n2))

        if edge not in self.Edges:
            # add n1 and n2 to the graph if they are non-existent
            self.add_node(n1)
            self.add_node(n2)

            self.Nodes[n1].add(n2)
            self.Nodes[n2].add(n1)
            self.Edges.append(edge)

    def del_node(self, n):
        '''Delete node 'n' from the graph.'''
        try:
            del self.Nodes[n]
            edges = []

            for k in self.Nodes.iterkeys():
                try:
                    self.Nodes[k].remove(n)
                    edges.append(set((n, k)))

                except KeyError:
                    continue

            # self.Edges.difference(edges)
            self.Edges = [e for e in self.Edges if e not in edges]

        except KeyError:
            raise ValueError('Can\'t delete non-existent nodes.''')

    def del_edge(self, n1, n2):
        '''Delete the edge connecting 'n1' and 'n2'.'''
        try:
            self.Edges.remove(set((n1, n2)))

        except KeyError:
            raise ValueError('Can\'t delete non-existent edges.''')

    def has_node(self, n):
        '''Return True if node 'n' is in the graph; otherwise, False.'''
        return n in self.Nodes

    def neighbors(self, n):
        '''Return all of the nodes connected via edges to node 'n'.'''
        try:
            return list(self.Nodes[n])

        except KeyError:
            raise ValueError('Non-existent nodes have no neighbors.')

    def is_adjacent(self, n1, n2):
        '''Return True if an edge connects 'n1' and 'n2'; otherwise, False.'''
        try:
            return n1 in self.Nodes[n2]

        except KeyError:
            raise ValueError('Either n1 or n2 is non-existent.')
