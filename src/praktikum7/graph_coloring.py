COLOR_NAMES = {
    1: "Merah",
    2: "Hijau",
    3: "Biru",
    4: "Kuning",
}


def build_adjacency(num_nodes, edges):
    graph = {node: [] for node in range(num_nodes)}
    for source, target in edges:
        graph[source].append(target)
        graph[target].append(source)

    for node in graph:
        graph[node].sort()

    return graph


def is_safe(graph, colors, node, color):
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True


def color_graph_backtracking(graph, num_colors, node=0, colors=None, trace=None):
    if colors is None:
        colors = [0] * len(graph)
    if trace is None:
        trace = []

    if node == len(graph):
        return True, colors, trace

    for color in range(1, num_colors + 1):
        trace.append(
            f"Coba node {node} dengan warna {color} ({COLOR_NAMES.get(color, color)})"
        )

        if is_safe(graph, colors, node, color):
            colors[node] = color
            trace.append(f"  diterima: {colors}")

            solved, result, trace = color_graph_backtracking(
                graph, num_colors, node + 1, colors, trace
            )
            if solved:
                return True, result, trace

            trace.append(f"  backtrack dari node {node}")
            colors[node] = 0
        else:
            trace.append("  ditolak: ada tetangga dengan warna sama")

    return False, colors, trace


def format_colors(colors):
    return [COLOR_NAMES.get(color, str(color)) for color in colors]


def run_case(name, num_nodes, edges, num_colors):
    graph = build_adjacency(num_nodes, edges)
    solved, colors, trace = color_graph_backtracking(graph, num_colors)

    print(f"Kasus: {name}")
    print(f"Jumlah simpul: {num_nodes}")
    print(f"Edges: {edges}")
    print(f"Jumlah warna: {num_colors}")

    if solved:
        print(f"Solusi kode warna: {colors}")
        print(f"Solusi nama warna: {format_colors(colors)}")
    else:
        print("Tidak ada solusi pewarnaan yang mungkin.")

    print("Trace:")
    for step in trace:
        print(step)
    print()


if __name__ == "__main__":
    # Graf contoh praktikum pada Gambar 7.4.
    praktikum_edges = [
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 2),
        (1, 3),
        (1, 4),
        (1, 5),
        (2, 3),
        (2, 5),
        (3, 4),
        (4, 5),
    ]

    # Graf pre test dan post test pada Gambar 7.5.
    pretest_edges = [
        (3, 4),
        (3, 0),
        (4, 1),
        (0, 1),
        (0, 2),
        (1, 2),
    ]

    run_case("Graf praktikum Gambar 7.4", 6, praktikum_edges, 4)
    run_case("Graf pre/post test Gambar 7.5", 5, pretest_edges, 3)
