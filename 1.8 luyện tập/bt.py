code = {'a': '!', 'b': '@', 'c': '#', 'd': '$'}
decode = {v: k for k, v in code.items()}
def ma_hoa(text):
    result = ""
    for ch in text:
        if ch in code:
            result += code[ch]
        else:
            result += ch  
    return result
def giai_ma(text):
    result = ""
    for ch in text:
        if ch in decode:
            result += decode[ch]
        else:
            result += ch
    return result
s = "abcd xyz"
mahoa = ma_hoa(s)
giaima = giai_ma(mahoa)
print("Chuoi goc:", s)
print("Ma hoa:", mahoa)
print("Giai ma:", giaima)