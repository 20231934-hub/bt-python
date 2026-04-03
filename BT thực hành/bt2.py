ten_file = input("Nhap ten file: ")
with open(ten_file, "w", encoding="utf-8") as f:
    van_ban = input("Nhap doan van ban: ")
    f.write(van_ban)
with open(ten_file, "r", encoding="utf-8") as f:
    print("Noi dung file:")
    print(f.read())