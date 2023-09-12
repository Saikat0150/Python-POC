import copy


'''def combine_list1(list1, list2):
    max_index = max(item['Index'] for item in list1)

    for item in list2:
        item['Index'] += max_index

    combine_list = list1 + list2

    return combine_list'''


def combine_lists(list1, list2):
    list2_copy = copy.deepcopy(list2)
    max_index = max(item['Index'] for item in list1)

    for item in list2_copy:
        item['Index'] += max_index

    combine_list = list1 + list2_copy

    return combine_list


list1 = [{'Index': 1, 'Message': 'msg1'}, {'Index': 2, 'Message': 'msg2'}]

list2 = [{'Index': 1, 'Message': 'msg3'}, {'Index': 2, 'Message': 'msg4'}, {'Index': 3, 'Message': 'msg5'}]

print(f"List1 = {list1}")
print(f"List2 = {list2}")
print(f"Output List = {combine_lists(list1, list2)}")
print(f"List2 after combine = {list2}")
