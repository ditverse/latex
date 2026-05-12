# ============================================================
# Praktikum 2 - Algoritma Brute Force
# Algoritma  : Pencarian Elemen Terbesar (Max Element)
# Sumber     : Langkah Praktikum (a)
# File       : pencarian_terbesar.py
# ============================================================

def cari_elemen_terbesar(arr):
    """
    Mencari nilai terbesar dalam array menggunakan pendekatan Brute Force.
    Memeriksa setiap elemen satu per satu dari awal hingga akhir.
    """
    if not arr:
        return None, 0

    n = len(arr)
    # Asumsikan elemen pertama adalah yang terbesar
    maksimum = arr[0]
    total_perbandingan = 0

    print(f"Mencari elemen terbesar pada array: {arr}")
    print("-" * 50)

    # Bandingkan dengan elemen sisa (mulai dari indeks 1)
    for i in range(1, n):
        total_perbandingan += 1
        
        # Jika ditemukan nilai yang lebih besar, perbarui variabel maksimum
        if arr[i] > maksimum:
            print(f"Langkah {i}: {arr[i]} > {maksimum} -> Maksimum baru = {arr[i]}")
            maksimum = arr[i]
        else:
            print(f"Langkah {i}: {arr[i]} tidak lebih besar dari {maksimum}")

    print("-" * 50)
    print(f"Nilai Terbesar       : {maksimum}")
    print(f"Total Perbandingan   : {total_perbandingan}")
    print(f"Kompleksitas (n)     : T(n) = n - 1 = {n} - 1 = {n - 1}")
    
    return maksimum, total_perbandingan


# ============================================================
# Main Program
# ============================================================
if __name__ == "__main__":
    # --- Kasus Uji 1: Acak ---
    data1 = [12, 45, 2, 78, 34, 56, 90, 23, 1, 67]
    print("=" * 50)
    print("  KASUS 1: Array Acak")
    print("=" * 50)
    cari_elemen_terbesar(data1)

    # --- Kasus Uji 2: Terurut Naik ---
    data2 = [10, 20, 30, 40, 50]
    print("\n" + "=" * 50)
    print("  KASUS 2: Array Terurut Naik (Terburuk untuk assignment)")
    print("=" * 50)
    cari_elemen_terbesar(data2)

    # --- Kasus Uji 3: Terurut Turun ---
    data3 = [50, 40, 30, 20, 10]
    print("\n" + "=" * 50)
    print("  KASUS 3: Array Terurut Turun (Terbaik untuk assignment)")
    print("=" * 50)
    cari_elemen_terbesar(data3)

# ============================================================
# Contoh Output (Kasus 1):
# ============================================================
# Mencari elemen terbesar pada array: [12, 45, 2, 78, 34, 56, 90, 23, 1, 67]
# --------------------------------------------------
# Langkah 1: 45 > 12 -> Maksimum baru = 45
# Langkah 2: 2 tidak lebih besar dari 45
# Langkah 3: 78 > 45 -> Maksimum baru = 78
# Langkah 4: 34 tidak lebih besar dari 78
# ...
# --------------------------------------------------
# Nilai Terbesar       : 90
# Total Perbandingan   : 9
# Kompleksitas (n)     : T(n) = n - 1 = 10 - 1 = 9
