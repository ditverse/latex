# ============================================================
# Praktikum 1 - Kompleksitas Algoritma
# Algoritma  : Selection Sort
# Sumber     : Langkah Praktikum
# File       : selection_sort.py
# ============================================================

def selection_sort(arr):
    """
    Mengurutkan array dengan algoritma Selection Sort.
    Setiap pass mencari elemen terkecil dari sisa array
    lalu menukarnya ke posisi yang tepat.
    """
    n = len(arr)
    total_comparisons = 0
    total_swaps = 0

    print(f"Array awal : {arr}")
    print("-" * 55)

    for i in range(n - 1):
        # Asumsikan elemen terkecil ada di posisi i
        min_idx = i
        pass_comparisons = 0
        pass_swaps = 0

        # Cari elemen terkecil dari i+1 hingga akhir array
        for j in range(i + 1, n):
            pass_comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Tukar elemen terkecil ke posisi i (jika berbeda)
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            pass_swaps += 1

        total_comparisons += pass_comparisons
        total_swaps += pass_swaps

        print(f"Pass {i + 1:2d} | Array: {arr} | "
              f"Perbandingan: {pass_comparisons:2d} | "
              f"Pertukaran: {pass_swaps}")

    print("-" * 55)
    print(f"Array akhir        : {arr}")
    print(f"Total perbandingan : {total_comparisons}")
    print(f"Total pertukaran   : {total_swaps}")

    return arr


def hitung_kompleksitas(n):
    """
    Menghitung T(n) untuk Selection Sort secara analitik.
    T(n) = jumlah perbandingan = (n-1) + (n-2) + ... + 1
         = n(n-1)/2
    """
    print(f"\n--- Derivasi T(n) untuk n = {n} ---")
    perbandingan_per_pass = []
    total = 0

    for i in range(n - 1):
        c = n - 1 - i
        perbandingan_per_pass.append(c)
        total += c

    print(f"Perbandingan tiap pass : {perbandingan_per_pass}")
    print(f"T(n) = {' + '.join(map(str, perbandingan_per_pass))}")
    print(f"T(n) = {total}")
    print(f"Rumus : n(n-1)/2 = {n}({n}-1)/2 = {n * (n - 1) // 2}")
    print(f"Kompleksitas Waktu : O(n^2)")


# ============================================================
# Main Program
# ============================================================
if __name__ == "__main__":
    # --- Kasus Uji 1: Array acak ---
    data1 = [64, 25, 12, 22, 11]
    print("=" * 55)
    print("  SELECTION SORT — Kasus Uji 1")
    print("=" * 55)
    selection_sort(data1.copy())
    hitung_kompleksitas(len(data1))

    # --- Kasus Uji 2: Array sudah terurut (best case) ---
    data2 = [1, 2, 3, 4, 5]
    print("\n" + "=" * 55)
    print("  SELECTION SORT — Kasus Uji 2 (sudah terurut)")
    print("=" * 55)
    selection_sort(data2.copy())
    hitung_kompleksitas(len(data2))

    # --- Kasus Uji 3: Array terurut terbalik (worst case) ---
    data3 = [5, 4, 3, 2, 1]
    print("\n" + "=" * 55)
    print("  SELECTION SORT — Kasus Uji 3 (terurut terbalik)")
    print("=" * 55)
    selection_sort(data3.copy())
    hitung_kompleksitas(len(data3))

# ============================================================
# Contoh Output:
# ============================================================
# ============================================================
#   SELECTION SORT — Kasus Uji 1
# ============================================================
# Array awal : [64, 25, 12, 22, 11]
# -------------------------------------------------------
# Pass  1 | Array: [11, 25, 12, 22, 64] | Perbandingan:  4 | Pertukaran: 1
# Pass  2 | Array: [11, 12, 25, 22, 64] | Perbandingan:  3 | Pertukaran: 1
# Pass  3 | Array: [11, 12, 22, 25, 64] | Perbandingan:  2 | Pertukaran: 1
# Pass  4 | Array: [11, 12, 22, 25, 64] | Perbandingan:  1 | Pertukaran: 0
# -------------------------------------------------------
# Array akhir        : [11, 12, 22, 25, 64]
# Total perbandingan : 10
# Total pertukaran   : 3
#
# --- Derivasi T(n) untuk n = 5 ---
# Perbandingan tiap pass : [4, 3, 2, 1]
# T(n) = 4 + 3 + 2 + 1
# T(n) = 10
# Rumus : n(n-1)/2 = 5(5-1)/2 = 10
# Kompleksitas Waktu : O(n^2)
