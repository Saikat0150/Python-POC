def first_last_capitalized(given_str):
    final = []
    for item in given_str.split(' '):
        if len(item) == 1:
            final.append(item.upper())
        else:
            x = item[0].upper() + item[1:-1] + item[-1].upper()
            final.append(x)
    final = " ".join(final)
    return final


def first_capitalized(given_str):
    final = []
    for item in given_str.split(' '):
        # x = item[0].upper() + item[1:]
        # final.append(x)
        final.append(item.capitalize())
    final = " ".join(final)
    return final


given_str = "i am saikat mondal"
print(first_last_capitalized(given_str))
print(first_capitalized(given_str))
