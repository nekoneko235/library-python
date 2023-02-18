# Union
s1 = {'A', 'B', 'C'}
s2 = {'C', 'D', 'E'}
s = s1.union(s2)
print(s)

# Intersection
s1 = {'A', 'B', 'C'}
s2 = {'C', 'D', 'E'}
s = s1.intersection(s2)
print(s)

# Difference
s1 = {'A', 'B', 'C'}
s2 = {'C', 'D', 'E'}

# s1 - s2
# s1 - s2 = s1 にあって s2 にないもの = A, B
s = s1.difference(s2)
print(s)

# s2 - s1
# s2 - s1 = s2 にあって s1 にないもの = D, E
s = s2.difference(s1)
print(s)

# Subset
s1 = {'A', 'B'}
s2 = {'A', 'B', 'C'}
b = s1.issubset(s2)
print(b)

# Superset
s1 = {'A', 'B', 'C'}
s2 = {'A', 'B'}
b = s1.issuperset(s2)
print(b)
