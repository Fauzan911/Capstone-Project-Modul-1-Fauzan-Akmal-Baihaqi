print("\n---------------------------------------------------------------")
print("\t \t Gudang Data Stok PT.Bubut")
print("---------------------------------------------------------------")

# Data stok disimpan dalam list
stok_gudang = [
    {"kode": "Q1", "nama": "Spion Motor", "jumlah": 50, "lokasi": "Gudang 1"},
    {"kode": "Q2", "nama": "Aki Mobil", "jumlah": 30, "lokasi": "Gudang 2"},
    {"kode": "Q3", "nama": "Lampu Sen Motor", "jumlah": 20, "lokasi": "Gudang 1"},
]

# Data akun login
akun = {
    "jajang": "pass123"
}

def login():
    print("\n===== LOGIN =====")
    percobaan = 3
    while percobaan > 0:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        
        if username in akun and akun[username] == password:
            print("\nLogin berhasil! Selamat datang,", username)
            tampilkan_menu()
            return
        else:
            percobaan -= 1
            print(f"Login gagal! Username atau password salah. Percobaan tersisa: {percobaan}")
    print("\nTerlalu banyak percobaan gagal! Program keluar.")
    exit()

def tampilkan_menu():
    print("\n===== MENU UTAMA =====")
    print("1. Lihat Stok")
    print("2. Tambah Stok")
    print("3. Update Stok")
    print("4. Hapus Stok")
    print("5. Keluar")
    
    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        menu_lihat_stok()
    elif pilihan == "2":
        menu_tambah_stok()
    elif pilihan == "3":
        menu_update_stok()
    elif pilihan == "4":
        menu_hapus_stok()
    elif pilihan == "5":
        exit()
    else:
        print("Pilihan tidak valid!")
        tampilkan_menu()

def menu_lihat_stok():
    print("\n===== SUB MENU LIHAT STOK =====")
    print("1. Melihat Seluruh Data")
    print("2. Melihat Data Tertentu")
    print("3. Kembali ke Menu Utama")
    pilihan = input("Silakan Pilih Sub Menu Read Data [1-3]: ")
    
    if pilihan == "1":
        lihat_stok()
        menu_lihat_stok()
    elif pilihan == "2":
        lihat_stok_tertentu()
        menu_lihat_stok()
    elif pilihan == "3":
        tampilkan_menu()
    else:
        print("Pilihan tidak valid!")
        menu_lihat_stok()

def lihat_stok():
    print("\n===== DAFTAR SELURUH STOK =====")
    if not stok_gudang:
        print("Stok kosong.")
    else:
        for item in stok_gudang:
            print(f"Kode Barang: {item['kode']}, Nama: {item['nama']}, Jumlah: {item['jumlah']}, Lokasi: {item['lokasi']}")

def lihat_stok_tertentu():
    kode_barang = input("Masukkan Kode barang yang ingin dilihat: ")
    print(f"\nKode yang Anda cari = {kode_barang}")
    for item in stok_gudang:
        if item['kode'] == kode_barang:
            print(f"Kode Barang: {item['kode']}, Nama: {item['nama']}, Jumlah: {item['jumlah']}, Lokasi: {item['lokasi']}")
            return
    print("=====Kode tidak ditemukan!=====")

def menu_tambah_stok():
    print("\n===== SUB MENU MENAMBAH STOK =====")
    print("1. Menambah Stok")
    print("2. Kembali ke Menu Utama")
    pilihan = input("Silakan Pilih Sub Menu Menambah Data [1-2]: ")

    if pilihan == "1":
        tambah_stok()
        menu_tambah_stok()
    elif pilihan == "2":
        tampilkan_menu()
    else:
        print("Pilihan tidak valid!")
        menu_tambah_stok()
        
def tambah_stok():
    kode_barang = input("Masukkan kode barang: ")
    nama = input("Masukkan nama barang: ")
    jumlah = int(input("Masukkan jumlah barang: "))
    lokasi = input("Masukkan lokasi gudang: ")
    keputusan = input("Apakah Stok Data Akan Disimpan? (y/n): ")
    if keputusan == "y" or keputusan == "Y":
        stok_gudang.append({"kode": kode_barang, "nama": nama, "jumlah": jumlah, "lokasi": lokasi})
        print("=====Stok Barang Berhasil Ditambahkan!=====")
    else:
        print("=====Stok Barang Tidak Disimpan!=====.")

def menu_update_stok():
    print("\n===== SUB MENU UPDATE STOK =====")
    print("1. Update Stok")
    print("2. Kembali ke Menu Utama")
    pilihan = input("Silakan Pilih Sub Menu Update Data [1-2]: ")

    if pilihan == "1":
        update_stok()
        menu_update_stok()
    elif pilihan == "2":
        tampilkan_menu()
    else:
        print("Pilihan tidak valid!")
        menu_update_stok()


def update_stok():
    kode_barang = input("Masukkan Kode barang yang akan diupdate: ")
    for item in stok_gudang:
        if item['kode'] == kode_barang:
            print("\n===== Data Barang Saat Ini =====")
            print(f"Kode Barang: {item['kode']}, Nama: {item['nama']}, Jumlah: {item['jumlah']}, Lokasi: {item['lokasi']}")
            print("================================")
            keputusan = input("Apakah kamu yakin ingin mengupdate stok? (y/n): ")
            if keputusan == "y" or keputusan == "Y":
                nama_baru = input("Masukkan nama baru (kosongkan jika tidak diubah): ")
                jumlah_baru = input("Masukkan jumlah baru (kosongkan jika tidak diubah): ")
                lokasi_baru = input("Masukkan lokasi baru (kosongkan jika tidak diubah): ")
                
                if nama_baru:
                    item['nama'] = nama_baru
                if jumlah_baru.isdigit():
                    item['jumlah'] = int(jumlah_baru)
                if lokasi_baru:
                    item['lokasi'] = lokasi_baru

                keputusan1 = input("Apakah Stok Data Akan Disimpan? (y/n): ")
                if keputusan1 == "y" or keputusan1 == "Y":
                    print("=====Stok Barang Berhasil Diperbarui!=====")
                else:
                    print("=====Stok Barang Tidak Disimpan!=====.")
                return
            else:
                print("=====Stok Barang Tidak Jadi diupdate=====.")
                return

    print("=====Kode Tidak Ditemukan!=====")

def menu_hapus_stok():
    print("\n===== SUB MENU HAPUS STOK =====")
    print("1. Hapus Stok")
    print("2. Kembali ke Menu Utama")
    pilihan = input("Silakan Pilih Sub Menu Hapus Data [1-2]: ")

    if pilihan == "1":
        hapus_stok()
        menu_hapus_stok()
    elif pilihan == "2":
        tampilkan_menu()
    else:
        print("Pilihan tidak valid!")
        menu_hapus_stok()

def hapus_stok():
    lihat_stok()
    kode_barang = input("Masukkan kode barang yang akan dihapus: ")
    for i, item in enumerate(stok_gudang):
        if item['kode'] == kode_barang:
            keputusan = input("Apakah Anda yakin ingin menghapus barang ini? (y/n): ")
            if keputusan == "y" or keputusan == "Y":
                stok_gudang.pop(i)
                print("=====Stok Barang Berhasil Dihapus!=====")
            else:
                print("=====Stok Barang Tidak Jadi Dihapus!=====.")
            return
    print("Kode tidak ditemukan!")


if __name__ == "__main__":
    login()
