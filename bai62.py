L = list(map(int, input("Nhập vào một list số nguyên, cách nhau bằng dấu phẩy: ").split()))
cong_sai = None
if len(L) >= 2:
    cong_sai = L[1] - L[0] 
    for i in range(2, len(L)):
        if L[i] - L[i-1] != cong_sai:
            cong_sai = None
            break
print("Công sai của cấp số cộng là:", cong_sai)
