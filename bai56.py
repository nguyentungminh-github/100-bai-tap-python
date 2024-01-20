def tim_gia_tri_duong_dau_tien(lst):
    for so in lst:
        if so > 0:
            return so
    return -1
list_so_nguyen = list(map(int,input().split()))
ket_qua = tim_gia_tri_duong_dau_tien(list_so_nguyen)

print("Giá trị dương đầu tiên của list là:", ket_qua)