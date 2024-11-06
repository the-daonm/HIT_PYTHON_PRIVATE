import random


def generate_samples(num_samples):
    y = [random.uniform(0, 10) for _ in range(num_samples)]
    y_hat = [random.uniform(0, 10) for _ in range(num_samples)]
    return y, y_hat


def mae(y, y_hat):
    return sum(abs(y_i - y_hat_i) for y_i, y_hat_i in zip(y, y_hat)) / len(y)


def mse(y, y_hat):
    return sum((y_i - y_hat_i) ** 2 for y_i, y_hat_i in zip(y, y_hat)) / len(y)


def rmse(y, y_hat):
    return mse(y, y_hat) ** 0.5


def huber_loss(y, y_hat, delta=0.5):
    loss = 0
    for y_i, y_hat_i in zip(y, y_hat):
        error = abs(y_i - y_hat_i)
        if error <= delta:
            loss += 0.5 * (y_i - y_hat_i) ** 2
        else:
            loss += delta * error - 0.5 * delta ** 2
    return loss / len(y)


def main():
    try:
        num_samples = int(input(">> Input number of samples (positive integer number) which are generated: "))
        if num_samples <= 0:
            print("number of samples must be a positive integer number")
            return
    except ValueError:
        print("number of samples must be a positive integer number")
        return

    loss_name = input("Input loss name: ")
    if loss_name not in {"MAE", "MSE", "RMSE", "Huber_Loss"}:
        print(f"{loss_name} loss is not supported")
        return

    y, y_hat = generate_samples(num_samples)

    if len(y) != num_samples or len(y_hat) != num_samples:
        print("The number of samples is incorrect")
        return

    print("target:", y)
    print("predict:", y_hat)

    if loss_name == "MAE":
        result = mae(y, y_hat)
    elif loss_name == "MSE":
        result = mse(y, y_hat)
    elif loss_name == "RMSE":
        result = rmse(y, y_hat)
    elif loss_name == "Huber_Loss":
        result = huber_loss(y, y_hat)

    print(f"{loss_name}: {result}")

main()




