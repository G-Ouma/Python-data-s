def josephus_formula(n, k):
    position = 0
    # Iterate over each person in the circle
    for i in range(1, n + 1):
        # Calculate new position after eliminating kth person, taking modulus n
        position = (position + k) % i
    # Return survivor's position (1-based indexing)
    return position + 1

# Example usage:
n = 5
k = 2
last_survivor = josephus_formula(n, k)
print("Position of the last survivor (mathematical formula):", last_survivor)
