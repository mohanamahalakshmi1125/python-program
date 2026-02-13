import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

def groovingMonkeys(arr):
    n = len(arr)
    visited = [False]*n
    answer = 1

    for i in range(n):
        if not visited[i]:
            count = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = arr[j] - 1   # because monkeys start from 1
                count += 1
            answer = lcm(answer, count)

    return answer

# Example
moves = [2,3,1,5,4]
print("Time =", groovingMonkeys(moves))
