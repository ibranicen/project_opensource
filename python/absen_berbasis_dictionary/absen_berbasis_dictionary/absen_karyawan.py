karyawan_db = {}

def menu():
    print("="*50)
    print("MENU".center(50))
    print("="*50)
    print("1. Tambahkan Data (Ketik 1)")
    print("2. Cek Data karyawan (Ketik 2)")
    print("3. Hapus Data karyawan (Ketik 3)")
    print("4. Ubah Data karyawan (Ketik 4)")
    print("="*50)

def Tambah_Data():
    while True:
        try:
            print("-"*50)
            user_input_id = int(input("\n[~] Masukan ID Anda >> "))

            if user_input_id > 999 or user_input_id < 100 :
                print("\n[!] ID USER HARUS 3 DIGIT")
                raise ValueError
            
            elif user_input_id in karyawan_db:
                print("="*50)   
                print(f"\n[-] KARYAWAN DENGAN ID: {user_input_id} Sudah Ada")
                raise ValueError
            
            else:
                break

        except ValueError:
            print("\n[!] HARAP INPUTKAN ID DENGAN BENAR")
            continue

    if user_input_id not in karyawan_db:
        while True:
            print("-"*50)
            nama = input("\n[~] Masukan Nama Anda >> ").title()

            if not nama or nama.isdigit():
                print("\n[!] ERROR INPUT USER")
                continue
            else:
                break
        
        while True:
            print("-"*50)
            posisi = input("\n[~] Masukan Posisi Anda >> ").title()

            if not posisi or posisi.isdigit():
                print("\n[!] ERROR USER INPUT")
                continue
            else:
                break
        
        while True:
            try:
                print("-"*50)
                no_tlp = int(input("\n[~] No Telephone >> "))    
                break
            except ValueError:
                print("\n[!] ERROR USER INPUT")
                continue

    karyawan_db[user_input_id] = {
        "nama":nama,
        "posisi":posisi,
        "no_tlp":no_tlp
    }

    print("-"*50)
    print(f"\n[+] DATA BERHASIL DNGAN ID: {user_input_id} BERHASIL DIINPUTKAN")

def Cek_Data():
    if not karyawan_db:
        print("-"*50)
        print("\n[-] DATA MASIH KOSONG")
        return

    while True:
        try:
            print("-"*50)
            user_input_id = int(input("\n[~] Masukan ID Yang Ingin Anda Cari >> "))
            
            if user_input_id not in karyawan_db:
                print("-"*50)
                print("\n[-] ID TIDAK DITEMUKAN")
                return

            else:
                break

        except ValueError:
            print("\n[!] ERROR INPUT USER")
            continue

    data = karyawan_db.get(user_input_id)

    print("-"*50)
    print("[+] DATA DITEMUKAN\n")
    print("="*50)
    print(f"DATA DENGAN ID: {user_input_id}")
    print(f"NAMA \t\t: {data["nama"]}")
    print(f"POSISI \t\t: {data["posisi"]}")
    print(f"TELEPON \t: {data["no_tlp"]}")
    print("="*50)


def Hapus_Data():
    if not karyawan_db:
        print("-"*50)
        print("\n[-] DATA MASIH KOSONG")
        return
    
    while True:
        try:
            user_input_id = int(input("\n Masukan ID Yang Ingin Anda Hapus >> "))

            if user_input_id not in karyawan_db:
                print("-"*50)
                print("\n[-] ID TIDAK DITEMUKAN")
                return
            
            else:
                while True:
                    print("-"*50)
                    verif = input("\n[~] Anda Yakin Ingin Menghapus Data?[Y/N] >> ").upper()

                    if verif not in ["Y", "N"]:
                        print("-"*50)
                        print("\n[!] HARAP INPUTKAN [Y/N]")
                        continue

                    elif verif == "Y":
                        del karyawan_db[user_input_id]
                        print("\n[+] DATA BERHASIL DIHAPUS")
                        return
                    else:
                        return
        except ValueError:
            print("\n[!] ERROR INPUT USER")
            continue    

def Ubah_Data():
    if not karyawan_db:
        print("-"*50)
        print("\n[-] DATA MASIH KOSONG")
        return
    
    while True:
        try:
            print("-"*50)
            user_input_id = int(input("\n[~] Masukan ID Yang Ingin Diganti >> "))

            if user_input_id not in karyawan_db:
                print("\n[-] ID TIDAK DI TEMUKAN")

            else:
                break    

        except ValueError:
            print("\n[!] ERROR INPUT USER")
            continue    
    
    while True:
        print("-"*50)
        nama = input("\n[~] Inputkan Nama Baru >> ").title()

        if not nama or nama.isdigit():
            print("-"*50)
            print("\n[!] ERROR INPUT USER")
            continue
        else:
            karyawan_db[user_input_id]["nama"] = nama
            print("-"*50)
            print("\n[+] NAMA BERHASIL DI GANTI")
            break
            
    while True:
        print("-"*50)
        posisi = input("\n[~] Inputkan Nama Baru >> ").title()

        if not posisi or posisi.isdigit():
            print("-"*50)
            print("\n[!] ERROR INPUT USER")
            continue

        else:
            karyawan_db[user_input_id]["posisi"] = posisi
            print("-"*50)
            print("\n[+] POSISI BERHASIL DI GANTI")
            break

    while True:
        try:
            print("-"*50)
            no_tlp = input("\n[~] Inputkan No Telp Baru >> ")
            karyawan_db[user_input_id]["no_tlp"] = no_tlp
            print("-"*50)
            print("\n[+] NO TELP BERHASIL DI GANTI")
            break

        except ValueError:
            print("\n[!] ERROR INPUT USER")
            continue    
    
    data = karyawan_db.get(user_input_id)
    
    print("-"*50)
    print("[+] DATA DITEMUKAN\n")
    print("="*50)
    print(f"DATA DENGAN ID: {user_input_id}")
    print(f"NAMA \t\t: {data["nama"]}")
    print(f"POSISI \t\t: {data["posisi"]}")
    print(f"TELEPON \t: {data["no_tlp"]}")
    print("="*50)

def main():
    while True:
        menu()

        while True:
            try:
                print("[~] PILIH MENU")
                user_input = int(input(">> "))
                break

            except ValueError:
                print("-"*50)
                print("\n[!] MENU TIDAK TERSEDIA")  
                continue  

        match user_input:
            case 1:
                Tambah_Data()
            case 2:
                Cek_Data()
            case 3:
                Hapus_Data()
            case 4:
                Ubah_Data()
            case _:
                print("\n[!] MENU TIDAK TERSEDIA")
                continue

        while True:
            try:
                back_to_menu = input("\n[~] Kembali ke menu? [Y/N] >> ").upper()

                if back_to_menu not in ["Y", "N"]:
                    print("-"*50)
                    raise ValueError("\n[!] HARAP INPUTKAN [Y/N]")
                
            except ValueError as e:
                print(e)

            match back_to_menu:
                case "Y":
                    break
                case "N":
                    exit()

if __name__ == "__main__":
    main()