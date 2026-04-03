with open("demo_file1.txt", "w", encoding="utf-8") as f:
    f.write("Thuc\nhanh\nvoi\nfile\nIO\n")
with open("demo_file1.txt", "r", encoding="utf-8") as f:
    noi_dung = f.read().replace("\n", " ")
    print("In tren 1 dong:")
    print(noi_dung)
with open("demo_file1.txt", "r", encoding="utf-8") as f:
    print("In tung dong:")
    for dong in f:
        print(dong.strip())