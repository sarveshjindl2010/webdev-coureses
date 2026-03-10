def list_sum(arr):
   total = 0 # O(1)
   for x in arr: # Loop runs n times
       total += x # O(1) each iteration
   return total
# Sum of all elements in an n x m matrix
for i in range(n):
   for j in range(n):
       total += matrix[i][j]
# Complexity: O(n*m)
def example(n):
   for i in range(n): # O(n)
       for j in range(n): # O(n)
           print(i, j) # O(1)