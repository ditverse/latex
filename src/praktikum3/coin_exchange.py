def coin_exchange(coins, amount):
    # urutkan koin dari nilai terbesar ke terkecil (strategi greedy)
    coins_sorted = sorted(coins, reverse=True)
    result = []
    remaining = amount

    for coin in coins_sorted:
        # ambil koin sebanyak mungkin selama tidak melebihi sisa
        while remaining >= coin:
            result.append(coin)
            remaining -= coin

    if remaining == 0:
        return result
    else:
        return None  # tidak ada solusi


def tampilkan_hasil(coins, amount):
    print(f"Nilai yang ditukar : {amount}")
    print(f"Himpunan koin      : {sorted(coins, reverse=True)}")

    hasil = coin_exchange(coins, amount)

    if hasil:
        from collections import Counter
        rekap = Counter(hasil)
        print("Solusi koin        :", dict(rekap))
        print("Total koin dipakai :", len(hasil))
        print("Rincian            :", hasil)
    else:
        print("Tidak ada solusi.")


if __name__ == "__main__":
    # koin yang tersedia (denominasi rupiah)
    koin = [1000, 500, 200, 100, 50, 25, 10, 5, 1]

    # kasus uji tunggal sesuai langkah praktikum
    tampilkan_hasil(koin, 2750)
