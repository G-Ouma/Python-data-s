def fibList(n):
    f = [0, 1] # initializing the first 2 numbers in the sequence
    for i in range(2, n):
        f.append(f[i - 1] + f[i - 2]) # Appending the calculated number in the list
    return f[n - 1] # returning the desired number, taking note that indexing begins at 0

def printfibList(n):
    f_n = fibList(n)
    digits = str(n)
    if digits[-2:] in ['11', '12', '13']:
        print(f'The {n}th Fibonacci number is: {f_n:,}')
    elif digits[-1] == '1':
        print(f'The {n}st Fibonacci number is: {f_n:,}')
    elif digits[-1] == '2':
        print(f'The {n}nd Fibonacci number is: {f_n:,}')
    elif digits[-1] == '3':
        print(f'The {n}rd Fibonacci number is: {f_n:,}')
    else:
        print(f'The {n}th Fibonacci number is: {f_n:,}')

printfibList(23)