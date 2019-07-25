num=int(input("enter a number"))
temp = num
rev=0
while num!=0:
    rem=num % 10
    num=num // 10
    rev=rev * 10 +rem
  
print(f"reverse of{temp} is {rev}")