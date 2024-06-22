import random
import string

def generate_captcha(length=5):
    # Define the character set (A-Z, a-z, 0-9)
    characters = string.ascii_letters + string.digits
    # Generate a random CAPTCHA
    captcha = ''.join(random.choices(characters, k=length))
    return captcha

captcha = generate_captcha()
print("Generated CAPTCHA:", captcha)
