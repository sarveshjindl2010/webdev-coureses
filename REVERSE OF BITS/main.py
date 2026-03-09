def reverse_bits(n):
   result = 0
   while n > 0:
       # Shift result left to make space for the next bit
       result <<= 1
       # Add the least significant bit of n to result
       result |= n & 1
       # Shift n right to process the next bit
       n >>= 1
   return result
# Test case
number = 11 # Binary: 1011
print(reverse_bits(number)) # Output: 13 (Binary: 1101)