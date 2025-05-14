def generate_matrix(n, m):
    return [[i * j for j in range(m)] for i in range(n)]

n, m = map(int, input().split())
print(generate_matrix(n, m))
