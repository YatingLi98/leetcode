def isValid(s):
    dictionary = {'(': 1, ')': 10, '[': 2, ']': 20, '{': 3, '}': 30}
    need = []
    for char in s:
        c = dictionary[char]
        if c < 10:
            need.append(c)
        else:
            if len(need) == 0 or need.pop() * 10 != c:
                return False
    if len(need) == 0:
        return True
    return False

s = "}"
print(isValid(s))
