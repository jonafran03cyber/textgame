from os import system
global score
score=0
u_name = input("What is your name?\n")

valid_choise_byhour = {
    "6":["Shine shoes"],
    "7":["Shine shoes"],
    "8":["Shine shoes"],
    "9":["Shine shoes"]
}

def dedscreen():
    with open('ns.txt', 'w') as f:
        f.write(u_name, score)
    print(f"Your Score: {score}\n")
    print(f"The Leaderboard: {score}\n")
    for i in range (10):
        print(score)

dedscreen()

while True:
    for i in range(6,23,1):
        choice = ""
        system("cls")
        print(f"The clock is now {i}:00")
        while choice not in valid_choise_byhour[str(i)]:
            choice = input("What to do\n")

