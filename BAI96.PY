so_nhap_vao = int(input("Nhập vào một số nguyên dương: "))

if so_nhap_vao <= 0:
    print("Vui lòng nhập số nguyên dương lớn hơn 0.")
else:
    tong_uoc_so = 1
    for i in range(2, int(so_nhap_vao**0.5) + 1):
        if so_nhap_vao % i == 0:
            tong_uoc_so += i
            if i != so_nhap_vao // i:
                tong_uoc_so += so_nhap_vao // i
    so_ban_be = []
    for j in range(1, so_nhap_vao):
        tong_uoc_so_j = 1
        for k in range(2, int(j**0.5) + 1):
            if j % k == 0:
                tong_uoc_so_j += k
                if k != j // k:
                    tong_uoc_so_j += j // k
        if tong_uoc_so_j == so_nhap_vao and j != so_nhap_vao:
            so_ban_be.append(j)
    print(f"Số bạn vừa nhập có {len(so_ban_be)} số bạn bè là: {so_ban_be}")
