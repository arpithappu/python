list=[]
def add (ele):
    list.append(ele)
 
def pop():
    if len(list)==0:
        print("list empty")
    else:
        ele=list.pop()
        print(f"element {ele} removed")

def search(ele):
    if len(list)==0:
        print("list empty")
    else:
        if ele in list:
            index=list.index(ele)
            print(f"element {ele} found at {index}")

def display():
    if len(list)==0:
        print("list empty")
    else:
        for i in list:
            print(i)
    
while True:
    print("\n**1.add 2.delete 3.search 4.display 5.exit**")
    ch=int(input("enter the choice:"))
    if ch==1:
        ele=int(input("enter the element to add:"))
        add(ele)
    elif ch==2:
        pop()
    elif ch==3:
        ele=int(input("enter the element to search:"))
        search(ele)
    elif ch==4:
        display()
    else:
        print("thank you...")
        break


    