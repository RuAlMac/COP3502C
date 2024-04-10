# Lab 9 Document
# Encode and __main__ code written by Russell MacGregor
# Decode code writted by Robert Giasson

def encode(string):
    inList = list(string)

    for i in range(len(inList)):
        inList[i] = int(inList[i])
        inList[i] = (inList[i] + 3) % 10
        inList[i] = str(inList[i])

    outString = ''.join(inList)
    return outString


def decode(string):
    num = str(string)
    code = 0
    counter = 1
    for i in range(len(num) - 1, -1, -1):
        code += ((int(num[i]) + 7) % 10) * counter
        counter *= 10

    return str(code)


def printMenu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()

    option = int(input("Please enter an option: "))
    return option


if __name__ == '__main__':
    encoded = 0
    while (1):
        option = printMenu()

        match option:
            case 1:
                toEncode = input("Please enter your password to encode: ")
                encoded = encode(toEncode)
                print("Your password has been encoded and stored!")
                print(encoded)
            case 2:
                decoded = decode(encoded)
                print(f"The encoded password is {encoded}, and the original password is {decoded}.")
            case 3:
                break

        print()
