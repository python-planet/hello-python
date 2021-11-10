"""
Program perulangan membaca buku
"""

jumlah_buku = 10
print(' Ibu berkata, "baca semua buku')

jumlah_buku_yang_sudah_dibaca = 0

for jumlah_buku_yang_sudah_dibaca in range (1, jumlah_buku+1):
    print(f"Buku ke {jumlah_buku_yang_sudah_dibaca} sudah dibaca")

print(f"jumlah buku yang sudah dibaca adalah {jumlah_buku_yang_sudah_dibaca}")