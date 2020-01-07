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
        inp = input("pyTerm-0.2 $ ")
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
        elif "ls" in inp:
            lsWhat = input("Type in the folder to view (. for current): ")
            os.system("ls "+lsWhat)
        elif "calc" in inp:
            print("This is not a Linux/Unix command but...")
            calcWhat = int(input("First number?"))
            print("Available operators: + - * / ^ (power)")
            o = input("Choose one: ")
            if o == "*":
                calcWhat2 = int(input("Second number? "))
                print(calcWhat2 * calcWhat)
            elif o == "/":
                cW2 = int(input("2nd number?"))
                try:
                    print(calcWhat / cW2)
                except:
                    print("Error in maths. Check that your equation is possible.")
            elif o == "-":
                cW2 = int(input("2nd number?"))
                print(calcWhat - cW2)
            elif o == "+":
                cW2 = int(input("2nd number?? "))
                print(calcWhat + cW2)
            elif o == "^":
                pwr = int(input("To the power of what? "))
                print(calcWhat ** pwr)
            else:
                print("Unknown operator: "+o)
        else:
            os.system(inp)
        print()
main()
