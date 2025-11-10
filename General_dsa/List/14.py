#Write a program that merges two dictionaries into one.
dict_1={
    "name": "Prakash",
    "school":"algoma",
    "course":"computer"
}
dict_2={
    "rollno": 24,
    "year":"second"
}
dict_1.update(dict_2)
print(dict_1)