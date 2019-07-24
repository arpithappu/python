from functools import reduce
lst=[1,2,3,4,5,6,7,8,9]
x=list(map(lambda x:x**2,lst))
y=list(filter(lambda x:x%2==0,x))
z=reduce(lambda a,b:a+b,y)
print(f"sum of squares of even numbers {z}")