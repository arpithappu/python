c=[1,2,3,4]
f=[2,5,6,7,9]
b=[5,6,8,2,4,]
players=[]
players.extend(c)
players.extend(f)
players.extend(b)
u_name=[]
for name in players:
    if name in u_name:
        pass
    else:
        u_name.append(name)
print(u_name)
