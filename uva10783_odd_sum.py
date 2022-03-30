def cal(a,b): #計算a到b 的所有奇數總和
    #若a,b皆為奇數則a  為首項 b為末項
    #若a偶b奇      a+1      b
    #若a偶b偶      a+1      b-1
    #若a奇b偶      a        b-1
    if a % 2 == 0:
        a0 = a + 1
    else:
        a0 = a
    if b % 2 == 0:
        an = b - 1
    else:
        an = b
    numOfa0toan = (an-a0)//2 + 1
    return ((a0+an)*(numOfa0toan))//2
    
T = int(input())
count = T
case = 1
while count >= 1:
    a = int(input())
    b = int(input())

    s = "Case " + str(case) + ": " + str(cal(a,b))
    print(s)
    count -= 1
    case += 1
