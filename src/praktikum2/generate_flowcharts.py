# ============================================================
# Generate Flowcharts - Praktikum 2
# Menghasilkan flowchart untuk Pencarian Terbesar & Uji Prima
# Output : figures/praktikum2/flowchart_pencarian_terbesar.png
#          figures/praktikum2/flowchart_uji_prima.png
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
    os.path.dirname(__file__), "..", "..", "figures", "praktikum2"
)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Style default node (Sesuai modifikasi Praktikum 1)
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
# FLOWCHART 1: Pencarian Elemen Terbesar
# ============================================================
def buat_flowchart_pencarian_terbesar():
    g = graphviz.Digraph(
        "pencarian_terbesar",
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
    node(g, "input",    "Input: arr[0..n-1]",           "io")
    node(g, "init_max", "maks = arr[0]\ni = 1",         "process")

    # --- Loop ---
    node(g, "cek_i",    "i < n ?",                      "decision")
    
    # --- Kondisi ---
    node(g, "cek_maks", "arr[i] > maks ?",              "decision")
    node(g, "upd_maks", "maks = arr[i]",                "process")
    node(g, "inc_i",    "i = i + 1",                    "process")

    # --- Selesai ---
    node(g, "output",   "Output: maks",                 "io")
    node(g, "end",      "SELESAI",                      "terminator")

    # --- Edges ---
    edge(g, "start",    "input")
    edge(g, "input",    "init_max")
    edge(g, "init_max", "cek_i")

    edge(g, "cek_i",    "cek_maks",  "Ya")
    edge(g, "cek_i",    "output",    "Tidak")

    edge(g, "cek_maks", "upd_maks",  "Ya")
    edge(g, "cek_maks", "inc_i",     "Tidak")
    
    edge(g, "upd_maks", "inc_i")
    edge(g, "inc_i",    "cek_i")

    edge(g, "output",   "end")

    # Render
    out_path = os.path.join(OUTPUT_DIR, "flowchart_pencarian_terbesar")
    g.render(out_path, format="png", cleanup=True)
    print(f"[OK] Flowchart Pencarian Terbesar -> {out_path}.png")


# ============================================================
# FLOWCHART 2: Uji Bilangan Prima
# ============================================================
def buat_flowchart_uji_prima():
    g = graphviz.Digraph(
        "uji_prima",
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
    node(g, "input",    "Input: bilangan n",            "io")
    
    # --- Cek Dasar ---
    node(g, "cek_n",    "n <= 1 ?",                     "decision")
    node(g, "out_f1",   "Output: Bukan Prima",          "io")
    
    node(g, "init_i",   "i = 2",                        "process")

    # --- Loop ---
    node(g, "cek_i",    "i < n ?",                      "decision")
    
    # --- Kondisi Modulus ---
    node(g, "cek_mod",  "n mod i == 0 ?",               "decision")
    node(g, "out_f2",   "Output: Bukan Prima",          "io")
    node(g, "inc_i",    "i = i + 1",                    "process")

    # --- Selesai ---
    node(g, "out_t",    "Output: Prima",                "io")
    node(g, "end",      "SELESAI",                      "terminator")

    # --- Edges ---
    edge(g, "start",    "input")
    edge(g, "input",    "cek_n")
    
    edge(g, "cek_n",    "out_f1",   "Ya")
    edge(g, "cek_n",    "init_i",   "Tidak")
    
    edge(g, "out_f1",   "end")

    edge(g, "init_i",   "cek_i")
    
    edge(g, "cek_i",    "cek_mod",  "Ya")
    edge(g, "cek_i",    "out_t",    "Tidak")

    edge(g, "cek_mod",  "out_f2",   "Ya")
    edge(g, "cek_mod",  "inc_i",    "Tidak")
    
    edge(g, "out_f2",   "end")
    edge(g, "out_t",    "end")
    
    edge(g, "inc_i",    "cek_i")

    # Render
    out_path = os.path.join(OUTPUT_DIR, "flowchart_uji_prima")
    g.render(out_path, format="png", cleanup=True)
    print(f"[OK] Flowchart Uji Bilangan Prima -> {out_path}.png")


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    print("=" * 55)
    print("  Generate Flowcharts - Praktikum 2")
    print("=" * 55)

    buat_flowchart_pencarian_terbesar()
    buat_flowchart_uji_prima()

    print()
    print("Semua flowchart berhasil dibuat di:")
    print(f"  {os.path.abspath(OUTPUT_DIR)}")
