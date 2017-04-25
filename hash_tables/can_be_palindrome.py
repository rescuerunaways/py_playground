def can_be_polindrome(s):
    i = 0
    m = {}
    while i < len(s):
        if s[i] in m.keys():
            m[s[i]] += 1
        else:
            m[s[i]] = 1
        i += 1

    odds = 0

    for key in m:
        if m[key] % 2 == 1:
            odds += 1
        if odds > 1:
            return False

    return True


print(can_be_polindrome("edified"))
print(can_be_polindrome("edified1"))

# python 3:
# how to work with dictionaries:
# standart python dictionaries unordered, so accessing value by index doesn't make much sense
# if you know what you are doing, use : m.values[i]

# doesn't work as TypeError: 'dict_values' object does not support indexing
# doesn't work: if m.values()[j] % 2 == 1:
# doesn't work: if m.values[j] % 2 == 1:
