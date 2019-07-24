
import random as rn

def prime(num):
    if num<2:
        return False
    else:
        for i in range (2,num//2+1):
            if num%i==0:
                return False
        return True

nums=[rn.randint(1,100) for i in range(1,20)]
nums=[i for  i in range(1,201)]
list=list(filter(prime,nums))
print(list)
