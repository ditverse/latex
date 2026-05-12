# ============================================================
# Praktikum 2 - Algoritma Brute Force
# Algoritma  : Uji Bilangan Prima (Primality Testing)
# Sumber     : Langkah Praktikum (b) & Post Test
# File       : uji_bilangan_prima.py
# ============================================================

import math

def uji_prima_bruteforce_lambat(n):
    """
    Menguji keprimaan dengan mencoba membagi n dari 2 hingga n-1.
    (Pendekatan Brute Force paling dasar).
    """
    if n <= 1:
        return False, 0
        
    total_pembagian = 0
    print(f"Menguji bilangan {n} (Brute Force Dasar: 2 hingga {n-1})")
    
    for i in range(2, n):
        total_pembagian += 1
        if n % i == 0:
            print(f" -> Bukan Prima. Habis dibagi {i}")
            return False, total_pembagian
            
    print(" -> Merupakan Bilangan Prima!")
    return True, total_pembagian


def uji_prima_bruteforce_optimal(n):
    """
    Menguji keprimaan dengan mencoba membagi n dari 2 hingga akar(n).
    (Ini merupakan Post Test: bagaimana membuat uji prima lebih efisien
    namun tetap menggunakan pendekatan Brute Force).
    """
    if n <= 1:
        return False, 0
        
    total_pembagian = 0
    batas = math.floor(math.sqrt(n))
    
    print(f"Menguji bilangan {n} (Brute Force Optimal: 2 hingga {batas})")
    
    for i in range(2, batas + 1):
        total_pembagian += 1
        if n % i == 0:
            print(f" -> Bukan Prima. Habis dibagi {i}")
            return False, total_pembagian
            
    print(" -> Merupakan Bilangan Prima!")
    return True, total_pembagian


def evaluasi_kompleksitas(n):
    """
    Menjalankan kedua fungsi dan membandingkan beban kerjanya.
    """
    print("=" * 55)
    print(f"  EVALUASI BILANGAN: {n}")
    print("=" * 55)
    
    # 1. Cara Lambat
    hasil1, step1 = uji_prima_bruteforce_lambat(n)
    
    print("-" * 55)
    
    # 2. Cara Optimal
    hasil2, step2 = uji_prima_bruteforce_optimal(n)
    
    print("-" * 55)
    print(f"Kesimpulan untuk N = {n}:")
    print(f"Status Prima    : {hasil1}")
    print(f"Langkah Lambat  : {step1} kali operasi modulus (O(n))")
    print(f"Langkah Optimal : {step2} kali operasi modulus (O(akar(n)))")


# ============================================================
# Main Program
# ============================================================
if __name__ == "__main__":
    # --- Kasus 1: Bilangan Bukan Prima (Kecil) ---
    evaluasi_kompleksitas(15)
    
    # --- Kasus 2: Bilangan Prima (Kecil) ---
    evaluasi_kompleksitas(29)
    
    # --- Kasus 3: Bilangan Prima (Besar) - Menunjukkan Signifikansi Optimasi ---
    evaluasi_kompleksitas(997)
    
    # --- Kasus 4: Bilangan Bukan Prima (Besar, faktor besar) ---
    evaluasi_kompleksitas(899)  # 899 = 29 * 31

# ============================================================
# Contoh Output:
# ============================================================
# =======================================================
#   EVALUASI BILANGAN: 997
# =======================================================
# Menguji bilangan 997 (Brute Force Dasar: 2 hingga 996)
#  -> Merupakan Bilangan Prima!
# -------------------------------------------------------
# Menguji bilangan 997 (Brute Force Optimal: 2 hingga 31)
#  -> Merupakan Bilangan Prima!
# -------------------------------------------------------
# Kesimpulan untuk N = 997:
# Status Prima    : True
# Langkah Lambat  : 995 kali operasi modulus (O(n))
# Langkah Optimal : 30 kali operasi modulus (O(akar(n)))
