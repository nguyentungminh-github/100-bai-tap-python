L = input()
ky_tu_so = []
ky_tu_chu = []
for chu in L:
    if chu.isalpha():
        ky_tu_chu.append(chu)
        ky_tu_so.append("-")
    elif chu.isnumeric():
        ky_tu_so.append(chu)
        ky_tu_chu.append("-")
print(''.join(ky_tu_chu))
print(''.join(ky_tu_so))