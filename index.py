def main():
    # problem1()
    # problem2()
    # problem3()
    # problem4()
    # problem5()
    challenge()
# Problem 1
#
# Create a printNumbers function to print integers from -25 to 20 to the console (print in the function)
def problem1():
    def printNumber():
        x = range(-25,26)
        for n in x:
            print(n)
    printNumber()
# Problem 2
#
# Create a function called checkPassword. Send two string variables to the checkPassword function to check if the strings are equal. Return true if they are equal and false if they are not equal. Print the function's return value.
#

def problem2():
    user = input("Enter the password\n")
    passW = "red"
    def checkPassword(str1,str2):
        if str1 == str2:
            return "True"
        else:
            return "False"
    print(checkPassword(user, passW))

# Problem 3
#
# Write a function that determines if a number passed to it is odd or even. Pass a number of your choosing (using input a good idea) and then using the result from the function, print if the number was even or not.
#
# examples:
#
# The number 12 is an even number!
#
# The number 5 is an odd number!
#
def problem3():
    def evenorodd():
        user = int(input("Enter a number\n"))
        x = user % 2
        if x == 0:
            print(f"The number {user} is an even number.")
        else:
            print(f"The number {user} is an odd number.")
    evenorodd()

# Problem 4
#
# Create a function for the challenge that you call from your main
# Create a second function that takes NO parameters
# Create a third function that takes a single greeting parameter (ex. Howdy) and returns a string using the passed in greeting and 'World' (ex. Howdy World!)
# From your first function, call the function(s) and print out the final result returned

def problem4():

    greeting = "Hello"

    def sent(hey):
        return hey
    def word():
        BYE = "World"
        return BYE
    def hry(GREET):
        return (f"{GREET} {word()}")

    print(sent(hry(greeting)))


# Problem 5:
#
# We will keep having this problem until EVERYONE gets it right without help
#
# Create a function that has a loop that quits with ‘q’. If the user doesn't enter 'q', ask them to input another string.

def problem5():
    user = 0
    while user == 0:
        user1 = input("Enter something\n")
        if user1 == "q" or user1 == 'Q':
            user = 2


#
# Challenge
#
# Create a function that accepts 2 numbers. When the function is called return the sum, difference, product, and quotient as 4 separate return values.
#
# Print the 4 results that are returned using f-strings.
#
# Example: If 2 and 6 are passed into the function, output should be similar to the following:
#
# The sum of 2 + 6 is 8
# The difference of 2 - 6 is  -4
# The product of 2 * 6 is 12
# The quotient of 2 / 6 is .333

def challenge():
    def nums():
        user = int(input("Enter a number.\n"))
        return user

    def math(b1,b2):
        n1 = b1
        n2 = b2

        def su(num1, num2):
            sum = num1 + num2
            return (f"The sum of {num1} + {num2} is {sum}")

        def dif(num1, num2):
            diff = num1 - num2
            return (f"The difference of {num1} - {num2} is  {diff}")

        def pro(num1,num2):
            prod = num1 * num2
            return (f"The product of {num1} * {num2} is {prod}")

        def quo(num1,num2):
            quot = num1 / num2
            return (f"The quotient of {num1} / {num2} is {quot}")

        print(su(n1,n2))
        print(dif(n1,n2))
        print(pro(n1,n2))
        print(quo(n1,n2))

    print(math(nums(),nums()))



main()
