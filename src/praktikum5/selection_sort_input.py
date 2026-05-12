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

    # decrease: letakkan elemen terkecil ke posisi i
    bagi(arr, i, j)

    # conquer: rekursif pada subarray yang lebih kecil
    selection_sort_dc(arr, i + 1, j)


if __name__ == "__main__":
    # terima input array dari pengguna
    raw = input("Masukkan bilangan dipisah spasi: ")
    arr = list(map(int, raw.split()))

    print("Data awal   :", arr)
    selection_sort_dc(arr, 0, len(arr) - 1)
    print("Data terurut:", arr)
