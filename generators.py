import time


# def fibo_gen(max=None):
#     a, b = 0, 1
#     counter = 0

#     while True:
#         if max != None and counter >= max:
#             raise StopIteration

#         if counter == 0:
#             counter += 1
#             yield a

#         if counter == 1:
#             counter += 1
#             yield b

#         counter += 1
#         result = a + b
#         a, b = b, result
#         yield result

# COMPACT VERSION
def fibo_gen(max=None):
    a, b, counter = 0, 1, 0

    while not max or counter < max:
        yield a
        a, b, counter = b, a + b, counter + 1


def run():
    fibonacci = fibo_gen()

    for i in fibonacci:
        print(i)
        time.sleep(1)


if __name__ == "__main__":
    run()
