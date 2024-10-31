import math


def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


def binary(x):
    if x < 0:
        return 0
    else:
        return 1


def sigmoid(x):
    return 1 / (1 + math.e ** (-x))


def elu(x, alp=0.01):
    if x < 0:
        return alp * (math.e ** x - 1)
    else:
        return x


while True:
    x = input(">> Input x = ")
    if is_number(x):
        x = float(x)
        break
    else:
        print("x must be a number.")

activation_functions = {
    'binary': binary,
    'sigmoid': sigmoid,
    'elu': elu
}

while True:
    func = input("Input activation Function ( binary | sigmoid | elu ) : ").lower()
    if func not in activation_functions:
        print(f"{func} is not supported.")
    else:
        res = activation_functions[func](x)
        print(f"{func} : f({x}) = {res}")
        break
