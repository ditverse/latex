from collections import deque


def bfs(graph, start, n):
    visited = [False] * n
    urutan = []
    queue = deque()

    # tandai simpul awal sebagai dikunjungi dan masukkan ke antrian
    visited[start] = True
    queue.append(start)

    while queue:
        # ambil simpul paling depan antrian
        node = queue.popleft()
        urutan.append(node)

        # kunjungi semua tetangga yang belum dikunjungi
        for tetangga in graph[node]:
            if not visited[tetangga]:
                visited[tetangga] = True
                queue.append(tetangga)

        # jika antrian kosong tapi masih ada simpul yang belum dikunjungi
        if not queue:
            for j in range(n):
                if not visited[j]:
                    visited[j] = True
                    queue.append(j)
                    break

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

    hasil = bfs(graph, 0, n)
    print("BFS mulai dari node 0:", hasil)
