chuoi_a = input("Chuỗi a: ")
chuoi_b = input("Chuỗi b: ")
list_a = list(chuoi_a)
list_b = list(chuoi_b)
while list_b in list_a:
    list_a.remove(list_b)
chuoi_a = ''.join(list_a)
print("Sau khi xóa, chuỗi a:", chuoi_a)