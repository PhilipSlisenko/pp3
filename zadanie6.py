def mediana(lst):
    n = len(lst)
    if n % 2 == 1:
        return sorted(lst)[n//2]
    else:
        return sum(sorted(lst)[n//2-1:n//2+1])/2.0


def dominanta(lst):
    return max(set(lst), key=lst.count)


lst = [2, 3, 5, 2, 9, 8, 1, 3, 9, 1, 1, 4, 7, 7, 1, 4]
print("Mediana = ", mediana(lst))
print("Dominanta = ", dominanta(lst))
