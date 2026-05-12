# ============================================================
# Praktikum 1 - Kompleksitas Algoritma
# Algoritma  : Insertion Sort
# Sumber     : Post Test
# File       : insertion_sort.py
# ============================================================

def insertion_sort(arr):
    """
    Mengurutkan array dengan algoritma Insertion Sort.
    Setiap elemen disisipkan ke posisi yang tepat
    di dalam bagian array yang sudah terurut.
    """
    n = len(arr)
    total_comparisons = 0
    total_shifts = 0

    print(f"Array awal : {arr}")
    print("-" * 60)

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        pass_comparisons = 0
        pass_shifts = 0

        # Geser elemen yang lebih besar dari key ke kanan
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            pass_comparisons += 1
            pass_shifts += 1

        # Hitung perbandingan terakhir (kondisi berhenti)
        if j >= 0:
            pass_comparisons += 1

        # Sisipkan key ke posisi yang tepat
        arr[j + 1] = key

        total_comparisons += pass_comparisons
        total_shifts += pass_shifts

        print(f"Pass {i:2d} | key={key:3d} | Array: {arr} | "
              f"Perbandingan: {pass_comparisons} | "
              f"Pergeseran: {pass_shifts}")

    print("-" * 60)
    print(f"Array akhir        : {arr}")
    print(f"Total perbandingan : {total_comparisons}")
    print(f"Total pergeseran   : {total_shifts}")

    return arr


def hitung_kompleksitas(n, kasus="rata-rata"):
    """
    Menampilkan analisis kompleksitas Insertion Sort.
    - Best Case  : O(n)  — array sudah terurut
    - Worst Case : O(n^2) — array terurut terbalik
    - Average    : O(n^2)
    """
    print(f"\n--- Analisis Kompleksitas Insertion Sort (n = {n}) ---")
    print(f"Best Case  (terurut)         : T(n) = n-1 = {n - 1}  -> O(n)")
    print(f"Worst Case (terurut terbalik): T(n) = n(n-1)/2 = "
          f"{n * (n - 1) // 2}  -> O(n^2)")
    print(f"Average Case                 : T(n) aprox. n(n-1)/4 = "
          f"{n * (n - 1) // 4}  -> O(n^2)")


def bandingkan_dengan_selection_sort(n):
    """
    Perbandingan teoritis antara Insertion Sort dan Selection Sort.
    """
    print(f"\n--- Perbandingan Insertion Sort vs Selection Sort (n={n}) ---")
    print(f"{'Kasus':<25} {'Insertion Sort':<20} {'Selection Sort'}")
    print("-" * 65)
    print(f"{'Best Case':<25} {'O(n)':<20} {'O(n^2)'}")
    print(f"{'Worst Case':<25} {'O(n^2)':<20} {'O(n^2)'}")
    print(f"{'Average Case':<25} {'O(n^2)':<20} {'O(n^2)'}")
    print(f"{'Perbandingan (worst)':<25} {n*(n-1)//2:<20} {n*(n-1)//2}")
    print(f"{'Pergeseran/Pertukaran':<25} {'Banyak (geser)':<20} {'Sedikit (tukar)'}")
    print(f"{'Stabil':<25} {'Ya':<20} {'Tidak'}")
    print(f"{'Adaptif':<25} {'Ya (best=O(n))':<20} {'Tidak'}")


# ============================================================
# Main Program
# ============================================================
if __name__ == "__main__":
    # --- Kasus Uji 1: Array acak ---
    data1 = [64, 25, 12, 22, 11]
    print("=" * 60)
    print("  INSERTION SORT — Kasus Uji 1 (acak)")
    print("=" * 60)
    insertion_sort(data1.copy())
    hitung_kompleksitas(len(data1))

    # --- Kasus Uji 2: Best case (sudah terurut) ---
    data2 = [1, 2, 3, 4, 5]
    print("\n" + "=" * 60)
    print("  INSERTION SORT — Kasus Uji 2 (sudah terurut / best case)")
    print("=" * 60)
    insertion_sort(data2.copy())

    # --- Kasus Uji 3: Worst case (terurut terbalik) ---
    data3 = [5, 4, 3, 2, 1]
    print("\n" + "=" * 60)
    print("  INSERTION SORT — Kasus Uji 3 (terurut terbalik / worst case)")
    print("=" * 60)
    insertion_sort(data3.copy())

    # --- Perbandingan teoritis ---
    bandingkan_dengan_selection_sort(5)

# ============================================================
# Contoh Output:
# ============================================================
# ============================================================
#   INSERTION SORT — Kasus Uji 1 (acak)
# ============================================================
# Array awal : [64, 25, 12, 22, 11]
# ------------------------------------------------------------
# Pass  1 | key= 25 | Array: [25, 64, 12, 22, 11] | Perbandingan: 1 | Pergeseran: 1
# Pass  2 | key= 12 | Array: [12, 25, 64, 22, 11] | Perbandingan: 2 | Pergeseran: 2
# Pass  3 | key= 22 | Array: [12, 22, 25, 64, 11] | Perbandingan: 2 | Pergeseran: 2
# Pass  4 | key= 11 | Array: [11, 12, 22, 25, 64] | Perbandingan: 4 | Pergeseran: 4
# ------------------------------------------------------------
# Array akhir        : [11, 12, 22, 25, 64]
# Total perbandingan : 9
# Total pergeseran   : 9
#
# --- Analisis Kompleksitas Insertion Sort (n = 5) ---
# Best Case  (terurut)         : T(n) = n-1 = 4  → O(n)
# Worst Case (terurut terbalik): T(n) = n(n-1)/2 = 10  → O(n^2)
# Average Case                 : T(n) ≈ n(n-1)/4 = 5  → O(n^2)
#
# --- Perbandingan Insertion Sort vs Selection Sort (n=5) ---
# Kasus                     Insertion Sort       Selection Sort
# -----------------------------------------------------------------
# Best Case                 O(n)                 O(n^2)
# Worst Case                O(n^2)               O(n^2)
# Average Case              O(n^2)               O(n^2)
# Perbandingan (worst)      10                   10
# Pergeseran/Pertukaran     Banyak (geser)       Sedikit (tukar)
# Stabil                    Ya                   Tidak
# Adaptif                   Ya (best=O(n))       Tidak
