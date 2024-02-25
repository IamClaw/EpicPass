import random
import string

def generate_strong_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(12))
    return password

# Example usage:
strong_password = generate_strong_password()
print(strong_password)

