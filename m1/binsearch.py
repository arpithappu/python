class Stack:

    def __init__(self):
        self.st=[]

    def push(self,ele):
        self.st.append(ele)

    def pop(self):
        if self.is_empty():
            print("stack is emplty")
        else:
            ele=self.st.pop()
            print(f"element {ele} is removed from the stack")

    def search(self,searchEle):
        if self.is_empty():
            print("search is not possible")
        else:
            for index,ele in enumerate(self.st):
                if ele==searchEle:
                    return index

    def show(self):
        if self.is_empty():
            print("stack is emplty")
        else:
            print("elements of stacka are:")
            print(self.st)

    def is_empty(self):
        return len(self.st)==0
    
if __name__=="__main__":
    st=Stack()
    while True:
        print("1.Push 2.Pop 3.Search 4.Display 5.Exit")
        try:
            ch=int(input("enter your choice:"))
            if ch==1:
                ele=int(input("enter a element to push:"))
                st.push(ele)
            elif ch==2:
                st.pop()
            elif ch==3:
                ele=int(input("enter a element to search:"))
                res=st.search(ele)
                if res!=1:
                    print(f"elemet {ele} found at location {res}")
                else:
                    print("element not found")
            elif ch==4:
                st.show()
            else:
                break
        except(ValueError,KeyError):
            print("enter only number 1 to 5")