"Program Manajemen kontak"

class Kontak:
    def __init__(self):
        self.kontak = []

    def melihat_kontak(self):
        # Melihat semua kontak
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f'{num}. {item["nama"]} ({item["HP"]}), {item["Email"]}')
        else:
            print("kontak masih kosong!")
            return 1

    def menambah_kontak(self):
        # Menambahkan kontak baru
        nama = input("Masukan nama kontak yang baru: ")
        HP = input("Masukan nomer hp yang baru: ")
        email = input("Masukan email kontak yang baru: ")
        kontak_baru = {'nama': nama, 'HP': HP, 'Email': email}
        self.kontak.append(kontak_baru)
        print("Kontak baru berhasil ditambahkan!")

    def menghapus_kontak(self):
        # Menghapus kontak
        if self.melihat_kontak() == 1:
            return
        else:
            i_hapus = int(input("Masukan nomer kontak yang akan dihapus: "))
            del self.kontak[i_hapus - 1]
            print("Kontak yang dimaksud sudah dihapus")

kontak_kantor = Kontak()
kontak_keluarga = Kontak()

while True:
    print("\nMenu Kontak")
    print("1. Melihat semua kontak")
    print("2. Menambahkan kontak baru")
    print("3. Menghapus kontak")
    print("4. Keluar dari kontak")

    pilihan = input("Masukan pilihan menu kontak (1,2,3 atau 4):")


    if pilihan == '1':
        kontak_keluarga.melihat_kontak()


    elif pilihan == '2':
        kontak_keluarga.menambah_kontak()

    elif pilihan == '3':
        kontak_keluarga.menghapus_kontak()

    elif pilihan == '4':
        # Keluar dari kontak
        break
    else:
        print("Anda memasukan pilihan yang salah")