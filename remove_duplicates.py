# def remove_duplicates(list):
#     without_duplicates = []

#     for i in list:
#         if not i in without_duplicates:
#             without_duplicates.append(i)

#     return without_duplicates


# * Altenativa con sets
def remove_duplicates(some_list):
    return list(set(some_list))


def run():
    random_list = [1, 2, 3, 4, 5, 22, 3, 1, 2, 21, 123, 421, 1, 12, 3, 4, 5]

    print(random_list)
    print(remove_duplicates(random_list))


if __name__ == "__main__":
    run()
