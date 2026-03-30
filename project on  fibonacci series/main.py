def fibonacci_series(nterms):
    """
    Prints the Fibonacci series up to nterms terms.
    """
    n1, n2 = 0, 1
    count = 0

    # Check if the number of terms is valid
    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print("Fibonacci sequence up to", nterms, ":")
        print(n1)
    else:
        print("Fibonacci sequence:")
        while count < nterms:
            print(n1, end=' ')
            # Update values for the next iteration
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
        print() # for a new line at the end

# Example usage:
number_of_terms = int(input("Enter how many Fibonacci numbers to print: "))
fibonacci_series(number_of_terms)
