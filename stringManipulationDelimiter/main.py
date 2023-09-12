def string_manipulation(given_str):
    str_after = given_str.split('@')
    # str_after = [s.strip() for s in given_str.split('@')]
    final_list = [elem for elem in str_after if elem.strip()]
    final_dict = {}
    for items in final_list:
        item = items.split('-')
        join_item = item[0] + '-' + item[1]
        final_dict.update({join_item: item[2]})
        
    print(final_dict)


given_str = '@abc-test-zero @empty-test-one @new-test-two @full-test-three'
string_manipulation(given_str)
