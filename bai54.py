"""Nhập vào một list số nguyên L, nhập vào 2 số nguyên dương a và b (a < b < len(L))
Tìm và in ra số nhỏ nhất trong list từ vị trí a đến vị trí b"""
L = list(map(int,input().split()))
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b (a < b): "))
if not (0 <= a < b < len(L)):
    print("Vui lòng nhập lại số nguyên dương a và b sao cho a < b < len(L)")
else:
    so_nho_nhat = min(L[a:b+1])
    print(f"Số nhỏ nhất trong đoạn từ vị trí {a} đến vị trí {b} là: {so_nho_nhat}")