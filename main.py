from geometri.bangun_ruang import BangunRuang
from geometri.segitiga import Segitiga

from geometri.persegi_panjang import PersegiPanjang
p1 = PersegiPanjang(10,3)
print(p1.info())
print(p1.hitung_luas())

s1 = Segitiga(4,6)
print(s1.info())
print(s1.hitung_luas())

print('\nMencoba membuat object dari bangun ruang')
b1 = BangunRuang()
print(b1.Info())
print(b1.hitung_luas())

daftar_bangun_ruang = []
daftar_bangun_ruang.append(p1)
daftar_bangun_ruang.append(s1)
print('\nPolymorpism')
for bangun_ruang in daftar_bangun_ruang:
    print(bangun_ruang.info())