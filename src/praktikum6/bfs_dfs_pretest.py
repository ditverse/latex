from collections import deque


def bfs(graph, start, n):
    visited = [False] * n
    urutan = []
    queue = deque()

    # tandai simpul awal dan masukkan ke antrian
    visited[start] = True
    queue.append(start)

    while queue:
        node = queue.popleft()
        urutan.append(node)

        # kunjungi tetangga yang belum dikunjungi
        for tetangga in graph[node]:
            if not visited[tetangga]:
                visited[tetangga] = True
                queue.append(tetangga)

        # tangani simpul tidak terjangkau
        if not queue:
            for j in range(n):
                if not visited[j]:
                    visited[j] = True
                    queue.append(j)
                    break

    return urutan


def _dfs_rekursif(graph, node, visited, urutan):
    # tandai dan catat simpul yang dikunjungi
    visited[node] = True
    urutan.append(node)

    # rekursif ke tetangga yang belum dikunjungi
    for tetangga in graph[node]:
        if not visited[tetangga]:
            _dfs_rekursif(graph, tetangga, visited, urutan)


def dfs(graph, start, n):
    visited = [False] * n
    urutan = []

    _dfs_rekursif(graph, start, visited, urutan)

    # tangani simpul yang belum terjangkau
    for j in range(n):
        if not visited[j]:
            _dfs_rekursif(graph, j, visited, urutan)

    return urutan


if __name__ == "__main__":
    # graf pre test Gambar 6.4 (7 simpul, berarah)
    n = 7
    graph_pretest = {
        0: [1, 2],
        1: [3],
        2: [3, 4],
        3: [5],
        4: [5, 6],
        5: [],
        6: [],
    }

    print("Graf Pre Test (Gambar 6.4) - mulai dari node 0")
    print("-" * 45)

    hasil_bfs = bfs(graph_pretest, 0, n)
    print("BFS:", hasil_bfs)

    hasil_dfs = dfs(graph_pretest, 0, n)
    print("DFS:", hasil_dfs)

    print()
    print("Apakah BFS sama dengan jawaban pre test manual?",
          hasil_bfs == [0, 1, 2, 3, 4, 5, 6])
    print("Apakah DFS sama dengan jawaban pre test manual?",
          hasil_dfs == [0, 1, 3, 5, 2, 4, 6])
