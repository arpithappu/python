names=["pkm","aln","pvr","pkm","aln","gln","ivr","pvr","km","vp","cs","mcs"]
c_names={}
for name in names:
    if c_names.get(name)==None:
        c_names[name]=1
    else:
        c_names[name]+=1
print(c_names)