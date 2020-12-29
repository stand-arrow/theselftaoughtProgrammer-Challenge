#線形探索

def ls(number_list, n):
    found = False
    for i in number_list:
        if i == n:
            found = True
            return found
    return found

numbers = range(0, 100)
s1 = ls(numbers, 2)
print(s1)
s2 = ls(numbers, 102)
print(s2)