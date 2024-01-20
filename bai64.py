L = list(map(int, input("Nhập vào một list số nguyên, cách nhau bằng dấu phẩy: ").split()))
la_list_chan_le = True
for i in range(len(L)):
    for j in range(i+1, len(L)):
        if (L[i] + L[j]) % 2 == 0:
            la_list_chan_le = False
            break
if la_list_chan_le:
    print("Là list chẵn lẻ.")
else:
    print("Không phải là list chẵn lẻ.")
