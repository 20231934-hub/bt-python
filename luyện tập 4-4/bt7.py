lst = ['abc', 'xyz', 'abc', '12', 'ii', '12', '5a']
new1 = []
for x in lst:
    if lst.count(x) == 1:
        new1.append(x)

print("Ket qua cach 1:", new1)
new2 = []
for x in lst:
    if x not in new2:
        new2.append(x)
print("Ket qua cach 2:", new2)