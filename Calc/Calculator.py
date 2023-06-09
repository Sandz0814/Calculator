import time
import os

def clear():
    os.system('cls')

def separator():
    sep = "=" * 20
    print(sep)

def print_separator():
    sep2 = "=" * 109
    print(sep2)

def print_operators():
    print("| (1) addition ||", "(2) subtraction ||", "(3) multiplication ||", "(4) division ||",
          "(5) exit calculator ||", "(6) clear |")
def print_header():
    print("{:^107}".format("Python Simple Calculator by Sandro"))
    print_separator()
    print_operators()
    print_separator()
    print("{:^107}".format("O P E R A T O R S"))

print_header()
def footer():
    print("{:^107}".format("|Thank you for using calculator|"))
    print("{:^107}".format("|Sandro Jimena 080879|"))
def heart():
    print("{:^107}".format("  * *     * *   "))
    print("{:^107}".format("*      *      * "))
    print("{:^107}".format(" *           *  "))
    print("{:^107}".format("    *      *    "))
    print("{:^107}".format("       **       "))
def exit():
    print("{:^107}".format("Exiting Calculator"))

def inputs():
    n1 = num1()
    n2 = num2()
    return n1, n2
def num1():
    while True:
        try:
            return float(input("Number1: "))
        except ValueError as error:
            input_error(str(error))
def num2():
    while True:
        try:
            return float(input("Number2: "))
        except ValueError as error:
            input_error(str(error))
def input_error(error_message):
    error_value = error_message.split(": ")[1]
    print(f"Invalid input!! ({error_value}) is not a number, Please input a number:")
    space()

def space():
    print("")

while True:
    try:
        space()

        operator = float(input("Select operator: "))

        if operator == 5:
            close = input("Do you want to close the calculator? (Y/N): ")

            if close.upper() == "Y":
                for _ in range(5):
                    space()
                exit()
                space()
                heart()
                break
            elif close.upper() == "N":
                clear()
                print_header()
                continue
            else:
                close1 = input("Invalid choice! Please select (Y/N): ")

            if close1.upper() == "Y":
                for _ in range(5):
                    space()
                exit()
                space()
                heart()
                break
            elif close1.upper() == "N":
                clear()
                print_header()
            else:
                close1 = input("Invalid choice again! Please select (Y/N) only idiot: ")

            if close1.upper() == "Y":
                for _ in range(5):
                    space()
                exit()
                space()
                heart()
                break
            elif close1.upper() == "N":
                clear()
                print_header()
                continue
            else:
                for _ in range(3):
                    space()

                print('"SOBRANG TANGA MO NAMAN, DYOS KA NG KABOBOHAN!!! SABING (Y/N) LANG EEHHH!! BOBO TALAGA"')
                space()
                print('"HINDI KA SIGURO MAHAL NG MAMA MO!! NUNG BATA KA KAPE PINAPA DEDE SAYO "')
                time.sleep(1)
                clear()
                print_header()
                continue

        if operator == 6:
            clear()
            print_header()
            continue

        if operator > 6 or operator < 1:
            print(f"You input an invalid operator!! Please select from the operator list")
            continue

        n1, n2 = inputs()

        if operator == 1:
            result = n1 + n2
            print(f'The answer is: {result}')

        elif operator == 2:
            result = n1 - n2
            print(f'The answer is: {result}')

        elif operator == 3:
            result = n1 * n2
            print(f'The answer is: {result}')

        elif operator == 4:
            if n2 != 0:
                result = n1 / n2
                print(f'The answer is: {round(result, 2)}')
            else:
                print("Error! Cannot divide by zero")

    except ValueError as error:
        print(f"You input an invalid operator!! Please select from the operator list")
        continue

    separator()

count = 0
while count < 8:
    space()
    count += 1

footer()
