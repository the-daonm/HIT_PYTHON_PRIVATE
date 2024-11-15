input_dict = eval(input("key: value cach nhau boi ','"))

def swap_dict(d):
    try:
        if len(set(d.values())) != len(d.values()):
            return None
        return {v: k for k, v in d.items()}
    except TypeError:
        print("Khong the lam key (e.g., list, dict).")
        return None

swapped_dict = swap_dict(input_dict)

if swapped_dict is None:
    print("Khong the")
else:
    print(swapped_dict)
