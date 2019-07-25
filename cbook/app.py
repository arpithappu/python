from memory import InMemoryImpl
while True:
    print("*"*75)
    print("1.Add 2.View All 3.Update 4.Delete 5.Search 6.Exit")
    print("*"*75)
    ch=int(input("enter your choice:"))
    if ch == 1:
        InMemoryImpl.addContact()
    elif ch == 2:
        InMemoryImpl.viewContact()
    elif ch == 3:
        InMemoryImpl.updateContact()   
    elif ch == 4:
        InMemoryImpl.deleteContact() 
    elif ch == 5:
        InMemoryImpl.search()
    else:
        break