import random

def get_guess():
    x = input("What is your three digit guess? ")
    xlist = [int(num) for num in list(x)]
    return xlist


def create_guess(combo_list):
    while True:
        in_list = 0
        in_right_place = 0
        riddle_combo = get_guess()
        if combo_list != riddle_combo:
            for i in combo_list:
                if i in riddle_combo:
                    in_list += 1
            if in_list != 0:
                for i in range(3):
                    if combo_list[i] == riddle_combo[i]:
                        in_right_place += 1
            print("\n{} {} digit(s) is right.".format(riddle_combo, in_list))
            print("{0:<10}{1} digit(s) are in right place.".format(' ', in_right_place))
        else:
            print(f"You Found the Correct Combination {riddle_combo}!")
            break

combo_list = random.choices([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], k=3)
print(combo_list)
create_guess(combo_list)