import re


def is_polindrome(s):
    # iterate through string like though array

    # i didn't guess about 2 while loops(tried to do something with continue/break)
    # i didn't guess about while loop condition!!!! and what does intersection mean
    # incorrect: while i< len(s)  and j > 0:
    # i was also shy about thinking that i can possibly increase the index in 2 places;

    # the idea that everything inside outer while loop - just conditions to break,
    # if none of them are satisfied - return TRUE

    # try without preprocessing:
    # break and if
    i = 0
    j = len(s) - 1

    while i < j:
        while (not re.match("[a-z]", s[i].lower()) and i < j):
            i += 1
        while (not re.match("[a-z]", s[j].lower()) and i < j):
            j -= 1

        if not s[i].lower() == s[j].lower(): return False
        i += 1
        j -= 1

    return True
    # how to identify that two indices crossed?
    # how to skip non alphabetic symbols???


# google: while statements with break/continue in if branch;
# break and continue statements can appear anywhere inside the
# while (or for) loop’s body, but they are usually coded further
# nested in an if test to take action in response to some condition.


print(is_polindrome("A man, a plan, a canal, Panama"))
# print("Ray a Ray")
