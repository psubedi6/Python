#Remove all vowels from the string "Hello World".
a="Hello World"
vowels = "aeiouAEIOU"
result= "".join([char for char in a if char not in vowels])
print(result)