from os import system
score=0
import time
from random import randint
alive = True

def high_score_list():
    global score, scores
    hlist= r"ns.txt"
    with open (hlist, "r") as file:
        line = file.readline()
        high_scores = [int(s) for s in line.split()]
        if score in high_scores:
            return
        high_scores.append(score)
        high_scores.sort()
        with open (hlist, "w") as file :
            for high_score in high_scores [::-1]:
                    file.write(str(high_score)+ "")

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
    r = randint(0,5) + core_stats["luck"]
    core_stats["shoe_shine"] += (r*r)
    core_stats["luck"] += r

def eat():
    r = randint(0,100) + core_stats["luck"]
    if r < 30:
        print("Ison va gammal o möglig")
        print("-30 i mat")
        core_stats["food"] -= 20
    else:
        core_stats["food"] += 20


while alive:
    for h in range(6,23,1):
        choice = ""
        system("cls")
        print(f"The clock is now {h}:00")
        while choice not in valid_choise_byhour[str(h)]:
            choice = input("What to do\n")

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
        score+=1
        time.sleep(1)

        if h == 22:
            print("Good night")
            time.sleep(2)