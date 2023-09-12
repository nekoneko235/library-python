import numpy as np


# Convert base 10 to base N number with 10 digits
def convert_base10_to_baseN(n, base, width):
    baseN = ""
    while n > 0:
        baseN = "".join([str(n % base), baseN])
        n //= base

    return baseN.zfill(width)


# Convert base 2 to base 10 number
def convert_base2_to_base10(base2):
    base10 = 0
    for i in range(len(base2)):
        base10 += int(base2[i]) * 2 ** (len(base2) - i - 1)
    return base10


# Convert base 10 to base n number by using NumPy
n = 1234
n = np.base_repr(n, 2)

# Convert base n to base 2 number by using NumPy
n = 13
n = np.binary_repr(n, 10)

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

# Add a string to the end of the string
s = "ELTE"
s = "".join([s, " University"])
