import random
import string
def generate_password(length):
    """Generate a random password of a given length."""
    # The password will be composed of printable ascii characters
    chars = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password of the given length
    password = ''.join(random.choice(chars) for i in range(length))
    return password
def main():
    # Get the length of the password from the user
    length = int(input("Enter the length of the password: "))
    # Generate a random password of the given length
    password = generate_password(length)
    # Print the generated password
    print("Your password is:", password)
if __name__ == "__main__":
    main()
