def merge_sorted(list1,list2):
    list3=list2+list1
    return sorted(list3)
list1=list(map(int,input("enter the numbers").split()))
list2=list(map(int,input("enter the numbers").split()))
print(merge_sorted(list1,list2))