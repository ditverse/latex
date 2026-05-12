import os
import sys

graphviz_path = r"C:\Program Files\Graphviz\bin"
if graphviz_path not in os.environ.get("PATH", ""):
    os.environ["PATH"] += os.pathsep + graphviz_path

import graphviz

out_dir = os.path.join(os.path.dirname(__file__), "..", "figures", "praktikum6")
os.makedirs(out_dir, exist_ok=True)

def create_digraph(name):
    return graphviz.Digraph(
        name,
        graph_attr={
            "rankdir": "LR",
            "bgcolor": "white",
        },
        node_attr={
            "shape": "circle",
            "style": "solid",
            "fixedsize": "true",
            "width": "0.6",
            "height": "0.6"
        }
    )

def generate_graf_pretest():
    g = create_digraph("graf_pretest")
    # Edges: 0->1, 0->2, 1->3, 2->3, 2->4, 3->5, 4->5, 4->6
    edges = [(0,1), (0,2), (1,3), (2,3), (2,4), (3,5), (4,5), (4,6)]
    for u, v in edges:
        g.edge(str(u), str(v))
    g.render(os.path.join(out_dir, "graf_pretest"), format="png", cleanup=True, view=True)

def generate_graf_praktikum():
    g = create_digraph("graf_praktikum")
    # Edges: 0->1, 0->3, 2->0, 2->3, 2->4, 2->6, 3->1, 4->5, 4->6, 5->2, 6->3
    edges = [(0,1), (0,3), (2,0), (2,3), (2,4), (2,6), (3,1), (4,5), (4,6), (5,2), (6,3)]
    for u, v in edges:
        g.edge(str(u), str(v))
    g.render(os.path.join(out_dir, "graf_praktikum"), format="png", cleanup=True, view=True)

def generate_graf_bfs():
    g = create_digraph("graf_bfs")
    # Order: 0(1), 1(2), 2(4), 3(3), 4(5), 5(7), 6(6)
    labels = {
        0: "0\n(1)",
        1: "1\n(2)",
        2: "2\n(4)",
        3: "3\n(3)",
        4: "4\n(5)",
        5: "5\n(7)",
        6: "6\n(6)"
    }
    for i in range(7):
        g.node(str(i), label=labels[i])
        
    edges = [(0,1), (0,3), (2,0), (2,3), (2,4), (2,6), (3,1), (4,5), (4,6), (5,2), (6,3)]
    for u, v in edges:
        g.edge(str(u), str(v))
    g.render(os.path.join(out_dir, "graf_bfs"), format="png", cleanup=True, view=True)

def generate_graf_dfs():
    g = create_digraph("graf_dfs")
    # Order: 0(1), 1(2), 2(4), 3(3), 4(5), 5(6), 6(7)
    labels = {
        0: "0\n(1)",
        1: "1\n(2)",
        2: "2\n(4)",
        3: "3\n(3)",
        4: "4\n(5)",
        5: "5\n(6)",
        6: "6\n(7)"
    }
    for i in range(7):
        g.node(str(i), label=labels[i])
        
    edges = [(0,1), (0,3), (2,0), (2,3), (2,4), (2,6), (3,1), (4,5), (4,6), (5,2), (6,3)]
    for u, v in edges:
        g.edge(str(u), str(v))
    g.render(os.path.join(out_dir, "graf_dfs"), format="png", cleanup=True, view=True)

if __name__ == "__main__":
    generate_graf_pretest()
    generate_graf_praktikum()
    generate_graf_bfs()
    generate_graf_dfs()
    print("Grafs generated.")
