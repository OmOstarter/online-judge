# 20220331 v1.0
while True:
    try:
        n = int(input())
    except EOFError:
        break
    if n == 0:
        break
    a = str(n)
    lenOfa = len(a)
    odd=0
    even=0
    for i in range(0,lenOfa,2):
        odd += int(a[i])
    for i in range(1,lenOfa,2):
        even += int(a[i])
    if (odd -even) %11 ==0:
        s=str(n)+" is a multiple of 11."
    else:
        s=str(n)+" is not a multiple of 11."
    print(s)
# 若一個數是11的倍數，那它的奇數項減偶數項也會是11的倍數。
