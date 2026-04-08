import random

print("PASSWORD GENERATOR")

length=int(input("Enter the length of password:"))

letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbols="@#$%&*!"

all_characters=letters+numbers+symbols

password = ""

for i in range(length):
    random_character=random.choice(all_characters)
    password=password+random_character

print("Generated Password:",password)
print("Password created successfully.")