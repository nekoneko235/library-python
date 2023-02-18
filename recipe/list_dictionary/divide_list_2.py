"""
リストをN分割したい
[list型変数[idx:idx + size] for idx in range(0, len(list型変数), size)]
"""

import math

lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3
size = math.ceil(len(lst1)/n)
lst2 = [lst1[i:i+size] for i in range(0, len(lst1), size)]
print(lst2)
