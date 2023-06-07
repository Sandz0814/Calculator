import time
import os

def clear():
    # Clear the console by scrolling the output
    os.system('cls' if os.name == 'nt' else 'printf "\033c"')

def separator():
    sep = "=" * 20
    print(sep)

def print_separator():
    sep2 = "=" * 109
    print(sep2)

print_separator()

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
    print("{:^107}".format("Thank you for using calculator"))
    print("{:^107}".format("Sandro Jimena 080879"))

def operate():
    n3 = num3()
    return n3

def num3():
    while True:
        try:
            return int(input("Select operator: "))
        except ValueError as error:
            operator_error(str(error))

def operator_error(error_message):
    error_value = error_message.split(": ")[1]
    print(f"Invalid Operator!!, {error_value} Please select Operatoron the list:")
    space()

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

def inputs():
    n1 = num1()
    n2 = num2()
    return n1, n2

def input_error(error_message):
    error_value = error_message.split(": ")[1]
    print(f"Invalid input!! {error_value} is not a number, Please input a number:")
    space()

def space():
    print("")

while True:
    try:
        space()

        n3 = operate()

        if n3 == 5:
            close = input("Do you want to close the calculator? (Y/N): ")

            if close.upper() == "Y":
                print("Exiting the calculator...")
                break
            elif close.upper() == "N":
                clear()
                print_header()
                continue
            else:
                close1 = input("Invalid choice! Please select (Y/N): ")

            if close1.upper() == "Y":
                print("Exiting the calculator...")
                break
            elif close1.upper() == "N":
                clear()
                print_header()
            else:
                close1 = input("Invalid choice again! Please select (Y/N) only idiot: ")

            if close1.upper() == "Y":
                print("Exiting calculator")
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
                time.sleep(10)
                clear()
                print_header()
                continue

        if n3 == 6:
            clear()
            print_header()
            continue

        if n3 > 6 or n3 < 1:
            operator_error()
            clear()
            print_header()
            continue

        n1, n2 = inputs()

        if n3 == 1:
            result = n1 + n2
            print(f'The answer is: {result}')

        elif n3 == 2:
            result = n1 - n2
            print(f'The answer is: {result}')

        elif n3 == 3:
            result = n1 * n2
            print(f'The answer is: {result}')

        elif n3 == 4:
            if n2 != 0:
                result = n1 / n2
                print(f'The answer is: {round(result, 2)}')
            else:
                print("Error! Cannot divide by zero")

    except ValueError as error:
        operator_error()
        clear()
        print_header()
        continue

    separator()

for _ in range(15):
    space()

print_separator()
footer()
print_separator()
