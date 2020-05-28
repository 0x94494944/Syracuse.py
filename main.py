# Library
import os

# The main function
def main():
    user_input = int(input("Enter a number >> "))
    os.system("cls")
    print("Here is your answer:\n")
    while user_input != 1:
        if user_input % 2 == 0:
            user_input = user_input // 2 
            print(user_input)
        else:
            user_input = (user_input * 3) + 1  
            print(user_input)
main()