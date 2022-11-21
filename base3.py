num=int(input())
val1 = '-' if num<0 else ''
num = abs(num)
if num < 3:
    print(str(num))
val2 = ''
while num != 0:
    val2 = str(num%3) + val2
    num = num//3
print(val1+val2)

