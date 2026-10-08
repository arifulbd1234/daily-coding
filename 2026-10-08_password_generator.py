# Day 2 - 2026-10-08
# Tool: Strong Password Generator
# What it does: Creates a random strong password using letters, numbers
# and symbols, with a chosen length.
# Useful for: Everyone - safer passwords for any online account,
# instead of reusing weak or easy-to-guess passwords.

import random
import string


def generate_password(length=12, use_symbols=True):
    if length < 4:
        raise ValueError("Password length should be at least 4")
    chars = string.ascii_letters + string.digits
    if use_symbols:
        chars += "!@#$%^&*()-_=+"
    # Guarantee at least one of each main type
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
    ]
    if use_symbols:
        password.append(random.choice("!@#$%^&*()-_=+"))
    password += [random.choice(chars) for _ in range(length - len(password))]
    random.shuffle(password)
    return "".join(password)


if __name__ == "__main__":
    print(generate_password())            # 12 characters, with symbols
    print(generate_password(16))          # 16 characters, with symbols
    print(generate_password(10, False))   # 10 characters, no symbols
