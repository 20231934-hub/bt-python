_list = ['abc', 'xyz', 'aba', '1221', 'ii', 'ii2', '5yhy5']
n = int(input("Nhập độ dài tối thiểu: "))
dem = 0
for chuoi in _list:
    if len(chuoi) >= n and chuoi[0] == chuoi[-1]:
        dem += 1
        print(f"Thỏa mãn: {chuoi}") 
print(f"Số lượng chuỗi thỏa mãn điều kiện là: {dem}")