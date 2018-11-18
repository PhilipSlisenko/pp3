def sumaTablicy(tablica):
    sum = 0
    for i in tablica:
        if not isinstance(i, list):
            sum += i
        else:
            sum += sumaTablicy(i)
    return sum


lst = [7, 5, [3, 6, [2]], 7, [1, [2, 3, [4]], 9, 2], 4]
print(sumaTablicy(lst))
