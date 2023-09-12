def caesar_cipher(main_str, switch_by):
    final = ''
    for char in main_str:
        final += chr(ord(char) + switch_by)
    print(final)


main_str = input("Enter the string you want to coded: ")
switch_by = int(input("Enter the number you want to shift for encrypting: "))
caesar_cipher(main_str, switch_by)
