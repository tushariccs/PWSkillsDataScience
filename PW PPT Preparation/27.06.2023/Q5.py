def plusOne(digits):
    n = len(digits)

    # Start from the rightmost digit
    for i in range(n - 1, -1, -1):
        digits[i] += 1

        if digits[i] == 10:
            digits[i] = 0
        else:
            # No carry left, return the digits array
            return digits

    # If there is a carry left, insert it at the beginning of the array
    digits.insert(0, 1)
    return digits
digits = [1, 2, 3]
print(plusOne(digits))  # Output: [1, 2, 4]