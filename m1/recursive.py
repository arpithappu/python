def binarySearch(lst,l,h,key):
    if l<=h:
        mid=(l+h)//2
        if key==lst[mid]:
            return mid
        elif key>lst[mid]:
            return binarySearch(lst,mid+1,h,key)
        else:
            return binarySearch(lst,l,mid-1,key)
    return -1

ele=6
res=binarySearch([1,2,3,4,5,6,7,8],0,7,ele)
if res==-1:
    print(f"{ele} not found")
else:
    print(f"{ele} is found at:{res}")