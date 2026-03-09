def find_all_substrings(s):
    substrings = []
    n = len(s)
    # Outer loop for the starting index
    for i in range(n):
        # Inner loop for the ending index (j+1 to include the last character)
        for j in range(i, n):
            substrings.append(s[i:j+1])
    return substrings

# Example usage:
input_string = "anki"
all_substrings = find_all_substrings(input_string)
print(f"Substrings of '{input_string}': {all_substrings}")
