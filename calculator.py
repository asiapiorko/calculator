class Calculator:

    def substract(self, number_one, number_two):
        return number_one - number_two

    def add(self, number_one, number_two):
        return number_one + number_two

    def multiply(self, number_one, number_two):
        return number_one * number_two

    def divide(self, number_one, number_two):
        return number_one / number_two


class Main:

    calculator = Calculator()
    print("Enter your option:")
    option = input("1 add, 2 sub, 3 div, 4 mult")
    number_one = input("Enter the number one ")
    number_two = input("Enter the number two ")
    
    if option == 1:
       result = calculator.substract(number_one, number_two)
       print("number_one %s" % number_one)

    elif option == 2:
       result = calculator.add(number_one, number_two)
    
    elif option == 3:
       result = calculator.multiply(number_one, number_two)

    elif option == 4:
       result = calculator.divide(number_one, number_two)

    else:
        print("Error. You need to enter a valid option")
    
    if type(result) == int:
       print("The result is: %s" % result)