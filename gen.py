import random
list=[]
for i in range(1,21):
    list.append(random.randint(1,50))
print(list)
res=[max(list),min(list)]
print(res)