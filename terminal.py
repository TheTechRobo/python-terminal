import os
print()
def main():
    print("Welcome to pyTerm!")
    print("Please wait while I set everything up...")
    while True:
        print()
        inp = input("$ ")
        if inp == "pico":
            os.system('pico')
        else:
            print("Sorry, this is not a command :(")
