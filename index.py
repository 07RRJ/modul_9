import os
from sys import exit
from time import sleep
from random import randint
from msvcrt import getwch
from colors import bcolors

# import color

os.system("cls")

function_ = ""
first_number = 0
second_number = 0

while True:
    print(bcolors.DEFAULT + "1) add\n2) subtract\n3) multiply\n4) divide")
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
                    first_number = input("first number: ")
                    break
                except:
                    os.system("cls")
                    print("use a valid number")
            while True:
                try:
                    second_number = input("second number: ")
                    break
                except:
                    os.system("cls")
                    print("use a valid number")

            os.system("cls")
            print("thinking")
            for repets in range(1,4):
                for dots in range(1,4):
                    sleep((randint(1, 2))/10)
                    os.system("cls")
                    print("thinking"+"." * dots)
            sleep(0.5)
            try:
                print(bcolors.GREEN)
                os.system("cls")
                if function_ == 1:
                    print(f"{first_number} + {second_number} = {eval((first_number) + (second_number))}\n")
                elif function_ == 2:
                    print(f"{first_number} - {second_number} = {eval((first_number) - (second_number))}\n")
                elif function_ == 3:
                    print(f"{first_number} * {second_number} = {eval((first_number) * (second_number))}\n")
                elif function_ == 4:
                    if second_number == 0:
                        print("you cant devide by \"0\"")
                    else:
                        print(f"{first_number} / {second_number} = {eval((first_number) / (second_number))}\n")
                bcolors.DEFAULT
            except:
                os.system("cls")
                print(bcolors.RED,"use a valid input\n",bcolors.DEFAULT)
        else:
            print("chose a number available\n")
    else:
        print("use a valid input\n")