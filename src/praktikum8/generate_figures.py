import os

graphviz_path = r"C:\Program Files\Graphviz\bin"
if graphviz_path not in os.environ.get("PATH", ""):
    os.environ["PATH"] += os.pathsep + graphviz_path

import graphviz


OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "figures", "praktikum8")


def ensure_output_dir():
    os.makedirs(OUT_DIR, exist_ok=True)


def save_png(graph, filename):
    output_path = os.path.join(OUT_DIR, filename)
    with open(output_path, "wb") as output_file:
        output_file.write(graph.pipe(format="png"))


def create_tsp_graph(name, solution_edges=None):
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
        0: "1,2!",
        1: "0,0!",
        2: "2,0!",
        3: "1,1!",
    }

    for node, pos in positions.items():
        graph.node(str(node), label=str(node), pos=pos)

    edges = [
        (0, 1, 25),
        (0, 2, 15),
        (0, 3, 20),
        (1, 2, 35),
        (1, 3, 10),
        (2, 3, 30),
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
        "flowchart_branch_bound_tsp",
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
    graph.node("input", "Input: cost matrix,\nstart city", shape="box")
    graph.node("reduce", "Reduksi matrix awal\nhitung bound akar", shape="box")
    graph.node("queue", "Masukkan node akar\nke priority queue", shape="box")
    graph.node("empty", "queue kosong?", shape="diamond")
    graph.node("pop", "Ambil node dengan\nbound terkecil", shape="box")
    graph.node("bound", "bound >= best?", shape="diamond")
    graph.node("leaf", "semua kota\nsudah dikunjungi?", shape="diamond")
    graph.node("tour", "tutup tur ke start\nhitung cost aktual", shape="box")
    graph.node("best", "cost < best?", shape="diamond")
    graph.node("update", "update best path\nbest cost", shape="box")
    graph.node("child", "Bangkitkan anak:\nset baris/kolom inf", shape="box")
    graph.node("childreduce", "Reduksi matrix anak\nhitung child bound", shape="box")
    graph.node("push", "Masukkan anak\njika bound layak", shape="box")
    graph.node("result", "Output best path\nbest cost", shape="box")
    graph.node("end", "SELESAI", shape="oval")

    graph.edge("start", "input")
    graph.edge("input", "reduce")
    graph.edge("reduce", "queue")
    graph.edge("queue", "empty")
    graph.edge("empty", "result", label="Ya")
    graph.edge("empty", "pop", label="Tidak")
    graph.edge("pop", "bound")
    graph.edge("bound", "empty", label="Ya")
    graph.edge("bound", "leaf", label="Tidak")
    graph.edge("leaf", "tour", label="Ya")
    graph.edge("tour", "best")
    graph.edge("best", "update", label="Ya")
    graph.edge("best", "empty", label="Tidak")
    graph.edge("update", "empty")
    graph.edge("leaf", "child", label="Tidak")
    graph.edge("child", "childreduce")
    graph.edge("childreduce", "push")
    graph.edge("push", "empty")
    graph.edge("result", "end")

    return graph


if __name__ == "__main__":
    ensure_output_dir()

    save_png(create_tsp_graph("graf_pretest_83"), "graf_pretest_83.png")
    save_png(
        create_tsp_graph(
            "graf_pretest_83_solusi",
            solution_edges=[(0, 2), (2, 1), (1, 3), (3, 0)],
        ),
        "graf_pretest_83_solusi.png",
    )
    save_png(create_flowchart(), "flowchart_branch_bound_tsp.png")

    print("Gambar praktikum 8 berhasil dibuat.")
