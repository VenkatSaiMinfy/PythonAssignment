def filter_even_numbers(numbers):
    temp=[]
    for i in numbers:
        if(i%2==0):
            temp.append(i)
        else:
            continue
    return temp

print(filter_even_numbers([1, 2, 3, 4, 5, 6]))
print(filter_even_numbers([1, 3, 5])) 


def merge_sorted(list1,list2):
    list3=list2+list1
    return sorted(list3)

print(merge_sorted([1, 3, 5], [2, 4, 6])) 
print(merge_sorted([1, 2, 3], [4, 5, 6]))  


def generate_matrix(n, m):
    return [[i * j for j in range(m)] for i in range(n)]

print(generate_matrix(3,3))


def transpose_matrix(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(transpose_matrix(matrix))
