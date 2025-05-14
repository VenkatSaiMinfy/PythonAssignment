def filter_even_numbers(numbers):
    temp=[]
    for i in numbers:
        if(i%2==0):
            temp.append(i)
        else:
            continue
    return temp
numbers=list(map(int,input("enter the numbers").split()))
print(filter_even_numbers(numbers))