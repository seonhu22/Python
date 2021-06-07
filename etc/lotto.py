import random
import sys

def input_manual_auto():
    global option
    option = []
    global checklist_page
    checklist_page = ['First', 'Second', 'Third', 'Fourth', 'Fifth']

    for i in range(5):
        print("Choose Option for", checklist_page[i], "Checklist")
        print("1: Auto")
        print("2: Manual")
        option.append(int(input()))

def select_number():
    number = list(range(1, 46))
    global checklist_number
    checklist_number = []

    for i in range(5):
        if option[i] == 1:
            print(checklist_page[i], "is Auto.")
            auto()
            checklist_number.append(auto_number)
            continue
        else:
            print(checklist_page[i], "is Manual.")
        print("Choose 6 number on", checklist_page[i]," checklist")
        select = []
        for j in range(6):
            print("Number", j + 1)
            while (1):
                test = int(input())
                if test not in select and test in number:
                    select.append(test)
                    break
                else:
                    print("You already input this number or wrong number."
                          "Input range is 1~45. Please try another number.")
        checklist_number.append(select)

def auto():
    global auto_number
    auto_number = []
    for i in range(6):
        while(1):
            test = random.randrange(1, 46)
            if test not in auto_number:
                auto_number.append(test)
                break

def make_answer():
    global answer
    answer = []

    for i in range(7):
        while (1):
            test = random.randrange(1, 46)
            if test not in answer:
                answer.append(test)
                break

def check_answer():
    global normal
    global bonus
    normal = []
    bonus = []

    for i in range(5):
        normal.append(len(set(answer[0:6]) & set(checklist_number[i])))
        if answer[6] in checklist_number[i]:
            bonus.append(1)
        else:
            bonus.append(0)

def print_result():
    for i in range(5):
        print(checklist_page[i], "result\n",
              "Your Choice:", checklist_number[i], "\n",
              "Answer:", answer[0:6], "Bonus:", answer[6], "\n",
              "count without bonus:", normal[i], "\n",
              "count with bonus:", normal[i] + bonus[i], "\n")
        if normal[i] == 3:
            print("Congratulations!! You got 5th!!\n")
        elif normal[i] == 4:
            print("Congratulations!! You got 4th!!\n")
        elif normal[i] == 5 and bonus[i] == 1:
            print("Congratulations!! You got 2nd!!\n")
        elif normal[i] == 5:
            print("Congratulations!! You got 3rd!!\n")
        elif normal[i] == 6:
            print("Congratulations!! You got 1st!!\n")
        else:
            print("You losing the ticket\n")

print("-----------------Simple Lotto Experience-----------------\n")

make_answer()

while(1):
    input_manual_auto()
    select_number()
    check_answer()
    print_result()
    print("Try again??\n"
          "1: Yes\n"
          "2: No\n")
    if int(input()) == 2:
        break

sys.exit()
