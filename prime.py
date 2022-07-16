def is_prime(number: int) -> bool:
    results = [i for i in range(2, number) if number % i == 0]

    return len(results) == 0


def run():
    print(is_prime(7))


if __name__ == "__main__":
    run()
