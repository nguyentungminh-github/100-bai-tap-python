def dem_gia_tri_lon_nhat(L):
    dem = 0
    max_value = float('-inf')
    for gia_tri in L:
        if gia_tri > max_value:
            max_value = gia_tri
            dem += 1
    return dem
danh_sach_so_nguyen = [int(x) for x in input("Nhập vào danh sách số nguyên, cách nhau bằng dấu cách: ").split()]
ket_qua = dem_gia_tri_lon_nhat(danh_sach_so_nguyen)
print(f"Số lượng giá trị lớn hơn tất cả giá trị đứng trước nó là: {ket_qua}")
