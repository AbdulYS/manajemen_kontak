"Program Manajemen kontak"
import kontak

def main():
    kontak_kantor = kontak.Kontak()
    kontak_keluarga =  kontak.Kontak()

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
            kontak_keluarga.keluar_kontak()
            break
        else:
            print("Anda memasukan pilihan yang salah")

if __name__ == "__main__":
    main()