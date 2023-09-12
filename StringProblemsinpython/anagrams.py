def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        return False

    char_count = {}
    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1

    for char in str2:
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1

    return True


def anagrams(str1, str2):
    str1 = str1.replace(" ", "").upper()
    str2 = str2.replace(" ", "").upper()

    if len(str1) != len(str2):
        return "The strings are not anagram...."

    char_count = {}

    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1

    for char in str2:
        if char not in char_count or char_count[char] == 0:
            return "The strings are not anagram..."
        char_count[char] -= 1

    return "The strings are anagrams..."


# Test the function
input1 = input("Enter the first string: ")
input2 = input("Enter the second string: ")
print(are_anagrams(input1, input2))
print(anagrams(input1, input2))

