#Ngày vào ngày, tháng. #Hãy tính và in ra xem ngày nhập vào cách ngày đầu năm bao nhiêu ngày (giả sư năm đó không phải là năm nhuận)
thang = int(input("Nhập tháng"))
ngay = int(input("Nhập ngày "))
while True : 
    if thang < 31 :
        print ("Nhập lỗi")
        break 
    elif thang in 1 or 3 or 5 or 7 or 8 or 10 or 12:
        if ngay > 31 :
            print ("Nhập Lỗi")
            break 
    elif thang == 4 or 6 or 9 or 11:
        if ngay > 30 :
            print ("Nhập Lỗi")
            break 
    elif thang in [2]:
        if ngay > 28 :
            print ("Nhập Lỗi")
            break 
    else :
        ngay_dau = 1 
        khoang_cach = ngay - ngay_dau
        print (khoang_cach)
        break 