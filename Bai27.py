h = int(input())
for i in range (1,h):
    for j in range (1,i+1):
        print("*",end=" ")
    print()
k = int(input())
for i in range(1, k+1):
    for j in range(1, k+1-i):
        print("", end = " ")
    for t in range(1, i+1):
        print("*", end=" ")
    print()

