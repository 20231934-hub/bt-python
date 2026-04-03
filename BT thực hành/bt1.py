ten_file = input("Nhap ten file: ")
n = int(input("Nhap so dong can doc: "))

with open(ten_file, "r", encoding="utf-8") as f:
    for i in range(n):
        dong = f.readline()
        if not dong:
            break
        print(dong.strip())