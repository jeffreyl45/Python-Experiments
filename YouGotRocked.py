name1 = input("What is the name of player 1? ")
name2 = input("What is the name of player 2? ")
rocks = 0
turn = 0
while rocks < 16:
    print("There must be at least 16 rocks")
    rocks = int(input("How many rocks would you like? "))

while rocks > 0:
    print("Remaining rocks: %i" %rocks)
    if turn % 2 == 0:
        current = name1
    else:
        current = name2
    print("%s how many rocks would you like to take? " %current)
    choice = 0
    while choice <1 or choice > 3:
        choice = int(input("You can take 1, 2 or 3 rocks "))
        while rocks < choice <= 3:
            choice = int(input("There are not enough rocks for you to make this choice, please try again "))
    rocks = rocks - choice
    turn = turn + 1

if turn % 2 == 0:
    print("%s got rocked!" %name2)
else:
    print("%s got rocked!" %name1)





