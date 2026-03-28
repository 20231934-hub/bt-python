import time

x = time.localtime()
year = x[0]

nam_sinh = int(input("Nhập năm sinh: "))
tuoi = year - nam_sinh

print("Tuổi của bạn là:", tuoi)