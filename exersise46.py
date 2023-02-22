# !!!!! MODULES - random / sys / time / turtle / 

import random
# random.
#comGuess = random.randint(0,100)
# while True:
###   userGuess = int(input("Guess a number between 0 - 100: "))
#   if userGuess>comGuess:
#      print("Cuess lower")
# elif userGuess<comGuess:
#    print("Guess higher")
# else:
#   print("Congrats, You've guessed the correct number!")
#  break


#food = ["Raviolli", "Pasta", "Pizza", "Cheesecake"]
# print(random.choice(food))
# print(random.shuffle(food))
# random.shuffle(food)
# print(food)

import sys
# sys.
#inputStatement = sys.stdin.readline()

import time
# 1
print(time.time())


def numbers(max):
    time1 = time.time()
    for i in range(0, max):
        print(i)
    time2 = time.time()
    print(str(time2-time1))


numbers(100)
# 2
print(time.asctime())

# 3
tup = (1971, 1, 4, 14, 15, 12, 0, 0, 0)
print(time.asctime(tup))
# 4
print(time.localtime())
t = time.localtime()
year = t[0]
day = t[2]
month = t[1]
print(str(day) + "/" + str(month) + "/" + str(year))
#5
for i in range (0,5):
    print(i)
    time.sleep(2)

import turtle
#1
#t = turtle.Pen()
#t.forward(50)
#t.left(90)
#t.forward(50)
#t.left(90)
#t.forward(50)
#t.left(90)
#t.forward(50)
#print(t)
#2
t_t = turtle.Pen()
for i in range(0,8):
    t_t.forward(50)
    t_t.left(45)
    print(t_t)

