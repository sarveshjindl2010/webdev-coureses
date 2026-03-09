def max_consecutive_ones(n):
    """
    Finds the length of the longest sequence of consecutive 1's 
    in the binary representation of a number using bitwise operations.
    """
    count = 0
    while n != 0:
        # This operation reduces the length of every sequence of 1s by one.
        n = (n & (n << 1))
        count += 1
    return count

# Driver code
number = 56
length = max_consecutive_ones(number)
print(f"Enter your number: {number}")
print(f"Longest consecutive 1’s length : {length}")
