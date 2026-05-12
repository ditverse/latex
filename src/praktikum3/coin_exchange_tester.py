from collections import Counter


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

    return result if remaining == 0 else None


def analisis_kasus(coins, amount, label=""):
    print(f"\n{'='*50}")
    if label:
        print(f"  {label}")
    print(f"{'='*50}")
    print(f"Nilai ditukar : {amount}")
    print(f"Koin tersedia : {sorted(coins, reverse=True)}")

    hasil = coin_exchange(coins, amount)

    if hasil:
        rekap = Counter(hasil)
        print(f"Solusi        : {dict(rekap)}")
        print(f"Jumlah koin   : {len(hasil)}")
    else:
        print("Tidak ada solusi (greedy gagal).")

    return hasil


def hitung_kompleksitas(coins, amount):
    # hitung iterasi aktual untuk analisis kompleksitas
    coins_sorted = sorted(coins, reverse=True)
    n = len(coins_sorted)
    iterasi = 0
    remaining = amount

    for coin in coins_sorted:
        while remaining >= coin:
            remaining -= coin
            iterasi += 1

    print(f"\nAnalisis Kompleksitas (amount={amount}, n={n} jenis koin):")
    print(f"Jumlah iterasi while   : {iterasi}")
    print(f"Jumlah iterasi for     : {n}")
    print(f"T(n) = O(n + amount/koin_terkecil) -> praktis O(n) untuk denominasi wajar")


if __name__ == "__main__":
    koin_std = [1000, 500, 200, 100, 50, 25, 10, 5, 1]

    # kasus 1: solusi optimal
    analisis_kasus(koin_std, 2750, "Kasus 1: Solusi Normal")

    # kasus 2: jumlah besar
    analisis_kasus(koin_std, 9875, "Kasus 2: Jumlah Besar")

    # kasus 3: greedy tidak optimal (denominasi tidak kanonik)
    koin_non_kanonik = [10, 6, 1]
    analisis_kasus(koin_non_kanonik, 12, "Kasus 3: Greedy Tidak Optimal (koin [10,6,1], target 12)")
    print("  Solusi greedy: 10+1+1 = 3 koin")
    print("  Solusi optimal: 6+6   = 2 koin")

    # analisis kompleksitas
    hitung_kompleksitas(koin_std, 2750)
