"""
Program perulangan membaca buku dengan while sampai faham
"""

jumlah_buku = 10
print(' Ibu berkata, "baca semua buku')

jumlah_buku_yang_sudah_dibaca_dan_dipahami = 0
total_jumlah_baca = 0

while total_jumlah_baca < jumlah_buku * 2:
    total_jumlah_baca = total_jumlah_baca + 1

    if jumlah_buku_yang_sudah_dibaca_dan_dipahami == 10:
        print(f"Buku ke {jumlah_buku_yang_sudah_dibaca_dan_dipahami + 1} belum paham")

    else:
        jumlah_buku_yang_sudah_dibaca_dan_dipahami = jumlah_buku_yang_sudah_dibaca_dan_dipahami + 1
        print(f'jumlah buku yang sudah dibaca dan dipahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami}')


print(f"jumlah buku yang sudah dibaca dan dipahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami}")
if jumlah_buku_yang_sudah_dibaca_dan_dipahami == jumlah_buku:
    print('"Bu, semua buku sudah dibaca dan dipahami"')
else:
    print(f'"Bu, tidak semua buku bisa dipahami, '
          f'saya hanya bisa memahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami} buku')

