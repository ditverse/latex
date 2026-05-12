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
    "io":         {"shape": "box"}, # As per PDF screenshots, they mostly use simple boxes
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

# ================= Praktikum 3 =================
def buat_flowchart_coin_exchange():
    g = common_graph("coin_exchange")
    node(g, "start", "MULAI", "terminator")
    node(g, "input", "Input: C (himpunan koin), A (nilai target)", "io")
    node(g, "init", "S = {}\nUrutkan C dari nilai terbesar", "process")
    node(g, "loop", "total(S) < A\ndan C != {} ?", "decision")
    
    node(g, "ambil", "x = koin nilai terbesar\nC = C - {x}", "process")
    node(g, "cek_ambil", "total(S) + x <= A ?", "decision")
    node(g, "tambah", "S = S + {x}", "process")
    
    node(g, "cek_hasil", "total(S) == A ?", "decision")
    node(g, "sukses", "return S", "io")
    node(g, "gagal", "tulis: tidak ada solusi", "io")
    node(g, "end", "SELESAI", "terminator")
    
    edge(g, "start", "input")
    edge(g, "input", "init")
    edge(g, "init", "loop")
    
    edge(g, "loop", "ambil", "Ya")
    edge(g, "loop", "cek_hasil", "Tidak")
    
    edge(g, "ambil", "cek_ambil")
    edge(g, "cek_ambil", "tambah", "Ya")
    edge(g, "cek_ambil", "loop", "Tidak")
    edge(g, "tambah", "loop")
    
    edge(g, "cek_hasil", "sukses", "Ya")
    edge(g, "cek_hasil", "gagal", "Tidak")
    
    edge(g, "sukses", "end")
    edge(g, "gagal", "end")

    out_dir = os.path.join(os.path.dirname(__file__), "..", "figures", "praktikum3")
    os.makedirs(out_dir, exist_ok=True)
    g.render(os.path.join(out_dir, "flowchart_coin_exchange"), format="png", cleanup=True)
    print(f"[OK] Praktikum 3: flowchart_coin_exchange.png")

# ================= Praktikum 4 =================
def buat_flowchart_mergesort():
    g = common_graph("merge_sort")
    node(g, "start", "MULAI", "terminator")
    node(g, "input", "Input: A[i..j]", "io")
    node(g, "basis", "i >= j ?", "decision")
    node(g, "ret", "return\n(basis: 1 elemen)", "process")
    
    node(g, "div", "k = (i + j) / 2\n(DIVIDE: titik tengah)", "process")
    node(g, "con_kiri", "MergeSort(A, i, k)\n(CONQUER kiri)", "process")
    node(g, "con_kanan", "MergeSort(A, k+1, j)\n(CONQUER kanan)", "process")
    node(g, "comb", "Merge(A, i, k, j)\n(COMBINE: gabungkan)", "process")
    node(g, "end", "SELESAI", "terminator")
    
    edge(g, "start", "input")
    edge(g, "input", "basis")
    edge(g, "basis", "ret", "Ya")
    edge(g, "ret", "end")
    
    edge(g, "basis", "div", "Tidak")
    edge(g, "div", "con_kiri")
    edge(g, "con_kiri", "con_kanan")
    edge(g, "con_kanan", "comb")
    edge(g, "comb", "end")
    
    out_dir = os.path.join(os.path.dirname(__file__), "..", "figures", "praktikum4")
    os.makedirs(out_dir, exist_ok=True)
    g.render(os.path.join(out_dir, "flowchart_mergesort"), format="png", cleanup=True)
    print(f"[OK] Praktikum 4: flowchart_mergesort.png")

def buat_flowchart_quicksort():
    g = common_graph("quick_sort")
    node(g, "start", "MULAI", "terminator")
    node(g, "input", "Input: A[i..j]", "io")
    node(g, "basis", "i >= j ?", "decision")
    node(g, "ret", "return", "process")
    
    node(g, "part", "k = Partisi(A, i, j)\npivot = A[(i+j)/2]", "process")
    node(g, "con_kiri", "QuickSort(A, i, k)", "process")
    node(g, "con_kanan", "QuickSort(A, k+1, j)", "process")
    node(g, "end", "SELESAI", "terminator")
    
    edge(g, "start", "input")
    edge(g, "input", "basis")
    edge(g, "basis", "ret", "Ya")
    edge(g, "ret", "end")
    
    edge(g, "basis", "part", "Tidak")
    edge(g, "part", "con_kiri")
    edge(g, "con_kiri", "con_kanan")
    edge(g, "con_kanan", "end")
    
    out_dir = os.path.join(os.path.dirname(__file__), "..", "figures", "praktikum4")
    os.makedirs(out_dir, exist_ok=True)
    g.render(os.path.join(out_dir, "flowchart_quicksort"), format="png", cleanup=True)
    print(f"[OK] Praktikum 4: flowchart_quicksort.png")

# ================= Praktikum 5 =================
def buat_flowchart_selection_dc():
    g = common_graph("selection_sort_dc")
    node(g, "start", "MULAI", "terminator")
    node(g, "input", "Input: A[i..j]", "io")
    node(g, "basis", "i >= j ?", "decision")
    node(g, "ret", "return\n(basis: ukuran <= 1)", "process")
    
    node(g, "bagi", "Bagi(A, i, j)\n(cari min A[i..j], tukar ke A[i])", "process")
    node(g, "conq", "SelectionSort(A, i+1, j)\n(Conquer: subproblem lebih kecil)", "process")
    node(g, "end", "SELESAI", "terminator")
    
    edge(g, "start", "input")
    edge(g, "input", "basis")
    edge(g, "basis", "ret", "Ya")
    edge(g, "ret", "end")
    
    edge(g, "basis", "bagi", "Tidak")
    edge(g, "bagi", "conq")
    edge(g, "conq", "end")
    
    out_dir = os.path.join(os.path.dirname(__file__), "..", "figures", "praktikum5")
    os.makedirs(out_dir, exist_ok=True)
    g.render(os.path.join(out_dir, "flowchart_selection_sort_dc"), format="png", cleanup=True)
    print(f"[OK] Praktikum 5: flowchart_selection_sort_dc.png")


if __name__ == "__main__":
    buat_flowchart_coin_exchange()
    buat_flowchart_mergesort()
    buat_flowchart_quicksort()
    buat_flowchart_selection_dc()
    print("Selesai men-generate flowchart.")
