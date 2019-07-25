

def sum1(num):
    res=0
    while num!=0:
        rem=num%10
        res+=rem
        num=num//10
    if res<10:
        return res
    else:
        s1=res
        s2=sum1(s1)
        return s2

num=int(input("enter the number"))
sum=sum1(num)
print(f"result={sum}")
