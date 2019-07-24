n=int(input("enter anumber"))
sum=0
if n>0:
    for i in range(1,n+1):
        sum+=1/(i*i*i)

print(f"result:{sum}")