username = input("write your username here: ")
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
numbers = "123456789"
uppercase_count = 0
lowercase_count = 0
numbers_count = 0

for letter in username:
    if letter in uppercase:
        uppercase_count = uppercase_count + 1
    elif letter in lowercase:
        lowercase_count = lowercase_count + 1
    elif letter in numbers:
        numbers_count = numberscount +1

print("amount of uppercase:", uppercase_count)
print("amount of lowercase:", lowercase_count)