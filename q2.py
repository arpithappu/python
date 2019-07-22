n=int(input("enter a number:"))
sum=0
fact=1
if n>0:
   for i in range(1,n+1):
      fact*=i
      sum+=1/fact
      
print(f"result is{sum}")