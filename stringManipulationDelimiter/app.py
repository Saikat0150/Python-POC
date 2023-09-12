def string_manipulation(given_str):
    final_dict = {}
    for item in given_str.split('@'):
        item = item.strip().split('-')
        if len(item) == 3:
            final_dict[f"{item[0]}-{item[1]}"] = item[2]
    print(final_dict)


given_str = '@abc-test-zero @empty-test-one @new-test-two @full-test-three'
string_manipulation(given_str)
