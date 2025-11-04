#Given the string "I love Python", print it in reverse without using [::-1].
a = "I love Python"
rev = ""
for char in a:
    rev = char + rev
print(rev)