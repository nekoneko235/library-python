import random

l1 = [0, 1, 2, 3, 4]
l2 = random.sample(l1, len(l1))
print(l2)

l1 = [0, 1, 2, 3, 4]
random.shuffle(l1)
print(l1)
