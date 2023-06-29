<<<<<<< HEAD
def findMissingRanges(nums, lower, upper):
    result = []
    start = lower

    for num in nums:
        if num > start:
            result.append(getRange(start, num - 1))
        start = num + 1

    if start <= upper:
        result.append(getRange(start, upper))

    return result
def getRange(start, end):
    if start == end:
        return str(start)
    else:
        return str(start) + "->" + str(end)
nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(findMissingRanges(nums, lower, upper))  # Output: [[2,2],[4,49],[51,74],[76,99]]
=======
def findMissingRanges(nums, lower, upper):
    result = []
    start = lower

    for num in nums:
        if num > start:
            result.append(getRange(start, num - 1))
        start = num + 1

    if start <= upper:
        result.append(getRange(start, upper))

    return result
def getRange(start, end):
    if start == end:
        return str(start)
    else:
        return str(start) + "->" + str(end)
nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(findMissingRanges(nums, lower, upper))  # Output: [[2,2],[4,49],[51,74],[76,99]]
>>>>>>> 7caea318e86370ce5b856e0aaf2784353e6ad797
