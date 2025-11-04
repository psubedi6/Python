#Write a function multiply(a, b) that has a proper docstring explaining what it does. Then use help(multiply) to display the docstring.
def multiply(a,b):
    '''
    Returns the sum of two numbers
    a(int):The first number
    b(int):The second number

    Returns:
    int:The multiplication of two number
    '''
    return a*b

print(multiply.__doc__)