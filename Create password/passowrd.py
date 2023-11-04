import random
import string

# Define the length of the password
password_length = 15

# Define the characters to use in the password
password_characters = string.ascii_letters + string.digits + string.punctuation

# Generate the password
password = ''.join(random.choice(password_characters) for i in range(password_length))

# Print the password to the console
print("Your random password is:", password)
