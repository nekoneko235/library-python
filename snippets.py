# Int variable
n = int(input())

# Int variables
n, m = map(int, input().split())

# String variable
s = input()

# String variables
a, b = input().split()

# Int array
A = list(map(int, input().split()))

# String array
A = input().split()

# Int rows in array
A = [int(input()) for _ in range(n)]

# String rows in array
A = [input() for _ in range(n)]

# Int matrix
M = [list(map(int, input().split())) for _ in range(n)]

# String matrix
M = [input().split() for _ in range(n)]

# Initialize array
M = [0] * n

# Initialize matrix
M = [[0] * 4 for _ in range(4)]

# Initialize graph
G = [list() for _ in range(n)]

# Print the number with 12 decimal places
print(f"{100 / (n - 1):.12f}")
