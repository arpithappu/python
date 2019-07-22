n=int(input("enter a number:"))
sum=0
if n>0:
   for i in range(1,n+1):
      sum+=1/i
      
print(f"result is{sum}")