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

print(swap_pairs((1, 2, 3, 4)))
print(swap_pairs((1, 2, 3))) 

def get_stats(numbers):
    temp=[]
    temp.append(min(numbers))
    temp.append(max(numbers))
    temp.append(sum(numbers))
    temp.append(sum(numbers)/len(numbers))
    return temp

print(get_stats([1, 2, 3, 4, 5])) 


from collections import namedtuple

Student = namedtuple("Student", ["name", "age", "grades"])

def top_student(students):
    return max(students, key=lambda s: sum(s.grades) / len(s.grades))


alice = Student("Alice", 20, (85, 90, 95))
bob = Student("Bob", 19, (70, 80, 90))
charlie = Student("Charlie", 21, (90, 92, 93))

print(top_student([alice, bob, charlie]))  # Should return the charlie Student tuple

def count_coordinate_occurrences(coords):
    count = {}
    for coord in coords:
        count[coord] = count.get(coord, 0) + 1
    return count


coords = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4), (1, 2)]
print(count_coordinate_occurrences(coords))
