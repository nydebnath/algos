# Test Graph

from app.graphs import Graph


class TestGraphs:
    def test_graph_initialization(self):
        g = Graph()
        assert g.adj_list == dict()

    def test_graph_add_vertex(self):
        g = Graph()
        assert g.add_vertex("A") == True  # adding for the first time
        assert g.add_vertex("A") == False  # duplicate should throw `False`
        assert g.print_graph() == {"A": []}

    def test_graph_add_edge(self):
        g = Graph()
        assert g.add_edge("A", "B") == False  # Vertices are not present
        # add vertices
        g.add_vertex("A")
        g.add_vertex("B")
        assert g.add_edge("A", "B") == True
        assert g.print_graph() == {"A": ["B"], "B": ["A"]}

    def test_graph_remove_edge(self):
        g = Graph()
        assert g.remove_edge("A", "B") == False  # Vertices are not present
        # add vertices
        g.add_vertex("A")
        g.add_vertex("B")
        # remove edge non-existing edge
        g.remove_edge("A", "B")
        # add edge and then remove it
        assert g.add_edge("A", "B") == True
        g.remove_edge("A", "B")
        assert g.print_graph() == {"A": [], "B": []}

    def test_graph_remove_vertex(self):
        g = Graph()
        assert g.remove_vertex("A") == False  # removing non-existing vertex

        # add vertices
        g.add_vertex("A")
        g.add_vertex("B")
        g.add_vertex("C")
        g.add_vertex("D")
        g.add_vertex("E")
        # add edge
        assert g.add_edge("A", "B") == True
        assert g.add_edge("B", "C") == True
        assert g.add_edge("C", "A") == True
        assert g.add_edge("D", "B")
        assert g.print_graph() == {
            "A": ["B", "C"],
            "B": ["A", "C", "D"],
            "C": ["B", "A"],
            "D": ["B"],
            "E": [],
        }
        # now remove vertex
        assert g.remove_vertex("A")
        assert g.print_graph() == {"B": ["C", "D"], "C": ["B"], "D": ["B"], "E": []}

        # remove vertex which is not connected to any other vertices
        assert g.remove_vertex("E")
        assert g.print_graph() == {"B": ["C", "D"], "C": ["B"], "D": ["B"]}

