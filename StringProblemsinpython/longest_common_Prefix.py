def longest_common_Prefix(given_list):
    c_pre = ''
    i = 0
    while i < len(given_list)-1:
        c_pre1 = ''
        for ci in range(len(given_list[i])):
            if given_list[i][ci] == given_list[i + 1][ci]:
                c_pre1 += given_list[i][ci]
            else:
                i += 1
                if len(c_pre) == 0:
                    c_pre = c_pre1
                elif len(c_pre) > len(c_pre1):
                    c_pre = c_pre1
                break

    print(c_pre)


def longest_common_prefix_minimize(given_list):
    c_pre = given_list[0]
    for item in given_list[1:]:
        i = 0
        while i < len(c_pre) and i < len(item) and c_pre[i] == item[i]:
            i += 1
        c_pre = c_pre[:i]
    print(c_pre)


given_list = ["apple", "apricot", "apartment"]
longest_common_Prefix(given_list)
longest_common_prefix_minimize(given_list)
