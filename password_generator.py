import secrets
import string


def generate_password(length=16):
    """Generate a secure random password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(characters) for _ in range(length))


def main():
    print("=== Password Generator ===")

    try:
        length = int(input("Password length: "))

        if length < 4:
            print("Length must be at least 4.")
            return

        password = generate_password(length)

        print(f"\nGenerated password:\n{password}")

    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()
