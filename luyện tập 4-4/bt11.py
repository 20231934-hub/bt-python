danh_sach = ["Python", "Hoc", "Lap", "Trinh", "AI", "Code"]
n = int(input("Nhập vào độ dài n: "))
ket_qua = []
for tu in danh_sach:
    if len(tu) > n:
        ket_qua.append(tu)
print(f"Các từ có độ dài lớn hơn {n} là: {ket_qua}")