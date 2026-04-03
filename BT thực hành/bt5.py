with open("demo_file2.txt", "r", encoding="utf-8") as f:
    data = f.read()
words = data.split()
count = {}
for w in words:
    if w in count:
        count[w] += 1
    else:
        count[w] = 1
print(count)