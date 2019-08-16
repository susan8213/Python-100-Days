import random


def gamer(is_win, money, debt):
    if is_win:
        money += debt
        print("You win!!!")
    else:
        money -= debt
        print("You lose!!")
    return money


def game_start():

    print("=====Game Start=====")
    money = 1000
    run = 0
    while money:
        run += 1
        print("*%d run: $%d" % (run, money))
        while True:
            debt = int(input("Please give your debt:"))
            if debt and debt <= money:
                break

        first = random.randint(1, 6) + random.randint(1, 6)
        print("You got %d" % first)
        if first == 7 or first == 11:
            money = gamer(True, money, debt)
            continue
        elif first == 2 or first == 3 or first == 12:
            money = gamer(False, money, debt)
            continue

        while True:
            second = random.randint(1, 6) + random.randint(1, 6)
            print("You got %d" % second)
            if second == first:
                money = gamer(True, money, debt)
                break
            elif second == 7:
                money = gamer(False, money, debt)
                break
    print("You have no money.")
    print("=====Game Over=====")

if __name__ == '__main__':
    game_start()
