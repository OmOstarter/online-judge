v1.0
while True:
    try:
        x = int(input())
    except EOFError:
        break
    a = ""
    if x < 0:
        break
    elif x == 0:
        print(x)
    else: # x > 0 
        while x > 0: 
            a = str(x%3) + a
            x = x // 3
    print(a)
# 0 -> 0
# 1 -> 1
# 2 -> 2
# 3 -> 10
# 4 -> 11
# 5 -> 12
# 6 -> 20
# x = a_n * 3^n + a_n-1 * 3^n-1 + 3^n-2 + .... + a_0 3^0
# a_n 介於 1~2 之間
# a_n-1 ~ a_0 介於0~2之間
# a_0 = x % 3
# a_1 = (x // 3) % 3
