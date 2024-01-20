L = list(map(int, input().split()))
vi_tri_thoa_man = -1
for i in range(1, len(L) - 1):
    if L[i] == L[i-1] * L[i+1]:
        vi_tri_thoa_man = i
        break
print("Vị trí thỏa mãn điều kiện là:", vi_tri_thoa_man)