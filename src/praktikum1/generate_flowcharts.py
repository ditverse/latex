# ============================================================
# Generate Flowcharts - Praktikum 1
# Menghasilkan flowchart untuk Selection Sort & Insertion Sort
# Output : figures/praktikum1/flowchart_selection_sort.png
#          figures/praktikum1/flowchart_insertion_sort.png
# ============================================================

import os
import sys

# Tambahkan path Graphviz ke PATH (untuk Windows)
graphviz_path = r"C:\Program Files\Graphviz\bin"
if graphviz_path not in os.environ.get("PATH", ""):
    os.environ["PATH"] += os.pathsep + graphviz_path

try:
    import graphviz
except ImportError:
    print("ERROR: Package 'graphviz' belum terinstall.")
    print("Jalankan: pip install graphviz")
    sys.exit(1)

# ============================================================
# Konfigurasi Output
# ============================================================
OUTPUT_DIR = os.path.join(
    os.path.dirname(__file__), "..", "..", "figures", "praktikum1"
)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Style default node (Default Styling)
NODE_STYLE = {
    "terminator": {"shape": "oval"},
    "process":    {"shape": "box"},
    "decision":   {"shape": "diamond"},
    "io":         {"shape": "parallelogram"},
}

def node(g, name, label, ntype="process"):
    g.node(name, label=label, **NODE_STYLE[ntype])

def edge(g, src, dst, label=""):
    g.edge(src, dst, label=label)



# ============================================================
# FLOWCHART 1: Selection Sort
# ============================================================
def buat_flowchart_selection_sort():
    g = graphviz.Digraph(
        "selection_sort",
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

    # --- Mulai ---
    node(g, "start",    "MULAI",                        "terminator")
    node(g, "input",    "Input: array arr[0..n-1]",     "io")
    node(g, "init_i",  "i = 0",                         "process")

    # --- Loop luar ---
    node(g, "cek_i",   "i < n - 1 ?",                  "decision")
    node(g, "min_idx", "min_idx = i",                   "process")
    node(g, "init_j",  "j = i + 1",                    "process")

    # --- Loop dalam ---
    node(g, "cek_j",   "j < n ?",                      "decision")
    node(g, "cek_min", "arr[j] < arr[min_idx] ?",      "decision")
    node(g, "upd_min", "min_idx = j",                  "process")
    node(g, "inc_j",   "j = j + 1",                    "process")

    # --- Tukar ---
    node(g, "cek_swap", "min_idx != i ?",              "decision")
    node(g, "swap",    "Tukar arr[i] dan arr[min_idx]","process")
    node(g, "inc_i",   "i = i + 1",                    "process")

    # --- Selesai ---
    node(g, "output",  "Output: arr terurut",           "io")
    node(g, "end",     "SELESAI",                       "terminator")

    # --- Edges ---
    edge(g, "start",    "input")
    edge(g, "input",    "init_i")
    edge(g, "init_i",  "cek_i")

    edge(g, "cek_i",   "min_idx",  "Ya")
    edge(g, "cek_i",   "output",   "Tidak")

    edge(g, "min_idx", "init_j")
    edge(g, "init_j",  "cek_j")

    edge(g, "cek_j",   "cek_min",  "Ya")
    edge(g, "cek_j",   "cek_swap", "Tidak")

    edge(g, "cek_min", "upd_min",  "Ya")
    edge(g, "cek_min", "inc_j",    "Tidak")
    edge(g, "upd_min", "inc_j")
    edge(g, "inc_j",   "cek_j")

    edge(g, "cek_swap", "swap",    "Ya")
    edge(g, "cek_swap", "inc_i",   "Tidak")
    edge(g, "swap",    "inc_i")
    edge(g, "inc_i",   "cek_i")

    edge(g, "output",  "end")

    # Render
    out_path = os.path.join(OUTPUT_DIR, "flowchart_selection_sort")
    g.render(out_path, format="png", cleanup=True)
    print(f"[OK] Flowchart Selection Sort -> {out_path}.png")


# ============================================================
# FLOWCHART 2: Insertion Sort
# ============================================================
def buat_flowchart_insertion_sort():
    g = graphviz.Digraph(
        "insertion_sort",
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

    # --- Mulai ---
    node(g, "start",   "MULAI",                             "terminator")
    node(g, "input",   "Input: array arr[0..n-1]",          "io")
    node(g, "init_i",  "i = 1",                             "process")

    # --- Loop luar ---
    node(g, "cek_i",   "i < n ?",                           "decision")
    node(g, "set_key", "key = arr[i]\nj = i - 1",           "process")

    # --- Loop dalam ---
    node(g, "cek_j",   "j >= 0 AND\narr[j] > key ?",        "decision")
    node(g, "geser",   "arr[j+1] = arr[j]\nj = j - 1",      "process")

    # --- Sisipkan ---
    node(g, "sisip",   "arr[j+1] = key",                    "process")
    node(g, "inc_i",   "i = i + 1",                         "process")

    # --- Selesai ---
    node(g, "output",  "Output: arr terurut",                "io")
    node(g, "end",     "SELESAI",                            "terminator")

    # --- Edges ---
    edge(g, "start",   "input")
    edge(g, "input",   "init_i")
    edge(g, "init_i",  "cek_i")

    edge(g, "cek_i",   "set_key", "Ya")
    edge(g, "cek_i",   "output",  "Tidak")

    edge(g, "set_key", "cek_j")

    edge(g, "cek_j",   "geser",   "Ya")
    edge(g, "cek_j",   "sisip",   "Tidak")
    edge(g, "geser",   "cek_j")

    edge(g, "sisip",   "inc_i")
    edge(g, "inc_i",   "cek_i")

    edge(g, "output",  "end")

    # Render
    out_path = os.path.join(OUTPUT_DIR, "flowchart_insertion_sort")
    g.render(out_path, format="png", cleanup=True)
    print(f"[OK] Flowchart Insertion Sort -> {out_path}.png")


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    print("=" * 55)
    print("  Generate Flowcharts - Praktikum 1")
    print("=" * 55)

    buat_flowchart_selection_sort()
    buat_flowchart_insertion_sort()

    print()
    print("Semua flowchart berhasil dibuat di:")
    print(f"  {os.path.abspath(OUTPUT_DIR)}")
