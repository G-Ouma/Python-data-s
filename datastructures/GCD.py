def euclidGCD(a, b):
    # Ensure that a >= b
    if a < b:
        a, b = b, a

    # Euclidean algorithmto find GCD
    while b != 0:
        a, b = b, a % b
    
    return a

def gcdList(n):
    gcdResult = n[0]
    for num in n[1:]:
        gcdResult = euclidGCD(gcdResult, num)
    
    return gcdResult

numberList = [24, 56, 48, 60]
print("The GCD of", numberList, "is:", gcdList(numberList))