#Nhập vào nguyên a và b, nếu 1 trong 2 số a và b chia hết cho 2 thì in ra True, ngược lại in ra False
a=int(input())
b=int(input())
if a or b % 2 == 0 :
    print ("True")
else :
    print ("False")