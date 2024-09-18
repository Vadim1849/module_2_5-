def get_matrix(n, m, value):
    matrix = []
    if m <=0 or value <=0:
        return matrix
    for i in range(n):
        strings = []
        matrix.append(strings)
        for j in range(m):
            strings.append(value)
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
result4 = get_matrix(0, 2, 10)  # Примечания: со значением 0 или меньше, будет возвращаться пустой список
result5 = get_matrix(3, 0, 42)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
