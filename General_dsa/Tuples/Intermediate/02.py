#Unpack the tuple person = ("Alice", 25, "Engineer") into separate variables and print them.
person = ("Alice", 25, "Engineer")
name, age, profession = person
print("name: ", name)
print("age: ", age)
print("profession: ",profession )

person = ("Alice", 25, "Engineer", "NY", "USA", "Python Developer")
for i in range (len(person)):
    print(f"Element{i} is: {person[i]}")