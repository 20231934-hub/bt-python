ten = input("Nhap ten: ")
tuoi = input("Nhap tuoi: ")
email = input("Nhap email: ")
skype = input("Nhap skype: ")
dia_chi = input("Nhap dia chi: ")
noi_lam_viec = input("Nhap noi lam viec: ")
with open("setInfo.txt", "w", encoding="utf-8") as f:
    f.write(ten + "\n")
    f.write(tuoi + "\n")
    f.write(email + "\n")
    f.write(skype + "\n")
    f.write(dia_chi + "\n")
    f.write(noi_lam_viec + "\n")
print("Da luu file setInfo.txt")
print("\nNoi dung file:")
with open("setInfo.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())