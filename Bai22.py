#Nhập điểm toán, văn, anh.
""" Nếu điểm đúng quy tắc (trong khoảng từ 0 - 10), ta tính điểm trung bình rồi tiến hành xét:
Nếu điểm trung bình lớn hơn hoặc bằng 8, toán hoặc văn lớn hơn hoặc bằng 8 và không có điểm nào dưới 6.5 thì in ra “Học sinh giỏi”
Nếu không đủ điều kiện học sinh giỏi ta xét nếu điểm trung bình lớn hơn hoặc bằng 6.5, toán hoặc văn lớn hơn hoặc bằng 6.5 và không có điểm nào dưới 5 thì in ra “Học sinh khá”
Nếu không đủ điều kiện học sinh khá ta xét nếu điểm trung bình lớn hơn hoặc bằng 5, toán hoặc văn lớn hơn hoặc bằng 5 và không có điểm nào dưới 3.5 thì in ra “Học sinh trung bình”
Nếu không đủ điều kiện học sinh trung bình ta xét nếu điểm trung bình lớn hơn hoặc bằng 3.5, toán hoặc văn lớn hơn hoặc bằng 3.5 và không có điểm nào dưới 2 thì in ra “Học sinh yếu”
Nếu không đủ điều kiện học sinh yếu ta in ra “Học sinh kém”"""
diemtoan = float(input())
diemvan = float(input())
diemanh = float(input())
diemtb = (diemtoan+diemvan+diemanh)/3
if diemtb >= 8 and diemtoan >=6.5 and diemvan >=6.5 and diemanh >=6.5:
    print ("Học sinh giỏi")
elif diemtb >= 6.5 and diemtoan >=5 and diemvan >=5 and diemanh >=5:
    print ("Học sinh khá ")
elif diemtb >= 5 and diemtoan >=3.5 and diemvan >=3.5 and diemanh >=3.5:
    print ("Học sinh trung bình ")
else :
    print ("Học sinh Kém")