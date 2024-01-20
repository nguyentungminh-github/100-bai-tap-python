L = list(map(int, input("Nhập vào một list số nguyên, cách nhau bằng dấu phẩy: ").split()))
la_list_dang_song = True
n = len(L)
for i in range(1, n-1):
    if not (L[i-1] < L[i] > L[i+1] or L[i-1] > L[i] < L[i+1]):
        la_list_dang_song = False
        break
print(la_list_dang_song)