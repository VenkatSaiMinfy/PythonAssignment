import math
def get_stats(numbers):
    temp=[]
    temp.append(min(numbers))
    temp.append(max(numbers))
    temp.append(sum(numbers))
    temp.append(sum(numbers)/len(numbers))
    return temp
numbers=tuple(map(int,input().split()))
print(get_stats(numbers))