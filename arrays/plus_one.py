# instead of   while i <= len(a)-1  made it  while i < len(a):

def plus_one_1(a):
    a.reverse()

    # print (a)

    # for each x in b add 1
    # for x in b[:]:
    #     x += 1

    i = 0
    while i < len(a):
        a[i] += 1
        if a[i] < 10:
            break
        else:
            a[i] %= 10
        i += 1

    # print(a.reverse() doesn't work'
    a.reverse()
    print(a)


def plus_one_2(a):
    a.reverse()
    result = 0
    a[0] += 1

    i = 0
    while i < len(a):
        result += a[i] * 10 ** i
        i += 1

    print(result)


plus_one_1([1, 9, 9])
plus_one_2([1, 9, 9])
