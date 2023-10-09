from prettytable import PrettyTable

# Data user dan admin
user_data = {"Arajen": {"password": "JiilanTillDie", "saldo": 1000}}
admin_data = {"Admin": {"password": "qwerty"}}

# Data Nendoroid
nendoroid_data = {
    "Nendoroid Kobo Kanaeru": {"harga": 200, "deskripsi": "Action Figure nendoroid dari karakter Vtuber"},
    "Nendoroid Sukuna": {"harga": 300, "deskripsi": "Ini nih, karakter yang berhasil bikin mokad mas mas Saikyou Dakara"},
    "Nendoroid Kirito": {"harga": 400, "deskripsi": "Im Beater, Beta Tester Cheater"}
}

# Fungsi login user
def user_login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    if username in user_data and user_data[username]["password"] == password:
        return username
    else:
        print("Login gagal. Username atau password salah.")
        return None

# Fungsi login admin
def admin_login():
    username = input("Masukkan username admin: ")
    password = input("Masukkan password admin: ")
    if username in admin_data and admin_data[username]["password"] == password:
        return username
    else:
        print("Login admin gagal. Username atau password salah.")
        return None

# Fungsi top up saldo
def top_up_balance(username):
    try:
        amount = int(input("Masukkan jumlah saldo yang ingin ditambahkan: "))
        user_data[username]["saldo"] += amount
        print(f"Saldo Anda sekarang: {user_data[username]['saldo']}")
    except ValueError:
        print("Jumlah saldo harus berupa angka.")

# Fungsi tampilan menu untuk user
def user_menu(username):
    while True:
        print("\nMenu User:")
        print("1. Lihat Nendoroid")
        print("2. Top Up Saldo")
        print("3. Keluar")
        choice = input("Pilih menu: ")
        if choice == "1":
            display_nendoroid_pretty()
            buy_nendoroid(username)
        elif choice == "2":
            top_up_balance(username)
        elif choice == "3":
            break
        else:
            print("Pilihan tidak valid.")

# Fungsi tampilan menu untuk admin
def admin_menu():
    while True:
        print("\nMenu Admin:")
        print("1. Tambah Nendoroid")
        print("2. Lihat Nendoroid")
        print("3. Keluar")
        choice = input("Pilih menu: ")
        if choice == "1":
            add_nendoroid()
        elif choice == "2":
            display_nendoroid_pretty()
        elif choice == "3":
            break
        else:
            print("Pilihan tidak valid.")

# Fungsi menampilkan Nendoroid dalam format Pretty Table
def display_nendoroid_pretty():
    nendoroid_table = PrettyTable()
    nendoroid_table.field_names = ["Nama Nendoroid", "Harga", "Deskripsi"]
    for nendoroid_name, nendoroid_info in nendoroid_data.items():
        nendoroid_table.add_row([nendoroid_name, nendoroid_info["harga"], nendoroid_info["deskripsi"]])
    print(nendoroid_table)

# Fungsi penambahan Nendoroid oleh admin
def add_nendoroid():
    nendoroid_name = input("Masukkan nama Nendoroid: ")
    nendoroid_price = input("Masukkan harga Nendoroid: ")
    nendoroid_description = input("Masukkan deskripsi Nendoroid: ")
    nendoroid_data[nendoroid_name] = {"harga": int(nendoroid_price), "deskripsi": nendoroid_description}
    print(f"Nendoroid {nendoroid_name} telah ditambahkan.")

# Fungsi pembelian Nendoroid
def buy_nendoroid(username):
    nendoroid_name = input("Masukkan nama Nendoroid yang ingin dibeli: ")
    if nendoroid_name in nendoroid_data:
        nendoroid_price = nendoroid_data[nendoroid_name]["harga"]
        if user_data[username]["saldo"] >= nendoroid_price:
            user_data[username]["saldo"] -= nendoroid_price
            print(f"Selamat! Anda telah membeli {nendoroid_name}. Saldo Anda sekarang: {user_data[username]['saldo']}")
        else:
            print("Saldo tidak mencukupi untuk membeli Nendoroid ini.")
    else:
        print("Nendoroid tidak ditemukan.")

# Program utama
while True:
    print("\nSelamat datang di Toko Nendoroid")
    print("1. Login User")
    print("2. Login Admin")
    print("3. Keluar")
    choice = input("Pilih menu: ")
    if choice == "1":
        username = user_login()
        if username:
            user_menu(username)
    elif choice == "2":
        admin_username = admin_login()
        if admin_username:
            admin_menu()
    elif choice == "3":
        break
    else:
        print("Pilihan tidak valid.")
