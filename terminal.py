import os
print()
def main():
    print("Welcome to pyTerm!")
    print("Please wait while I set everything up...")
    lin = input("python: are you running Linux or Mac? (yes / no, case-sensitive)")
    if lin == "no":
        print("python: this is useless to you")
    while True:
        print()
        inp = input("$ ")
        if "pico" in inp:
            print("sorry, you cannot use arguments and parameters in pico right now :(")
            picoThis = input("File-Name? ")
            os.system('pico' +picoThis)
        elif "echo" in inp:
            print("Sorry, you cannot use arguments and parameters in echo right now :(")
            echoThis = input("Type what you want to echo: ")
            os.system('echo ' +echoThis)
        else:
            print("Sorry, this is not a command :(")
        print()
main()
