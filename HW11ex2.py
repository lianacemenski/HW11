class OwnError(Exception):
    pass


def calc():
    num_a = int(input("Enter number A: "))
    num_b = int(input("Enter number B: "))
    if num_b == 0:
        raise OwnError("Don't divide by zero")
    return num_a / num_b


try:
    result = calc()
except OwnError as err:
    print(err)
else:
    print(f"result = {result}")
