L = list(map(int, input().split()))
x = int(input("Nhập vào số nguyên x: "))
gia_tri_xa_nhat = None
khoang_cach_xa_nhat = float('inf')
for so in L:
    khoang_cach = abs(so - x)
    if khoang_cach < khoang_cach_xa_nhat:
        khoang_cach_xa_nhat = khoang_cach
        gia_tri_xa_nhat = so
print("Giá trị trong list xa x nhất là:", gia_tri_xa_nhat)