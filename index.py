import os
from sys import exit
from time import sleep
from random import randint
from msvcrt import getwch

# import color

os.system("cls")

function_ = ""
first_number = 0
second_number = 0

def add(first_number, second_number):
    return first_number + second_number

def subtract(first_number, second_number):
    return first_number - second_number

def multiply(first_number, second_number):
    return first_number * second_number

def devide(first_number, second_number):
    return first_number / second_number

while True:
    print("1) add\n2) subtract\n3) multiply\n4) divide")
    function_ = getwch()
    if function_ == "q":
        os.system("cls")
        exit("you quit")
    os.system("cls")
        
    if function_.isdigit():
        function_ = int(function_)

        if function_ > 0 and function_ < 5:

            while True:
                try:
                    first_number = float(input("first number: "))
                    break
                except:
                    os.system("cls")
                    print("use a valid number")
            while True:
                try:
                    second_number = float(input("second number: "))
                    break
                except:
                    os.system("cls")
                    print("use a valid number")

            os.system("cls")
            print("thinking")
            for repets in range(1,4):
                for dots in range(1,4):
                    sleep((randint(1, 4))/10)
                    os.system("cls")
                    print("thinking"+"." * dots)
            sleep(0.5)
            os.system("cls")

            if function_ == 1:
                print(f"{first_number} + {second_number} = {add(first_number, second_number)}\n")
            elif function_ == 2:
                print(f"{first_number} - {second_number} = {subtract(first_number, second_number)}\n")
            elif function_ == 3:
                print(f"{first_number} * {second_number} = {multiply(first_number, second_number)}\n")
            elif function_ == 4:
                if second_number == 0:
                    print("you cant devide by \"0\"")
                else:
                    print(f"{first_number} / {second_number} = {devide(first_number, second_number)}\n")
            
            else:
                print("use a valid input\n")
        else:
            print("chose a number available\n")
    else:
        print("use a valid input\n")