def letterCombinations(digits):
    dictionary = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                  '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['u', 'v', 'w'], '9': ['x', 'y', 'z']}
    result = [""]
    if digits == "":
        return []
    for num in digits:
        curr = result.copy()
        result = []
        for c in dictionary[num]:
            result += [s + c for s in curr]

    return result


digits = "23"
print(letterCombinations(digits))
