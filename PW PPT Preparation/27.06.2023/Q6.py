<<<<<<< HEAD
def singleNumber(nums):
    result = 0

    for num in nums:
        result ^= num

    return result
nums = [2, 2, 1]
=======
def singleNumber(nums):
    result = 0

    for num in nums:
        result ^= num

    return result
nums = [2, 2, 1]
>>>>>>> 7caea318e86370ce5b856e0aaf2784353e6ad797
print(singleNumber(nums))  # Output: 1