
from functools import reduce
list=[1,2,3,4,5,6,7,8,9]
res=reduce(lambda a,b:a+b,list)
print(res)
