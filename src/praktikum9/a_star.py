from collections import deque
from heapq import heappop, heappush
from math import inf


def build_graph(num_nodes, edges):
    graph = {node: [] for node in range(num_nodes)}
    for source, target, cost in edges:
        graph[source].append((target, cost))
        graph[target].append((source, cost))

    for node in graph:
        graph[node].sort()

    return graph


def compute_hop_heuristics(graph, target):
    heuristics = {node: inf for node in graph}
    heuristics[target] = 0
    queue = deque([target])

    while queue:
        node = queue.popleft()
        for neighbor, _ in graph[node]:
            if heuristics[neighbor] == inf:
                heuristics[neighbor] = heuristics[node] + 1
                queue.append(neighbor)

    return heuristics


def reconstruct_path(parent, target):
    path = [target]
    while parent[path[-1]] is not None:
        path.append(parent[path[-1]])
    path.reverse()
    return path


def a_star(graph, start, target):
    heuristics = compute_hop_heuristics(graph, target)
    g_score = {node: inf for node in graph}
    parent = {node: None for node in graph}
    visited = set()
    trace = []

    g_score[start] = 0
    queue = []
    heappush(queue, (heuristics[start], 0, start))

    while queue:
        f_score, current_g, node = heappop(queue)

        if node in visited:
            continue

        visited.add(node)
        trace.append(
            f"Expand node {node}: g={current_g}, h={heuristics[node]}, f={f_score}"
        )

        if node == target:
            path = reconstruct_path(parent, target)
            return {
                "path": path,
                "cost": g_score[target],
                "heuristics": heuristics,
                "expanded_nodes": len(visited),
                "trace": trace,
            }

        for neighbor, edge_cost in graph[node]:
            tentative_g = g_score[node] + edge_cost

            if tentative_g < g_score[neighbor]:
                parent[neighbor] = node
                g_score[neighbor] = tentative_g
                new_f = tentative_g + heuristics[neighbor]
                heappush(queue, (new_f, tentative_g, neighbor))
                trace.append(
                    f"  update node {neighbor}: g={tentative_g}, "
                    f"h={heuristics[neighbor]}, f={new_f}, parent={node}"
                )

    return {
        "path": [],
        "cost": inf,
        "heuristics": heuristics,
        "expanded_nodes": len(visited),
        "trace": trace,
    }


def run_case(name, num_nodes, edges, start, target):
    graph = build_graph(num_nodes, edges)
    result = a_star(graph, start, target)

    print(f"Kasus: {name}")
    print(f"Jumlah simpul: {num_nodes}")
    print(f"Edges berbobot: {edges}")
    print(f"Start: {start}")
    print(f"Target: {target}")
    print(f"Heuristik hop ke target: {result['heuristics']}")
    print(f"Jalur terpendek: {result['path']}")
    print(f"Cost minimum: {result['cost']}")
    print(f"Jumlah simpul diekspansi: {result['expanded_nodes']}")
    print("Trace ringkas:")
    for step in result["trace"][:20]:
        print(step)
    if len(result["trace"]) > 20:
        print("...")
    print()


if __name__ == "__main__":
    # Graf contoh praktikum pada Gambar 9.1.
    praktikum_edges = [
        (0, 1, 2),
        (0, 2, 4),
        (0, 4, 5),
        (1, 4, 1),
        (2, 3, 3),
        (3, 4, 3),
        (3, 5, 1),
        (4, 5, 2),
    ]

    # Graf pre test dan post test pada Gambar 9.2.
    pretest_edges = [
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

    run_case("Graf praktikum Gambar 9.1", 6, praktikum_edges, 0, 5)
    run_case("Graf pre/post test Gambar 9.2", 7, pretest_edges, 0, 6)
