data = [
    "name=Alice;age=30;score=85.5",
    "name=Bob;age =25;score=90",
    "name=Alice;age=30;score=92",
    "city=NewYork;name=Eve;age =35;score=88",
    "city=London;name=Alice;age=30;score=85.5",
]

dict = {}

for x in data:
    pairs = x.split(";")
    for pair in pairs:
        key, value = pair.split("=")

    dict[key].append(value)


result_dict = {}

for key, values in dict.items():
    unique_count = len(set(values))

    numeric_values = [v for v in values if isinstance(v, (int, float))]
    max_value = max(numeric_values) if numeric_values else None

    string_values = [v for v in values if isinstance(v, str)]
    max_length = max((len(v) for v in string_values), default=None)

    result_dict[key] = {
        "unique_count": unique_count,
        "max_value": max_value,
        "max_length": max_length,
    }

print(f"dict = {dict}")
print(f"result_dict = {result_dict}")
