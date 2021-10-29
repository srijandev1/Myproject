# calculator 2.0
def calculator_loop():
    firstnum = int(input("Enter the number:-\n"))
    a = 0
    while (a != 10000000000):

        operator = input("What do you wanna do?\n{+,-,*,/,=}\n")

        if operator == "+":
            secondnum = int(input("Enter the number:-\n"))
            firstnum = firstnum + secondnum
            # print(firstnum)
        elif operator == "-":
            secondnum = int(input("Enter the number:-\n"))
            firstnum = firstnum - secondnum
            # print(firstnum)
        elif operator == "*":
            secondnum = int(input("Enter the number:-\n"))
            firstnum = firstnum * secondnum
            # print(firstnum)
        elif operator == "/":
            secondnum = int(input("Enter the number:-\n"))
            firstnum = firstnum / secondnum
            # print(firstnum)
        elif operator == "=":
            print(firstnum)
            break
        else:
            print("Enter a valid operator!!")
            break

        second_operator = input("What do you wanna do?\n{+,-,*,/,=}\n")
        if second_operator == "+":
            secondnum = int(input("Enter the number:-\n"))
            firstnum = firstnum + secondnum
            # print(firstnum)
        elif second_operator == "-":
            secondnum = int(input("Enter the number:-\n"))
            firstnum = firstnum - secondnum
            # print(firstnum)
        elif second_operator == "*":
            secondnum = int(input("Enter the number:-\n"))
            firstnum = firstnum * secondnum
            # print(firstnum)
        elif second_operator == "/":
            secondnum = int(input("Enter the number:-\n"))
            firstnum = firstnum / secondnum
            # print(firstnum)
        elif second_operator == "=":
            print(firstnum)
            break
        else:
            print("Enter a valid operator!!")
            break

        a = a+1

calculator_loop()
