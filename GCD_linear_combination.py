def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0  # gcd, x, y
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y
input_list=list(map(int,input("please type all element in the same line.").split()))
coefficient=[]
gcd=input_list[0]
for i in input_list:
    gcd, x, y=extended_gcd(gcd,i)
    coefficient=[a*x for a in coefficient]
    coefficient.append(y)
print(f"GCD of {', '.join(map(str,input_list))} is {gcd}")
print("GCD linear combination is",end='')
for i, (a, b) in enumerate(zip(coefficient, input_list)):
    if i > 0:  # 從第二個元素開始，前面要加上 + 或 - 符號
        if a > 0:
            print(f"+ {a} * {b} ", end='')
        else:
            print(f"- {abs(a)} * {b} ", end='')
    else:
        print(f" {a} * {b} ", end='')
print(f"= {gcd}")