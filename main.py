from os import system
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
    "7":["shine shoes","train","march"],
    "8":["shine shoes","train","march"],
    "9":["shine shoes","train","march"],
    "10":["shine shoes","train","march"],
    "11":["shine shoes","train","march","eat"],
    "12":["shine shoes","train","march"],
    "13":["shine shoes","train","march"],
    "14":["shine shoes","train","march"],
    "15":["shine shoes","train","march"],
    "16":["shine shoes","train","march","eat"],
    "17":["shine shoes","train","march"],
    "18":["shine shoes","train","march"],
    "19":["shine shoes","train","march"],
    "20":["shine shoes","train","march"],
    "21":["shine shoes","train","march","eat"],
    "22":["shine shoes","train","march"],
    "23":["shine shoes","train","march"]
}
core_stats = {
    "food": 100,
    "shoe_shine":0,
    "health": 100,
    "luck": 0
}
def shine_shoes():
    print("Great choice")
    r = randint(0,200)


    if r<20:
        print("You fucked up")
        core_stats["shoe_shine"]-=r
    else:
        print("nice, shpe shine increased bye", r)
        core_stats["shoe_shine"] += r
    
    if core_stats["shoe_shine"]> 500:
        time.sleep(2)
        system("cls")
        print("fin puts, förtjänstfullt! sade fänrik Höglund")
        print("Du vann!! Hurra!!")
        time.sleep(200)

def eat():
    r = randint(0,100) + core_stats["luck"]
    if r < 30:
        print("Ison va gammal o möglig")
        print("-30 i mat")
        core_stats["food"] -= 20
    else:
        core_stats["food"] += 50
        print("Plus 50 mat")
def train():
    r = randint(0,100) + core_stats["luck"]
    if r < 30:
        print("Du stuka foten")
        print("-30 i hälsa")
        core_stats["food"] -= 20
    else:
        core_stats["food"] += 50
        print("Plus 50 hälsa")


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



txt = open("./backstroy.txt","r").read()
print(txt)
time.sleep(12)
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


        core_stats["food"]-=5
        core_stats["health"]-=5
        system("cls")
        print(f"Great, you proceed to {choice.capitalize()}") 
        if choice == "shine shoes":
            shine_shoes()
        else:
            if choice == "eat":
                eat()
            if choice == "train":
                train()
        standard_output()

        time.sleep(2)


        if h == 22:
            print("Good night")
            time.sleep(2)