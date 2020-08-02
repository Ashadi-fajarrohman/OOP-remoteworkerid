from geometri.bangun_ruang import BangunRuang


class PersegiPanjang(BangunRuang):
    def __init__(self, p, l):
        self.p = p
        self.l = l

    def info(self):
        return f'modul menghitung rumus-rumus tentang persegi panjang = {self.p} dan tinggi = {self.l}'

    def hitung_luas(self):
        return self.p * self.l