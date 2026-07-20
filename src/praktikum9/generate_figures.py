import os

graphviz_path = r"C:\Program Files\Graphviz\bin"
if graphviz_path not in os.environ.get("PATH", ""):
    os.environ["PATH"] += os.pathsep + graphviz_path

import graphviz


OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "figures", "praktikum9")


def ensure_output_dir():
    os.makedirs(OUT_DIR, exist_ok=True)


def save_png(graph, filename):
    output_path = os.path.join(OUT_DIR, filename)
    with open(output_path, "wb") as output_file:
        output_file.write(graph.pipe(format="png"))


def create_astar_graph(name, solution_edges=None):
    graph = graphviz.Graph(
        name,
        graph_attr={
            "bgcolor": "white",
            "layout": "neato",
            "splines": "line",
            "overlap": "false",
            "outputorder": "edgesfirst",
        },
        node_attr={
            "shape": "circle",
            "style": "filled",
            "fixedsize": "true",
            "width": "0.55",
            "height": "0.55",
            "fillcolor": "#111111",
            "fontcolor": "white",
            "fontname": "Times New Roman",
        },
        edge_attr={
            "fontname": "Times New Roman",
            "fontsize": "12",
            "color": "#222222",
            "penwidth": "1.5",
        },
    )

    positions = {
        0: "0,2!",
        1: "3,2!",
        2: "0,1!",
        3: "3,1!",
        4: "1.5,0.45!",
        5: "0,-0.7!",
        6: "3,-0.7!",
    }

    for node, pos in positions.items():
        graph.node(str(node), label=str(node), pos=pos)

    edges = [
        (0, 1, 3),
        (0, 2, 4),
        (0, 3, 5),
        (1, 3, 2),
        (2, 4, 4),
        (3, 4, 2),
        (4, 5, 1),
        (4, 6, 5),
        (5, 6, 3),
    ]

    normalized_solution = set()
    if solution_edges is not None:
        normalized_solution = {tuple(sorted(edge)) for edge in solution_edges}

    for source, target, cost in edges:
        edge_key = tuple(sorted((source, target)))
        attrs = {"label": str(cost)}
        if edge_key in normalized_solution:
            attrs.update({"color": "#d81b60", "penwidth": "3.0"})
        graph.edge(str(source), str(target), **attrs)

    return graph


def create_flowchart():
    graph = graphviz.Digraph(
        "flowchart_astar",
        graph_attr={
            "rankdir": "TB",
            "splines": "spline",
            "nodesep": "0.55",
            "ranksep": "0.45",
            "bgcolor": "white",
        },
        node_attr={"fontname": "Times New Roman", "margin": "0.1,0.06"},
    )

    graph.node("start", "MULAI", shape="oval")
    graph.node("input", "Input: graph,\nstart, target", shape="box")
    graph.node("heuristic", "Hitung h(n):\njumlah busur minimum\nke target", shape="box")
    graph.node("init", "g(start)=0\nopen set = start", shape="box")
    graph.node("empty", "open set\nkosong?", shape="diamond")
    graph.node("pop", "Ambil node dengan\nf(n) terkecil", shape="box")
    graph.node("goal", "node == target?", shape="diamond")
    graph.node("neighbor", "Periksa semua\ntetangga node", shape="box")
    graph.node("better", "g baru lebih kecil?", shape="diamond")
    graph.node("update", "Update parent,\ng(n), f(n)=g+h", shape="box")
    graph.node("push", "Masukkan ke\nopen set", shape="box")
    graph.node("path", "Rekonstruksi jalur\nterpendek", shape="box")
    graph.node("fail", "Tidak ada jalur", shape="box")
    graph.node("end", "SELESAI", shape="oval")

    graph.edge("start", "input")
    graph.edge("input", "heuristic")
    graph.edge("heuristic", "init")
    graph.edge("init", "empty")
    graph.edge("empty", "fail", label="Ya")
    graph.edge("empty", "pop", label="Tidak")
    graph.edge("pop", "goal")
    graph.edge("goal", "path", label="Ya")
    graph.edge("goal", "neighbor", label="Tidak")
    graph.edge("neighbor", "better")
    graph.edge("better", "update", label="Ya")
    graph.edge("better", "empty", label="Tidak")
    graph.edge("update", "push")
    graph.edge("push", "empty")
    graph.edge("path", "end")
    graph.edge("fail", "end")

    return graph


if __name__ == "__main__":
    ensure_output_dir()

    save_png(create_astar_graph("graf_pretest_92"), "graf_pretest_92.png")
    save_png(
        create_astar_graph(
            "graf_pretest_92_solusi",
            solution_edges=[(0, 3), (3, 4), (4, 5), (5, 6)],
        ),
        "graf_pretest_92_solusi.png",
    )
    save_png(create_flowchart(), "flowchart_astar.png")

    print("Gambar praktikum 9 berhasil dibuat.")
