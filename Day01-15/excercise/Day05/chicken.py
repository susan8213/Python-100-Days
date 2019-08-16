
num = int(input("Please enter how many chickens to sell and earn the same money as the number of chickens: "))

for x in range(num//5):
    for y in range((num-x)//3):
        male = x
        female = y
        child = (num-x-y)

        if child >= 0 and (9*female + 15*male + child) == 3*num:
            print("Male %d, Female %d, Child %d" %(male, female, child))
