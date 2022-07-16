# def make_division_of(n1):
#     def division(n2):
#         return n1 / n2

#     return division


def make_repeater_of(n: int):
    def repeater(text: str):
        return text * n

    return repeater


if __name__ == "__main__":
    repeater = make_repeater_of(2)
    print(repeater("hola"))
