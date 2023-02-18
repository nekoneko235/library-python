"""
リストをN個ずつの要素に分割する
[list型変数[idx:idx + n] for in range(0, len(list型変数), n)]
"""

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3
res = [lst[i:i+n] for i in range(0, len(lst), n)]
print(res)
