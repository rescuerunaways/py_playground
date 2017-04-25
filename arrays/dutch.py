# if x is bigger than a pivot, swap


def dutch(a, i):
    gr = []
    lt = []

    # for idx, val in enumerate(a):
    #     print(idx, val)
    #
    # for index in enumerate(a, start=3):
    #     print(index)

    def stepDown(n):
        while n > 1:
            yield n
            n = n / 2

    for i in stepDown(n):
        print(i)

    index = 0

    for idx, val in enumerate(a):
        print(idx, val)
        index = idx + 1








        # for i in range(len(a)):
        #     print(i)


        # for x in a:
        #     if x > i:
        #         # how to move all elements which are smaller than
        #         a[a.index(i)], a[a.index(x)] = a[a.index(x)], a[a.index(i)]
        #
        #         # a.remove(x)
        #
        # print('array:', a)


dutch([1, 4, 0, 5, 2, 7, 3, 5, 6, 7, 8], 3)

# print(a[0:len(a)])

# read: https://codeandchaos.wordpress.com/2014/11/15/swap-two-objects-in-python/
# a[0], a[3] = a[3], a[0]

# print(a[0:len(a)])
# print(a[0:index])
# print(a[index+1:len(a)])
#
# print(a[::-1])  # what does the third element in slicing mean?
