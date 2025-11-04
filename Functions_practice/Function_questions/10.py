#Write a function increment() that has a local variable counter initialized to 0 and increments it by 1 each time it is called. Observe whether the value persists across function calls.
def increment():
    global b
    b = b+1
    return b
b=0 
print(increment())
print(increment())
print(increment())