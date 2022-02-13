


def process(str, key):
    res = []
    for char in str:
        if char.isalpha():
            start = 97 if char.islower() else 65
            diff = ord(char) - start
            shift = (diff + key) % 26
            res.append(chr(start + shift))
        else:
            res.append(char)
    return ''.join(res)

def parseString(str):
    lastSpaceIndex = str.rfind(" ")
    if lastSpaceIndex == -1:
        return (0,0)
    else:
        data = str[:lastSpaceIndex]
        key = str[lastSpaceIndex + 1:]
        return (data, key)

def shiftCode():
    error = 0
    while True:
        if not error:
            command = input("1) Make a code\n2) Decode a message\n3) Quit\n\nEnter your selection: ")
        if command == "3":
            print("\nBye!\n")
            break
        elif command == "1" or command == "2":
            str = input("Enter text to encode followed by a number: ").rstrip()
            data, key = parseString(str)
            error = not data or not key.isnumeric()
            if error:
                print("Incorrect format. Enter text followed by a number.")
            elif command == "1":
                print("\nText encoded:")
                print(process(data, int(key)))
                error = 0
            elif command == "2":
                print("\nText decoded:")
                print(process(data, int(key) * -1))
                error = 0
        else:
            print("Enter an option number: 1, 2, 3\n")
        

if __name__ == "__main__":
    shiftCode()