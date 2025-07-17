#Assignment 1
#user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
fav_number = int(input("Enter your favorite number: "))

# Calculations
future_age = age + 10
square_fav = fav_number ** 2

# Display 
print("--- User Information ---")
print(f"Name:" ,name)
print(f"Current Age:",age)
print(f"Age in 10 Years:",future_age)
print(f"Favorite Number:",fav_number)
print(f"Square of Favorite Number:",square_fav)