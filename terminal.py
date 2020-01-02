import os
import time
print()
def main():
    print("Welcome to pyTerm!")
    print("==============================IMPORTANT!==============================")
    print("There is **LITTLE TO NO INTERACTIVITY** for commands apart from the ones programmed into this program.")
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
            os.system('pico ' +picoThis)
        if "echo" in inp:
            print("Sorry, you cannot use arguments and parameters in echo right now :(")
            echoThis = input("Type what you want to echo: ")
            os.system('echo ' +echoThis)
        if "rm -Rf" in inp:
            print("Sorry, you cannot use arguments and Parameters in rm right now")
            deleteThis = input("Type what you want to delete: ")
            os.system('rm -Rf ' +deleteThis)
            print("Completed")
        elif "python" in inp:
            pyThis = input("")
        else:
            os.system(inp)
        print()
main()
