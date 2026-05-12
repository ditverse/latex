import os
import sys

graphviz_path = r"C:\Program Files\Graphviz\bin"
if graphviz_path not in os.environ.get("PATH", ""):
    os.environ["PATH"] += os.pathsep + graphviz_path

import graphviz

NODE_STYLE = {
    "terminator": {"shape": "oval"},
    "process":    {"shape": "box"},
    "decision":   {"shape": "diamond"},
    "io":         {"shape": "box"},
}

def node(g, name, label, ntype="process"):
    g.node(name, label=label, **NODE_STYLE[ntype])

def edge(g, src, dst, label=""):
    g.edge(src, dst, label=label)

def common_graph(name):
    return graphviz.Digraph(
        name,
        graph_attr={
            "rankdir": "TB",
            "splines": "spline",
            "nodesep": "0.6",
            "ranksep": "0.4",
            "bgcolor": "white",
            "margin": "0",
        },
        node_attr={"margin": "0.1,0.05"},
    )

def buat_flowchart_bfs():
    g = common_graph("bfs")
    node(g, "start", "MULAI", "terminator")
    node(g, "input", "Input: graph, start, n", "io")
    node(g, "init1", "visited = [False] * n\nqueue = deque()\nurutan = []", "process")
    node(g, "init2", "visited[start] = True\nqueue.append(start)", "process")
    
    node(g, "loop", "queue\ntidak kosong?", "decision")
    node(g, "pop", "node = queue.popleft()\nurutan.append(node)", "process")
    node(g, "for_tetangga", "for tetangga in graph[node]", "process")
    node(g, "cek_visit", "visited\n[tetangga]?", "decision")
    node(g, "tambah", "visited[tetangga]=True\nqueue.append(tetangga)", "process")
    
    node(g, "cek_q", "queue\nkosong?", "decision")
    node(g, "cari_j", "cari simpul j\nbelum dikunjungi\nenqueue j", "process")
    
    node(g, "ret", "return urutan", "io")
    node(g, "end", "SELESAI", "terminator")
    
    edge(g, "start", "input")
    edge(g, "input", "init1")
    edge(g, "init1", "init2")
    edge(g, "init2", "loop")
    
    edge(g, "loop", "pop", "Ya")
    edge(g, "loop", "ret", "Tidak")
    
    edge(g, "pop", "for_tetangga")
    edge(g, "for_tetangga", "cek_visit")
    edge(g, "cek_visit", "tambah", "Belum")
    edge(g, "cek_visit", "for_tetangga", "Sudah")
    edge(g, "tambah", "for_tetangga")
    
    # After for loop ends
    edge(g, "for_tetangga", "cek_q", "Selesai")
    edge(g, "cek_q", "cari_j", "Ya")
    edge(g, "cek_q", "loop", "Tidak")
    edge(g, "cari_j", "loop")
    
    edge(g, "ret", "end")
    
    out_dir = os.path.join(os.path.dirname(__file__), "..", "figures", "praktikum6")
    os.makedirs(out_dir, exist_ok=True)
    g.render(os.path.join(out_dir, "flowchart_bfs"), format="png", cleanup=True)

def buat_flowchart_dfs():
    g = common_graph("dfs")
    node(g, "start", "MULAI", "terminator")
    node(g, "input", "Input: graph, start, n", "io")
    node(g, "init", "visited = [False] * n\nurutan = []", "process")
    node(g, "dfs1", "_dfs_rekursif\n(graph, start, visited, urutan)", "process")
    
    node(g, "for_j", "for j in range(n)", "process")
    node(g, "cek_j", "visited[j]?", "decision")
    node(g, "dfs2", "_dfs_rekursif\n(graph, j, visited, urutan)", "process")
    
    node(g, "ret", "return urutan", "io")
    node(g, "end", "SELESAI", "terminator")
    
    edge(g, "start", "input")
    edge(g, "input", "init")
    edge(g, "init", "dfs1")
    edge(g, "dfs1", "for_j")
    
    edge(g, "for_j", "cek_j")
    edge(g, "cek_j", "dfs2", "Belum")
    edge(g, "cek_j", "for_j", "Sudah")
    edge(g, "dfs2", "for_j")
    
    edge(g, "for_j", "ret", "Selesai")
    edge(g, "ret", "end")
    
    # Subgraph for recursive call
    node(g, "rs", "_dfs_rekursif\n(node)", "terminator")
    node(g, "ri", "visited[node]=True\nurutan.append(node)", "process")
    node(g, "rf", "for tetangga\nin graph[node]", "process")
    node(g, "rc", "visited\n[tetangga]?", "decision")
    node(g, "rr", "rekursi ke\ntetangga", "process")
    node(g, "re", "return", "terminator")
    
    edge(g, "rs", "ri")
    edge(g, "ri", "rf")
    edge(g, "rf", "rc")
    edge(g, "rc", "rr", "Belum")
    edge(g, "rc", "rf", "Sudah")
    edge(g, "rr", "rf")
    edge(g, "rf", "re", "Selesai")

    out_dir = os.path.join(os.path.dirname(__file__), "..", "figures", "praktikum6")
    os.makedirs(out_dir, exist_ok=True)
    g.render(os.path.join(out_dir, "flowchart_dfs"), format="png", cleanup=True)

if __name__ == "__main__":
    buat_flowchart_bfs()
    buat_flowchart_dfs()
    print("Selesai generate flowcharts Praktikum 6")
