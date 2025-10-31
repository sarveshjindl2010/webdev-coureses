def binary_to_decimal():
    binary = input("Enter a binary number: ")
    
    if not all(bit in '01' for bit in binary):
        print("Error: Please enter a valid binary number (containing only 0s and 1s)")
        return
    
    decimal = 0
    power = 0
    
    for digit in reversed(binary):
        if digit == '1':
            decimal += 2 ** power
        power += 1
    
    print(f"The decimal equivalent of binary {binary} is: {decimal}")

if __name__ == "__main__":
    binary_to_decimal()