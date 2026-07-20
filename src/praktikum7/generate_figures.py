import os

graphviz_path = r"C:\Program Files\Graphviz\bin"
if graphviz_path not in os.environ.get("PATH", ""):
    os.environ["PATH"] += os.pathsep + graphviz_path

import graphviz


OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "figures", "praktikum7")

COLOR_TABLE = {
    1: ("#e74c3c", "Merah"),
    2: ("#2ecc71", "Hijau"),
    3: ("#3498db", "Biru"),
    4: ("#f1c40f", "Kuning"),
}


def ensure_output_dir():
    os.makedirs(OUT_DIR, exist_ok=True)


def save_png(graph, filename):
    output_path = os.path.join(OUT_DIR, filename)
    with open(output_path, "wb") as output_file:
        output_file.write(graph.pipe(format="png"))


def create_graph(name, colored=False, colors=None):
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
            "style": "filled" if colored else "solid",
            "fixedsize": "true",
            "width": "0.55",
            "height": "0.55",
            "fontname": "Times New Roman",
        },
        edge_attr={
            "color": "#222222",
            "penwidth": "1.5",
        },
    )

    positions = {
        0: "0,1!",
        1: "2,1!",
        2: "1,0!",
        3: "0,2!",
        4: "2,2!",
    }

    for node, pos in positions.items():
        attrs = {"pos": pos}
        if colored and colors is not None:
            color_hex, _ = COLOR_TABLE[colors[node]]
            attrs.update({"fillcolor": color_hex, "fontcolor": "white"})
        else:
            attrs.update({"fillcolor": "white"})
        graph.node(str(node), label=str(node), **attrs)

    edges = [(3, 4), (3, 0), (4, 1), (0, 1), (0, 2), (1, 2)]
    for source, target in edges:
        graph.edge(str(source), str(target))

    return graph


def create_flowchart():
    graph = graphviz.Digraph(
        "flowchart_backtracking",
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
    graph.node("input", "Input: graph,\njumlah warna", shape="box")
    graph.node("init", "colors = [0] * n\nnode = 0", shape="box")
    graph.node("all", "semua node\nsudah diwarnai?", shape="diamond")
    graph.node("try", "coba warna\n1 sampai m", shape="box")
    graph.node("safe", "warna aman\nuntuk node?", shape="diamond")
    graph.node("assign", "colors[node] = warna", shape="box")
    graph.node("next", "rekursi ke\nnode berikutnya", shape="box")
    graph.node("solved", "solusi\nditemukan?", shape="diamond")
    graph.node("remove", "hapus warna\n(backtrack)", shape="box")
    graph.node("more", "masih ada\nwarna lain?", shape="diamond")
    graph.node("fail", "return false", shape="box")
    graph.node("success", "return true", shape="box")
    graph.node("end", "SELESAI", shape="oval")

    graph.edge("start", "input")
    graph.edge("input", "init")
    graph.edge("init", "all")
    graph.edge("all", "success", label="Ya")
    graph.edge("all", "try", label="Tidak")
    graph.edge("try", "safe")
    graph.edge("safe", "assign", label="Ya")
    graph.edge("safe", "more", label="Tidak")
    graph.edge("assign", "next")
    graph.edge("next", "solved")
    graph.edge("solved", "success", label="Ya")
    graph.edge("solved", "remove", label="Tidak")
    graph.edge("remove", "more")
    graph.edge("more", "try", label="Ya")
    graph.edge("more", "fail", label="Tidak")
    graph.edge("success", "end")
    graph.edge("fail", "end")

    return graph


if __name__ == "__main__":
    ensure_output_dir()

    save_png(create_graph("graf_pretest_75"), "graf_pretest_75.png")
    save_png(
        create_graph("graf_pretest_75_berwarna", colored=True, colors=[1, 2, 3, 2, 1]),
        "graf_pretest_75_berwarna.png",
    )
    save_png(create_flowchart(), "flowchart_backtracking.png")

    print("Gambar praktikum 7 berhasil dibuat.")
