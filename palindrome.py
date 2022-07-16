def is_palindrome(text: str) -> bool:
    text = text.replace(" ", "").lower()
    return text == text[::-1]


def main():
    user_input = input("Ingresa una palabra para saber si es un palíndromo: ")

    if is_palindrome(user_input):
        print("Si es un palíndromo")
    else:
        print("No es un palíndromo")


if __name__ == "__main__":
    main()
