import re


def first_last_occurrence(search_str):
    with open('data.txt', 'r') as file:
        data = file.readlines()

    occurrences = [i + 1 for i, line in enumerate(data) if re.search(search_str, line)]

    if occurrences:
        print(f"First occurrence of {search_str} is on line: {occurrences[0]}")
        print(f"Last occurrence of {search_str} is on line: {occurrences[-1]}")
    else:
        print(f"{search_str} is not found in the file..")


search_str = input("Enter the search item: ")
first_last_occurrence(search_str)
