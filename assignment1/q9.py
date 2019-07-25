num=int(input("Enter the 5 digit number:"))
n=5
sum=0
while n > 0:
    n-=1
    res=num // 10 ** (n)
    if res==9:
        res =0
    else:
        res +=1
    res *= 10 ** (n)
    sum += res
    num=num % 10 ** (n)
  
    
print(sum)