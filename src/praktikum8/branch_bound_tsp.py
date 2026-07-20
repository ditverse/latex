from dataclasses import dataclass, field
from heapq import heappop, heappush
from math import inf


@dataclass(order=True)
class SearchNode:
    bound: float
    level: int
    current_city: int = field(compare=False)
    path: list[int] = field(compare=False)
    matrix: list[list[float]] = field(compare=False)


def build_cost_matrix(num_nodes, edges):
    matrix = [[inf for _ in range(num_nodes)] for _ in range(num_nodes)]

    for source, target, cost in edges:
        matrix[source][target] = cost
        matrix[target][source] = cost

    return matrix


def copy_matrix(matrix):
    return [row[:] for row in matrix]


def reduce_matrix(matrix):
    reduction_cost = 0
    num_nodes = len(matrix)

    for row in matrix:
        finite_values = [value for value in row if value != inf]
        if not finite_values:
            continue

        minimum = min(finite_values)
        if minimum > 0:
            reduction_cost += minimum
            for col_idx in range(num_nodes):
                if row[col_idx] != inf:
                    row[col_idx] -= minimum

    for col_idx in range(num_nodes):
        finite_values = [
            matrix[row_idx][col_idx]
            for row_idx in range(num_nodes)
            if matrix[row_idx][col_idx] != inf
        ]
        if not finite_values:
            continue

        minimum = min(finite_values)
        if minimum > 0:
            reduction_cost += minimum
            for row_idx in range(num_nodes):
                if matrix[row_idx][col_idx] != inf:
                    matrix[row_idx][col_idx] -= minimum

    return reduction_cost


def path_cost(original_matrix, path):
    total = 0
    for idx in range(1, len(path)):
        total += original_matrix[path[idx - 1]][path[idx]]
    return total


def branch_and_bound_tsp(cost_matrix, start_city=0):
    num_nodes = len(cost_matrix)
    root_matrix = copy_matrix(cost_matrix)
    root_bound = reduce_matrix(root_matrix)

    queue = []
    root = SearchNode(root_bound, 0, start_city, [start_city], root_matrix)
    heappush(queue, root)

    best_cost = inf
    best_path = []
    trace = []
    expanded_nodes = 0
    pruned_nodes = 0

    while queue:
        node = heappop(queue)

        if node.bound >= best_cost:
            pruned_nodes += 1
            trace.append(
                f"Prune path {node.path} karena bound {node.bound} >= best {best_cost}"
            )
            continue

        expanded_nodes += 1
        trace.append(f"Expand path {node.path} dengan bound {node.bound}")

        if node.level == num_nodes - 1:
            if cost_matrix[node.current_city][start_city] == inf:
                continue

            candidate_path = node.path + [start_city]
            candidate_cost = path_cost(cost_matrix, candidate_path)
            trace.append(f"  kandidat tur {candidate_path} cost {candidate_cost}")

            if candidate_cost < best_cost:
                best_cost = candidate_cost
                best_path = candidate_path
                trace.append("  update solusi terbaik")
            continue

        for next_city in range(num_nodes):
            if next_city in node.path:
                continue

            edge_cost = node.matrix[node.current_city][next_city]
            if edge_cost == inf:
                continue

            child_matrix = copy_matrix(node.matrix)

            for city in range(num_nodes):
                child_matrix[node.current_city][city] = inf
                child_matrix[city][next_city] = inf

            child_matrix[next_city][start_city] = inf
            reduction_cost = reduce_matrix(child_matrix)
            child_bound = node.bound + edge_cost + reduction_cost
            child_path = node.path + [next_city]

            if child_bound < best_cost:
                child = SearchNode(
                    child_bound,
                    node.level + 1,
                    next_city,
                    child_path,
                    child_matrix,
                )
                heappush(queue, child)
                trace.append(
                    f"  masukkan path {child_path}, bound {child_bound}"
                )
            else:
                pruned_nodes += 1
                trace.append(
                    f"  prune path {child_path}, bound {child_bound} >= best {best_cost}"
                )

    return {
        "path": best_path,
        "cost": best_cost,
        "expanded_nodes": expanded_nodes,
        "pruned_nodes": pruned_nodes,
        "trace": trace,
    }


def run_case(name, num_nodes, edges, start_city=0):
    cost_matrix = build_cost_matrix(num_nodes, edges)
    result = branch_and_bound_tsp(cost_matrix, start_city)

    print(f"Kasus: {name}")
    print(f"Jumlah simpul: {num_nodes}")
    print(f"Edges berbobot: {edges}")
    print(f"Start: {start_city}")
    print(f"Jalur minimum: {result['path']}")
    print(f"Cost minimum: {result['cost']}")
    print(f"Jumlah simpul diekspansi: {result['expanded_nodes']}")
    print(f"Jumlah simpul dipangkas: {result['pruned_nodes']}")
    print("Trace ringkas:")
    for step in result["trace"][:20]:
        print(step)
    if len(result["trace"]) > 20:
        print("...")
    print()


if __name__ == "__main__":
    # Graf contoh praktikum pada Gambar 8.1.
    praktikum_edges = [
        (0, 1, 12),
        (0, 2, 10),
        (0, 3, 5),
        (1, 2, 9),
        (1, 3, 8),
        (2, 3, 15),
    ]

    # Graf pre test dan post test pada Gambar 8.3.
    pretest_edges = [
        (0, 1, 25),
        (0, 2, 15),
        (0, 3, 20),
        (1, 2, 35),
        (1, 3, 10),
        (2, 3, 30),
    ]

    run_case("Graf praktikum Gambar 8.1", 4, praktikum_edges)
    run_case("Graf pre/post test Gambar 8.3", 4, pretest_edges)
