#Superclass
class Pendidikan():
    
    def __init__(self, nama_sekolah, alamat_sekolah ) :
        self.nama_sekolah = nama_sekolah
        self.alamat_sekolah = alamat_sekolah

#Subclass Pendidikan Sekolah Menengah Pertama dan Sekolah Menengah Atas
class Pendidikan_SekolahMenengahPertama(Pendidikan):
    pass

class Pendidikan_SekolahMenengahAtas(Pendidikan):
    pass

SDNBlokICilegon = Pendidikan("SDN Blok I", "Cilegon")
SMPMuhammadiyahCilegon = Pendidikan_SekolahMenengahPertama("SMP Muhammadiyah", "Cilegon")
SMAMuhammadiyahCilegon = Pendidikan_SekolahMenengahAtas("SMA Muhammadiyah", "Cilegon")

#Output
print(SDNBlokICilegon.nama_sekolah, SDNBlokICilegon.alamat_sekolah)
print(SMPMuhammadiyahCilegon.nama_sekolah, SMPMuhammadiyahCilegon.alamat_sekolah)
print(SMAMuhammadiyahCilegon.nama_sekolah, SMAMuhammadiyahCilegon.alamat_sekolah)