data="Rajesh,Krish,manoj,suresh,Anu,Anish,Anush,kavya"
names=data.upper().split(",")
print(names)
list=[]
for name in names:
    if name.startswith("A") or name.endswith("H"):
        list.append(name)
list.sort()
print(list)