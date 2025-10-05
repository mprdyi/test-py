

import sys

# Data akun sederhana (username: [pin, saldo])
accounts = {
    "user1": ["1234", 1_000_000],
    "user2": ["4321", 500_000]
}

def login():
    print("=== SELAMAT DATANG DI ATM CLI ===")
    username = input("Masukkan username: ")
    pin = input("Masukkan PIN: ")

    if username in accounts and accounts[username][0] == pin:
        print("Login berhasil!\n")
        return username
    else:
        print("Login gagal! Username atau PIN salah.")
        return None

def menu(username):
    while True:
        print("\n=== MENU ATM ===")
        print("1. Cek Saldo")
        print("2. Tarik Tunai")
        print("3. Setor Tunai")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            print(f"Saldo anda: Rp {accounts[username][1]:,}")

        elif pilihan == "2":
            jumlah = int(input("Masukkan jumlah tarik tunai: Rp "))
            if jumlah <= accounts[username][1]:
                accounts[username][1] -= jumlah
                print(f"Berhasil tarik Rp {jumlah:,}. Saldo sekarang: Rp {accounts[username][1]:,}")
            else:
                print("Saldo tidak cukup!")

        elif pilihan == "3":
            jumlah = int(input("Masukkan jumlah setor tunai: Rp "))
            accounts[username][1] += jumlah
            print(f"Berhasil setor Rp {jumlah:,}. Saldo sekarang: Rp {accounts[username][1]:,}")

        elif pilihan == "4":
            print("Terima kasih telah menggunakan ATM CLI!")
            sys.exit()
        else:
            print("Pilihan tidak valid!")

def main():
    user = None
    while not user:
        user = login()
    menu(user)

if __name__ == "__main__":
    main()
