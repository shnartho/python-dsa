
def minimum_total(triangle):
    if not triangle:
        return 0
    
    n = len(triangle)
    for row in range(n-2, -1, -1):
        for i in range(len(triangle[row])):
            triangle[row][i] += min(triangle[row+1][i], triangle[row+1][i+1])

    return triangle[0][0]

triangle = [
    [2],
    [3,4],
    [5,6,7],
    [8,9,10,11]
]

result = minimum_total(triangle)
print(result)