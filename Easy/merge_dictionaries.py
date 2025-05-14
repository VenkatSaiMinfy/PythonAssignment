def merge_dictionaries(dict1, dict2):
    dict3 = dict1.copy()
    dict3.update(dict2)
    return dict3

n = int(input("enter the size of dict1"))
dict1 = {}
for i in range(n):
    key = input("enter the key: ")
    value = input("enter the value")
    dict1[key] = value

n1 = int(input("enter the size of dict2"))
dict2 = {}
for i in range(n1):
    key = input("enter the key: ")
    value = input("enter the value")
    dict2[key] = value

print(merge_dictionaries(dict1, dict2))
