from os import system
global score
score=0
import time
from random import randint
alive = True


u_name = input("What is your name?\n")
# eat, sleep, train, nerd, march
valid_choise_byhour = {
    "6":["shine shoes", "eat"],
    "7":["shine shoes"],
    "8":["shine shoes"],
    "9":["shine shoes"],
    "10":["shine shoes"],
    "11":["shine shoes","eat"],
    "12":["shine shoes"],
    "13":["shine shoes"],
    "14":["shine shoes"],
    "15":["shine shoes"],
    "16":["shine shoes","eat"],
    "17":["shine shoes"],
    "18":["shine shoes"],
    "19":["shine shoes"],
    "20":["shine shoes"],
    "21":["shine shoes","eat"],
    "22":["shine shoes"],
    "23":["shine shoes"]
}
core_stats = {
    "food": 100,
    "shoe_shine":0,
    "health": 100,
    "luck": 0
}
def shine_shoes():
    print("Great choice")
    r = randint(0,100)
    if r<20:
        print("You fucked up")
        core_stats["shoe_shine"]-=r
    else:
        print("nice, shpe shine increased bye", r)
        core_stats["shoe_shine"] += r

def eat():
    r = randint(0,100) + core_stats["luck"]
    if r < 30:
        print("Ison va gammal o möglig")
        print("-30 i mat")
        core_stats["food"] -= 30
    else:
        core_stats["food"] += 20



def dedscreen():
    with open('ns.txt', 'w') as f:
        f.write(u_name, score)
    print(f"Your Score: {score}\n")
    print(f"The Leaderboard: {score}\n")
    for i in range (10):
        print(score)

#dedscreen()
def choice_string_by_hour(hour, hourly_list):
    options = hourly_list[str(hour)]
    temp_str = "You can "
    for index, choice in enumerate(options):      
        temp_str = temp_str + choice
        if index + 1 < len(options):
            temp_str = temp_str + " OR "
    return temp_str + "!"

def standard_output():
    print("="*50)
    for stat in core_stats.keys():
        print(stat, " : ", core_stats[stat])
    print("="*50)




while alive:
    for h in range(6,23,1):
        system("cls")

        choice = ""
        print(f"The clock is now {h}:00, {u_name}, what to do?")
        # You can do ____ OR ____
        print(choice_string_by_hour(h,valid_choise_byhour))

        #Choose task
        tmp_cnt = 0
        while choice not in valid_choise_byhour[str(h)]:
            if tmp_cnt == 0:
                choice = input("What do you do now?\n").lower()
            else:
                choice = input("Not valid option\n").lower()
            tmp_cnt +=1

        system("cls")
        print(f"Great, you proceed to {choice.capitalize()}") 
        if choice == "shine shoes":
            shine_shoes()
        else:
            if choice == "eat":
                eat()
        time.sleep(2)
        standard_output()


        if h == 22:
            print("Good night")
            time.sleep(2)
