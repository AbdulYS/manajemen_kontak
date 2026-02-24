"Program Manajemen kontak"

def melihat_kontak():
    # Melihat semua kontak
    if kontak:
        for num, item in enumerate(kontak, start=1):
            print(f'{num}. {item["nama"]} ({item["HP"]}), {item["Email"]}')
    else:
        print("kontak masih kosong!")
        return 1

def menambah_kontak():
    # Menambahkan kontak baru
    nama = input("Masukan nama kontak yang baru: ")
    HP = input("Masukan nomer hp yang baru: ")
    email = input("Masukan email kontak yang baru: ")
    kontak_baru = {'nama': nama, 'HP': HP, 'Email': email}
    kontak.append(kontak_baru)
    print("Kontak baru berhasil ditambahkan!")

def menghapus_kontak():
    # Menghapus kontak
    if melihat_kontak() == 1:
        return
    else:
        i_hapus = int(input("Masukan nomer kontak yang akan dihapus: "))
        del kontak[i_hapus - 1]
        print("Kontak yang dimaksud sudah dihapus")


kontak1= {'nama' : "Abdul", 'HP' : '089685984', 'Email' : 'Abdul@yahoo.com'}
kontak2= {'nama' : "Yusuf", 'HP' : '089859483', 'Email' : 'yusuf@yahoo.com'}
kontak = [kontak1, kontak2]

while True:
    print("\nMenu Kontak")
    print("1. Melihat semua kontak")
    print("2. Menambahkan kontak baru")
    print("3. Menghapus kontak")
    print("4. Keluar dari kontak")

    pilihan = input("Masukan pilihan menu kontak (1,2,3 atau 4):")


    if pilihan == '1':
        melihat_kontak()


    elif pilihan == '2':
        menambah_kontak()

    elif pilihan == '3':
        menghapus_kontak()

    elif pilihan == '4':
        # Keluar dari kontak
        break
    else:
        print("Anda memasukan pilihan yang salah")