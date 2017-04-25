def binary_search(a, n):
    def recurse(a, n):
        mid_point = len(a) // 2
        # print (a[0:mid_point])
        if n < a[mid_point]:
            # how to define a slice in an array?
            return recurse(a[:mid_point], n)
        elif n > a[mid_point]:
            return recurse(a[mid_point:], n)
        elif a[mid_point] == n:
            return 'hit'
        else:
            # miss doesn't work
            return 'miss'

    return recurse(a, n)


# hit:
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 8))
# miss:
# print(binary_search([1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12], 8))
