def find_ak(k):
    if k == 1 or k == 2 or k == 3:
        return 1
    a = [1, 1, 1]
    for i in range(4, k + 1):
        a.append(a[i - 1] + a[i - 3])
    return a[k - 1]
k = int(input())
result = find_ak(k)
print(f"Gia tri a[{k}] trong day la: {result}")
