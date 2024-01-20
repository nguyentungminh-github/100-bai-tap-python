L = list(map(int, input("Nhập vào một list số nguyên, cách nhau bằng dấu phẩy: ").split()))
if L == sorted(L):
    print(True)
else:
    print(False)