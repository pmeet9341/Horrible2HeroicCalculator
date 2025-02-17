class Calculator:

    """Class Constructor"""
    def init(self):
        pass


    def summ(self):
        #SUMATION
        print("Select two numbers to sum: ")
        f_number = int(input("What is the first number: "))
        s_number = int(input("What is the second number: "))
        #total summation
        s = f_number + s_number
        return s # Returns the summation


    def mult(self):
        # MULTIPLICATION
        print("Select two numbers to multiply: ")
        f_number = int(input("What is the first number: "))
        s_number = int(input("What is the second number: "))
        # total multiplication
        m = f_number * s_number
        return m # Returns the multiplication


    def div(self):
        # DIVISION
        print("Select two numbers to divide: ")
        f_number = int(input("What is the first number: ")) # Gets the first number
        s_number = int(input("What is the second number: ")) # Gets the second number
        # total division
        d = f_number / s_number
        return d # Returns the division



def main():
    op = Calculator()
    # Prints results of summation, multiplication, and division
    print("The summation result is: ", op.summ()) # Prints the summation
    print("The multiplication result is: ", op.mult()) # Prints the multiplication
    print("The division result is: ", op.div()) # Prints the division

if __name__ == "__main__":
    main()