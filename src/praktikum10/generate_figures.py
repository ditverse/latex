from pathlib import Path

from graphviz import Digraph


ROOT = Path(__file__).resolve().parents[2]
FIGURE_DIR = ROOT / "figures" / "praktikum10"
FIGURE_DIR.mkdir(parents=True, exist_ok=True)

TEXT = "abacaabacabacababa"
PATTERN = "acabaca"
MATCH_INDEX = 7


def save_png(graph, filename):
    output_path = FIGURE_DIR / filename
    output_path.write_bytes(graph.pipe(format="png"))


def matching_table(label, compare_direction):
    rows = ["<TR>"]
    for index, char in enumerate(TEXT):
        color = "#DDEBFF" if MATCH_INDEX <= index < MATCH_INDEX + len(PATTERN) else "#FFFFFF"
        rows.append(f'<TD BGCOLOR="{color}"><FONT POINT-SIZE="10">{char}</FONT></TD>')
    rows.append("</TR><TR>")
    for index in range(len(TEXT)):
        if MATCH_INDEX <= index < MATCH_INDEX + len(PATTERN):
            char = PATTERN[index - MATCH_INDEX]
            rows.append(f'<TD BGCOLOR="#E6F4EA"><FONT POINT-SIZE="10">{char}</FONT></TD>')
        else:
            rows.append('<TD BGCOLOR="#F8F8F8"><FONT POINT-SIZE="10"> </FONT></TD>')
    rows.append("</TR>")

    return f"""<
    <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="6">
        <TR><TD BORDER="0" COLSPAN="{len(TEXT)}"><B>{label}</B></TD></TR>
        {''.join(rows)}
        <TR><TD BORDER="0" COLSPAN="{len(TEXT)}">pola ditemukan pada indeks {MATCH_INDEX}; arah perbandingan {compare_direction}</TD></TR>
    </TABLE>
    >"""


def make_kmp_match():
    graph = Digraph("kmp_match")
    graph.attr(rankdir="TB", bgcolor="white", margin="0.12")
    graph.node("match", label=matching_table("KMP", "kiri ke kanan"), shape="plain")
    save_png(graph, "kmp_match.png")


def make_boyer_moore_match():
    graph = Digraph("boyer_moore_match")
    graph.attr(rankdir="TB", bgcolor="white", margin="0.12")
    graph.node(
        "match",
        label=matching_table("Boyer-Moore", "kanan ke kiri"),
        shape="plain",
    )
    save_png(graph, "boyer_moore_match.png")


def make_flowchart():
    graph = Digraph("flowchart_string_matching")
    graph.attr(rankdir="TB", bgcolor="white", margin="0.12")
    graph.attr("node", shape="box", style="rounded,filled", color="#2F4858", fillcolor="#F7FBFF", fontname="Arial")
    graph.attr("edge", color="#2F4858", fontname="Arial")

    graph.node("start", "Mulai")
    graph.node("input", "Masukkan text dan pattern")
    graph.node("pre", "Pra-proses pattern\nKMP: LPS\nBM: last occurrence")
    graph.node("compare", "Bandingkan pattern\ndengan bagian text")
    graph.node("match", "Semua karakter cocok?", shape="diamond", fillcolor="#FFF7E6")
    graph.node("found", "Kembalikan indeks awal")
    graph.node("shift", "Jika tidak cocok,\ngeser pattern sesuai tabel")
    graph.node("done", "Tidak ada posisi tersisa?", shape="diamond", fillcolor="#FFF7E6")
    graph.node("not_found", "Kembalikan -1")
    graph.node("end", "Selesai")

    graph.edge("start", "input")
    graph.edge("input", "pre")
    graph.edge("pre", "compare")
    graph.edge("compare", "match")
    graph.edge("match", "found", label="Ya")
    graph.edge("found", "end")
    graph.edge("match", "shift", label="Tidak")
    graph.edge("shift", "done")
    graph.edge("done", "compare", label="Tidak")
    graph.edge("done", "not_found", label="Ya")
    graph.edge("not_found", "end")

    save_png(graph, "flowchart_string_matching.png")


if __name__ == "__main__":
    make_kmp_match()
    make_boyer_moore_match()
    make_flowchart()
