# File not found
# with open ("a_file.txt") as file:
#     file.read()

# Key Error
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# Index Error (Nothing at 3)
# fruit_list = ["apple", "banana", "pear"]
# fruit = fruit_list[3]

# Type Error
# text = "abc"
# print(text + 5)


# try:
# Do something that might cause an exception

# except:
# Do this if there was an exception

# else:
# Do this if there were no exceptions

# finally:
# Do this no matter what happens


#Exception Handling

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    raise TypeError("This is an error that I made up.")

#BMI Example

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)


