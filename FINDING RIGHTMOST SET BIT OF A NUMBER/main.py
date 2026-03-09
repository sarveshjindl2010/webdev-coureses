def rightmost_set_bit_position(n: int) -> int:
   if n == 0:
       return -1 # No set bits
   isolated_bit = n & -n # Isolate rightmost set bit
   position = (isolated_bit.bit_length() - 1) + 1 # Convert to 1-based index
   return position
# Test
print(rightmost_set_bit_position(18)) # Binary: 10010 → Output: 2
print(rightmost_set_bit_position(19)) # Binary: 10011 → Output: 1