def calculate_average(numbers):
    sum=0
    n=len(numbers)
    if(n==0):
        return 0
    for i in numbers:
        sum+=i
    return (sum/n)
print(calculate_average([5,10,15,20]))
print(calculate_average([]))


def greetuser(name,message="Hello"):
    return message+" "+name
print(greetuser("venkat"))
print(greetuser("sai","hi"))



def calculate_total(*prices, discount=0):
    total = sum(prices)
    total -= total * (discount / 100)
    return total


print(calculate_total(10, 20, 30)) 
print(calculate_total(10, 20, 30, discount=10))


def create_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)
print(double(5))
print(triple(5))  

