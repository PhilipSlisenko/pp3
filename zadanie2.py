from random import randint


lst1 = [randint(0, 9) for i in range(10)]
lst2 = [randint(0, 9) for i in range(10)]
lst3 = [lst1[i] + lst2[i] for i in range(len(lst1))]
print(lst1)
print(lst2)
print(lst3)
