def minimumAbsDifference(arr):
    arr = sorted(arr)
    mini = abs(arr[0] - arr[1])
    dictionary = {}
    for i in range(len(arr) - 1):
        dis = arr[i+1] - arr[i]
        if dis in dictionary:
            dictionary[dis].append([arr[i], arr[i+1]])
        else:
            dictionary[dis] = [[arr[i], arr[i+1]]]
        mini = min(mini, dis)

    return [element for element in dictionary[mini]]

arr1 = [1,3,6,10,15]
print(minimumAbsDifference(arr1))

arr = [3,8,-10,23,19,-4,-14,27]
print(minimumAbsDifference(arr))
