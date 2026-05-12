def bagi(arr, i, j):
    # cari indeks elemen terkecil dari A[i..j]
    idx_min = i
    for k in range(i + 1, j + 1):
        if arr[k] < arr[idx_min]:
            idx_min = k

    # tukar elemen terkecil ke posisi i
    arr[i], arr[idx_min] = arr[idx_min], arr[i]


def selection_sort_dc(arr, i, j):
    # basis: ukuran subarray <= 1, sudah terurut
    if i >= j:
        return

    # decrease: letakkan elemen terkecil A[i..j] ke posisi i
    bagi(arr, i, j)

    # conquer: urutkan sisa subarray A[i+1..j] secara rekursif
    selection_sort_dc(arr, i + 1, j)


if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Data awal   :", arr)

    selection_sort_dc(arr, 0, len(arr) - 1)

    print("Data terurut:", arr)
