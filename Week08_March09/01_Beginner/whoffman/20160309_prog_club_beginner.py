print("To end program, use the KeyboardInterrupt keybinding\n")
try:
    while 1:
        input_str = input('Input string: ')
        output_str = ""
        for char in input_str:
            if char.isalpha():
                if char.isupper():
                    if ord(char) > 77:
                        output_str += chr(-(ord(char) - 78) % 77)
                    else:
                        output_str += chr(90 - ord(char) % 65)
                else:
                    if ord(char) > 109:
                        output_str += chr(-(ord(char) - 110) % 109)
                    else:
                        output_str += chr(122 - ord(char) % 97)
            else:
                output_str += char
        print(output_str + "\n")

except KeyboardInterrupt:
    print("\nOk you're done. I understand")
    exit(1)
