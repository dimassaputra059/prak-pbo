# Latihan 1

print("Latihan 1")
n = int(input("Masukkan panjang dan lebar : "))

for i in range(n):
    print("*" * n)

# Latihan 2

print("\nLatihan 2")

for i in range(3):
    username = str(input("Username anda : "))
    password = int(input("Password anda : "))
    if username == "informatika" and password == 12345678:
        print("Berhasil login!")
        break
    elif i == 2:
        print("Akun diblokir")
    else:
        print("Username atau password salah coba lagi\n")
