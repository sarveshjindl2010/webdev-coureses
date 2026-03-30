def myfunction(n):
    # --- Loop 1 ---
    # Runs from 0 to n (n+1 times)
    # Time Complexity: O(n)
    for i in range(0, n + 1):
        print("First Loop")

    # --- Loop 2 (Nested Structure) ---
    # While loop doubles j, creating O(log n) steps.
    # Inside, it runs implicitly based on n, though technically 
    # it prints "Second Loop" O(log n) times.
    # Time Complexity: O(log n)
    j = 1
    while(j <= n + 1):
        print("Second Loop ", j)
        j = j * 2

    # --- Loop 3 ---
    # Runs 100 times, independent of n.
    # Time Complexity: O(1) (Constant)
    for i in range(0, 100):
        print("Third loop")

# Overall Complexity: O(n) + O(log n) + O(1) = O(n)
# Note: If the second loop was inside the first, it would be O(n log n).
