def valid(email):
    at = email.find('@')
    dot = email.rfind('.')

    if at != -1 and dot != -1 and at < dot:
        if dot - at > 1:
            return "Valid"

    return "Invalid"


s = input()

print(valid(s))
