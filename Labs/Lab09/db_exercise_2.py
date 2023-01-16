def greet():
    name: str = read_name()
    greeting = 'Hello ' + name
    return greeting


def read_name():
    val = str(input("What is your name? "))
    return val


if __name__ == "__main__":
    result_var = greet()
    print(result_var)
