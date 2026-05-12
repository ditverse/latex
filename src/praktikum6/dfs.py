def _dfs_rekursif(graph, node, visited, urutan):
    # tandai simpul saat ini sebagai dikunjungi
    visited[node] = True
    urutan.append(node)

    # kunjungi semua tetangga yang belum dikunjungi secara rekursif
    for tetangga in graph[node]:
        if not visited[tetangga]:
            _dfs_rekursif(graph, tetangga, visited, urutan)


def dfs(graph, start, n):
    visited = [False] * n
    urutan = []

    # mulai DFS dari simpul awal
    _dfs_rekursif(graph, start, visited, urutan)

    # tangani simpul yang belum terjangkau
    for j in range(n):
        if not visited[j]:
            _dfs_rekursif(graph, j, visited, urutan)

    return urutan


if __name__ == "__main__":
    # graf berarah Gambar 6.1 sesuai kode tester modul
    n = 7
    graph = {
        0: [1, 3],
        1: [],
        2: [0, 3, 4, 6],
        3: [1],
        4: [5, 6],
        5: [2],
        6: [3],
    }

    hasil = dfs(graph, 0, n)
    print("DFS mulai dari node 0:", hasil)
