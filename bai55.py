def Kiemtra(L):
    Gia_tri = L[0]
    return all(x == Gia_tri for x in L)
L = list(map(int,input().split()))
print(Kiemtra(L))