def first_last_occurrence(search_str):
    first = None
    last = None
    with open('data.txt', 'r') as file:
        data = file.readlines()

        for i, line in enumerate(data):
            if search_str in line:
                if first is None:
                    first = i + 1
                last = i + 1
    if first and last is not None:
        print(f"first occurrence of {search_str} is on line: {first}")
        print(f"Last occurrence of {search_str} is on line: {last}")
    else:
        print(f"{search_str} is not found in the file..")


search_str = input("Enter the search item: ")
first_last_occurrence(search_str)
