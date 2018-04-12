"""annabelle"""

def main():
    while True:
        name = str(input("Please enter your name:"))
        if name == "":
            print("Invalid name")
        else:
            print(name[1::2])
            break


main()
