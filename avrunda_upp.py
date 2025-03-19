import os

os.system("cls")

def round_up(number):
    if int(number + 0.5) > number:
        number = int((number + 0.5))
        return number
    else:
        number = int(number)
        return number

while True:
    try:
        number = float(input("number:"))
    except:
        print("use valid input")
    os.system("cls")
    print(round_up(number))