# calculator
logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)
restart = True

first_number = int(input("write the first number:" ))
while restart:
    print("+\n-\n*\n/\n**'power'\n")
    operation = input("Pick an operation you want to perform?: ")
    second_number = int(input("Write the other number: "))
 
    if operation == "+":
        result = (first_number + second_number)
    elif operation == "-":
        result = (first_number - second_number)
    elif operation == "*":
        result = (first_number * second_number)
    elif operation == "/":
        result = (first_number / second_number)
    elif operation == "**":
        result = (first_number ** second_number)
    else:
        print("wrong input")  
    
    print(f"result:{result} ")   



    again = (input("type 'yes' if you want to continue with this or 'no' for exit: "))   
    if again == 'yes':
        first_number = result
    if again == 'no':
        restart = False
        print("Thanks for using!!🥰") 
       

     



