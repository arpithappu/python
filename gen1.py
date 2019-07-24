import random
list=[]
for i in range(1,100):
    list.append(random.randint(1,1000))
print(list)
for i in list:
    if i%3==0 and i%6==0 and i%9!=0:
        print(i) 