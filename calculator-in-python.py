n1 = float(input("Enter a number: ") )
n2 = float(input("Enter another: ") )

opcion = 0
while True:
    print("""
    What calculation to do?
    
    1) Add two numbers
    2) Subtract two numbers
    3) Multiply numbers
    4) Divide two numbers
    5) Change numbers
    6) Turn off calculator
    """)
    opcion = int(input("Choose an option: ") )     

    if opcion == 1:
        print(" ")
        print("Result: the sum of",n1,"+",n2,"is equal to",n1+n2)
    elif opcion == 2:
        print(" ")
        print("Result: the remainder of",n1,"-",n2,"is equal to",n1-n2)
    elif opcion == 3:
        print(" ")
        print("Result: the product of",n1,"*",n2,"is equal to",n1*n2)
    elif opcion == 4:
        print(" ")
        print("Result: division of",n1,"/",n2,"in equal to",n1/n2)
    elif opcion == 5:
        n1 = float(input("Enter the first number: ") )
        n2 = float(input("Enter the second number: ") )
    elif opcion == 6:
        break
    else:
        print("Wrong choice")
