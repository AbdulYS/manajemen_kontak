'Berisi kelas kontak untuk menjalankan program kontak'

import document
class Kontak:
    def __init__(self):
        self.kontak = document.membuka_kontak()

    def melihat_kontak(self):
        # Melihat semua kontak
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f'{num}. ' + item)
        else:
            print("kontak masih kosong!")
            return 1

    def menambah_kontak(self):
        # Menambahkan kontak baru
        nama = input("Masukan nama kontak yang baru: ")
        HP = input("Masukan nomer hp yang baru: ")
        email = input("Masukan email kontak yang baru: ")
        kontak_baru = f'{nama} ({HP}, {email})' + '\n'
        self.kontak.append(kontak_baru)
        print("Kontak baru berhasil ditambahkan!")

    def menghapus_kontak(self):
        # Menghapus kontak
        if self.melihat_kontak() == 1:
            return
        else:
            try:
                i_hapus = int(input("Masukan nomer kontak yang akan dihapus: "))
                del self.kontak[i_hapus - 1]
                print("Kontak yang dimaksud sudah dihapus")
            except:
                print("Input yang anda masukan salah")

    def keluar_kontak(self):
        document.menyimpan_kontak(isi=self.kontak)
