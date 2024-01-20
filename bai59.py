L = list(map(int, input().split()))
if len(L) == 0:
    print("Danh sách rỗng. Không có giá trị trung bình.")
else:
    gia_tri_trung_binh = sum(L) / len(L)
    print("Giá trị trung bình của list là:", gia_tri_trung_binh)