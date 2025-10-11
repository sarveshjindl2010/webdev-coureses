def multiply_one_iteration(a, b):
  return a * b

# Function using N iterations (linear time)
# This function multiplies two numbers by repeatedly adding one number
# to itself N times, where N is the value of the other number.
# This implementation assumes b is non-negative.
def multiply_n_iterations(a, b):
  if b < 0:
    a, b = -a, -b  # Handle negative numbers
    
  result = 0
  for _ in range(b):
    result += a
  return result

# Example usage
a = 5
b = 6

print(f"Enter 'a' for a*b: {a}")
print(f"Enter 'b' for a*b: {b}")

print(f"1 iteration: {multiply_one_iteration(a, b)}")
print(f"N iteration: {multiply_n_iterations(a, b)}")