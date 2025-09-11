import random
import string


def password_generator():
    print("🔑 Welcome to the Password Generator!")

    try:
        length = int(input("Enter the desired password length: "))
        if length < 4:
            print("⚠️ Password length should be at least 4.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for _ in range(length))

        print(f"✅ Your generated password is: {password}")
    except ValueError:
        print("⚠️ Please enter a valid number.")


password_generator()
