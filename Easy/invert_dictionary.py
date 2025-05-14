def invert_dictionary(d):
    inverted = dict()
    for key, value in d.items():
        if value in inverted:
            inverted[value].append(key)
        else:
            inverted[value] = [key] 
    return inverted

numbers = dict()
n = int(input("Enter the len of dict: "))
for i in range(n):
    key = input("Enter the key: ")
    value = int(input("Enter the value: "))
    numbers[key] = value

print( invert_dictionary(numbers))