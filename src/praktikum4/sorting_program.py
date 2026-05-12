def minmaks(arr, i, j):
    # basis: 1 elemen
    if i == j:
        return arr[i], arr[i]

    # basis: 2 elemen, bandingkan langsung
    if i == j - 1:
        if arr[i] < arr[j]:
            return arr[i], arr[j]
        else:
            return arr[j], arr[i]

    # rekursif: bagi tabel di titik tengah
    k = (i + j) // 2
    min1, maks1 = minmaks(arr, i, k)
    min2, maks2 = minmaks(arr, k + 1, j)

    # combine: ambil min dan maks dari kedua bagian
    return min(min1, min2), max(maks1, maks2)


def merge(arr, kiri, tengah, kanan):
    # salin dua bagian ke array sementara
    kidal1 = arr[kiri:tengah + 1]
    kidal2 = arr[tengah + 1:kanan + 1]

    i = j = 0
    k = kiri

    # gabungkan dua bagian secara terurut
    while i < len(kidal1) and j < len(kidal2):
        if kidal1[i] <= kidal2[j]:
            arr[k] = kidal1[i]
            i += 1
        else:
            arr[k] = kidal2[j]
            j += 1
        k += 1

    # salin sisa elemen kiri jika ada
    while i < len(kidal1):
        arr[k] = kidal1[i]
        i += 1
        k += 1

    # salin sisa elemen kanan jika ada
    while j < len(kidal2):
        arr[k] = kidal2[j]
        j += 1
        k += 1


def merge_sort(arr, i, j):
    # basis: array 1 elemen sudah terurut
    if i >= j:
        return

    # divide: tentukan titik tengah
    k = (i + j) // 2

    # conquer: urutkan bagian kiri dan kanan secara rekursif
    merge_sort(arr, i, k)
    merge_sort(arr, k + 1, j)

    # combine: gabungkan hasil pengurutan
    merge(arr, i, k, j)


def partisi(arr, i, j):
    # pilih elemen tengah sebagai pivot
    pivot = arr[(i + j) // 2]
    p, q = i, j

    while True:
        # scan dari kiri sampai menemukan elemen >= pivot
        while arr[p] < pivot:
            p += 1
        # scan dari kanan sampai menemukan elemen <= pivot
        while arr[q] > pivot:
            q -= 1

        # jika belum bertemu, tukar dan geser indeks
        if p < q:
            arr[p], arr[q] = arr[q], arr[p]
            p += 1
            q -= 1
        else:
            break

    return q


def quick_sort(arr, i, j):
    # basis: array 1 elemen atau kosong
    if i >= j:
        return

    # partisi dan dapatkan indeks pembagi
    k = partisi(arr, i, j)

    # rekursif urutkan bagian kiri dan kanan
    quick_sort(arr, i, k)
    quick_sort(arr, k + 1, j)


if __name__ == "__main__":
    data = [4, 12, 23, 9, 21, 1, 35, 2, 24]
    print("Data awal:", data)

    # MinMaks D&C
    mn, mx = minmaks(data, 0, len(data) - 1)
    print(f"\nMinMaks D&C -> Min: {mn}, Maks: {mx}")

    # Merge Sort
    arr_ms = data.copy()
    merge_sort(arr_ms, 0, len(arr_ms) - 1)
    print(f"Merge Sort  -> {arr_ms}")

    # Quick Sort
    arr_qs = data.copy()
    quick_sort(arr_qs, 0, len(arr_qs) - 1)
    print(f"Quick Sort  -> {arr_qs}")
