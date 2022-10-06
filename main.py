import numpy as np

def login():
    arr_user = np.array = ([["admin", "admin123", "admin"], ["user", "user123", "user"]])

    print("\n" "*** LOGIN ACCOUNT****" "\n")
    username = input("Username : " "\t")
    password = input("Password : " "\t")

    test = bool
    while test:
        for x in arr_user:
            if username == x[0] and password == x[1] and x[2] == "admin":
                print("\n" + "*** Welcome to Teacher is Admin ***")
                admin()
                break
            elif username == x[0] and password == x[1] and x[2] == "user":
                print("\n" + "*** Welcome to User ***")
                user()
                break
    return test


def admin():
    min = input("\n"
                "1. Input Nilai \n"
                "2. Read Siswa \n"
                "3. Hapus \n"
                "4. Logout \n"
                "5. Edit \n"
                "Masukkan Inputan: ")

    if min == "1":
        create()

    elif min == "2":
        read()
        admin()

    elif min == "3":
        read()
        dlt = int(input("pilih Barang yang ingin dihapus: "))
        delete(hapus, dlt)

    elif min == "4":
        login()

    elif min == "5":
        read()
        up = int(input("Pilih yang ingin diupdate: "))
        update(upt, up)


def create():
    name = input("\nMasukkan Nama : ")
    uts = input("\nMasukkan UTS : ")
    uas = input("\nMasukkan UAS : ")
    hasil = (float(uts) + float(uas)) / 2

    if name and uts and uas:
        arr_data.insert(0, ["{ " + "Nama : " + name, "Uts : " + uts, "Uas : " + uas + ", Hasil : " + format(hasil) + " }"])
        read()
    else:
        print("Data kosong")
        login()


def read():
    print("")
    no = 0
    for i in arr_data:
        print("ID : ", no, ". ",i)
        no += 1

# Delete ---------------------
def hapus(dlt):
    s = 0
    if s >= len(arr_data[0]):
        print("Tidak ada")
        user()
    else:
        del arr_data[dlt]
    sukses()

def sukses():
    print("Berhasil di hapus")
    admin()

def delete(x, y):
    return x(y)

# Edit ---------------------
def update(x, y):
    return x(y)

def upt(up):
    x = 0

    if x >= len(arr_data[0]):
        print("Tidak ada")
        admin()
    else:
        print("Edit Data Siswa & Nilai")
        name = input("\nMasukkan Edit Nama : ")
        uts = input("\nMasukkan Edit UTS : ")
        uas = input("\nMasukkan Edit UAS : ")
        hasil = (float(uts) + float(uas)) / 2

        for i in range(len(arr_data)):
            if arr_data.pop(up)[0][up]:
                if name and uts and uas:
                    arr_data.append("['{ " + "Nama : " + name + "', 'Uts : " + uts + "', 'Uas : " + uas + ", Hasil : " + format(hasil) + " }']")
                    read()
                    admin()



# -----------USER
def user():
    ser = input("\n"
                "1. Info Nilai \n"
                "2. Logout \n"
                "Masukkan Inputan: ")
    if ser == "1":
        read()
    elif ser == "2":
        login()




arr_data = np.array = []
login()



