#Nhập vào số nguyên a, nếu a là số chia hết cho 5 nhưng KHÔNG nằm trong khoảng từ 20 - 70 thì in ra True, ngược lại in ra False
a=int(input())
if a>=20 and a<=70 :
    print ("False")
elif a % 5 == 0 :
    print ("True ")
else :
    print ("False")