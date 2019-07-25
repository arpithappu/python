
tab = {"mon":[3,2,2],"tue":[3,2,2],"wed":[3,2,2],"thu":[3,2,1],"fri":[3,2,1],"sat":[3,1,0],"sun":[0,0,0]}
print(tab)
inp = input("enter the day:")
for key,val in tab.items():
    if inp == key:
        print(val)
