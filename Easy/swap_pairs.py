def swap_pairs(numbers):
    temp=[]
    i=0
    n=len(numbers)
    while(i<n-2):
        temp.append(numbers[i+1])
        temp.append(numbers[i])
        i+=2
    if(n%2==0):
        temp.append(numbers[i+1])
        temp.append(numbers[i])
    else:
        temp.append(numbers[i])
    return tuple(temp)
numbers=tuple(map(int,input().split()))
print(swap_pairs(numbers))    