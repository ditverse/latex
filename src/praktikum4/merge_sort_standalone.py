def merge(arr, kiri, tengah, kanan):
    # salin dua bagian ke array sementara
    bagian_kiri  = arr[kiri:tengah + 1]
    bagian_kanan = arr[tengah + 1:kanan + 1]

    i = j = 0
    k = kiri

    # gabungkan dua bagian ke array utama secara terurut
    while i < len(bagian_kiri) and j < len(bagian_kanan):
        if bagian_kiri[i] <= bagian_kanan[j]:
            arr[k] = bagian_kiri[i]
            i += 1
        else:
            arr[k] = bagian_kanan[j]
            j += 1
        k += 1

    # salin sisa bagian kiri jika masih ada
    while i < len(bagian_kiri):
        arr[k] = bagian_kiri[i]
        i += 1
        k += 1

    # salin sisa bagian kanan jika masih ada
    while j < len(bagian_kanan):
        arr[k] = bagian_kanan[j]
        j += 1
        k += 1


def merge_sort(arr, i, j, depth=0):
    indent = "  " * depth

    # basis: array dengan 1 elemen sudah terurut
    if i >= j:
        return

    # divide: hitung titik tengah pembagi
    k = (i + j) // 2
    print(f"{indent}Divide  [{i}..{j}] -> kiri [{i}..{k}], kanan [{k+1}..{j}]")

    # conquer: urutkan bagian kiri secara rekursif
    merge_sort(arr, i, k, depth + 1)

    # conquer: urutkan bagian kanan secara rekursif
    merge_sort(arr, k + 1, j, depth + 1)

    # combine: gabungkan hasil pengurutan kedua bagian
    merge(arr, i, k, j)
    print(f"{indent}Combine [{i}..{j}] -> {arr[i:j+1]}")


if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    print("Data awal    :", data)
    print("\nProses Merge Sort (D&C):")
    print("-" * 45)

    merge_sort(data, 0, len(data) - 1)

    print("-" * 45)
    print("Data terurut :", data)
