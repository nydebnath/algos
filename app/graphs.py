# Graphs and it's operations


class Graph:
    def __init__(self) -> None:
        self.adj_list = (
            {}
        )  # solving graphs using `adjacency list` (other way is using `adjacency matrix`)

    def print_graph(self):
        return self.adj_list

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = list()
            return True
        return False

    def add_edge(self, v1, v2):
        # Connect to vertices - bi-directional
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            vertices = self.adj_list.pop(vertex, "")
            for vertx in vertices:
                self.adj_list[vertx].remove(vertex)
            return True
        return False

