import random
import string


def generate_password(length=12):
    # Define the character set to use for the password
    chars = string.ascii_letters + string.digits

    # Generate the password using random characters
    password = ''.join(random.choice(chars) for _ in range(length))

    return password
password = generate_password()
print(password)