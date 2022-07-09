import random

diceAmount = input("How many dice would you like to roll? | ")
sideAmount = input("How many sides should each dice have? | ")
timesRolled = 1
rollTotal = 0

for i in range(int(diceAmount)):
    unnamedVar = str(random.randint(1, int(sideAmount)))
    rollTotal += int(unnamedVar)
    print("Roll " + str(timesRolled) + ": " + str(unnamedVar))
    timesRolled += 1
print("Total: " + str(rollTotal))
