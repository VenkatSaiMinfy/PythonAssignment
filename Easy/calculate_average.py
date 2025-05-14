def calculate_average(numbers):
    sum=0
    n=len(numbers)
    if(n==0):
        return 0
    for i in numbers:
        sum+=i
    return (sum/n)
numbers=list(map(int,(input("Enter the numbers").split())))
print(calculate_average(numbers))