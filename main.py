from os import system


u_name = input("What is your name?\n")
valid_choise_byhour = {
    "6":["Shine shoes"],
    "7":["Shine shoes"],
    "8":["Shine shoes"],
    "9":["Shine shoes"]
}


while True:
    for i in range(6,23,1):
        choice = ""
        system("cls")
        print(f"The clock is now {i}:00")
        while choice not in valid_choise_byhour[str(i)]:
            choice = input("What to do\n")
