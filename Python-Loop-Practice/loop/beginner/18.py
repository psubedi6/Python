#Count vowels in a string using a loop.
c= input("Enter the character: ")
count=0
for i in c:
    if i in "aeiouAEIOU":
        count=count+1
print(count)