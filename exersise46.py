#SECTION 7 
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
#print(time.time())


#def numbers(max):
#    time1 = time.time()
#    for i in range(0, max):
#        print(i)
#    time2 = time.time()
#    print(str(time2-time1))


#numbers(100)
# 2
#print(time.asctime())

# 3
#tup = (1971, 1, 4, 14, 15, 12, 0, 0, 0)
#print(time.asctime(tup))
# 4
#print(time.localtime())
#t = time.localtime()
#year = t[0]
#day = t[2]
#month = t[1]
#print(str(day) + "/" + str(month) + "/" + str(year))
#5
#for i in range (0,5):
#    print(i)
#    time.sleep(2)

import turtle
#1
t = turtle.Pen()
#t.forward(50)
#t.left(90)
#t.forward(50)
#t.left(90)
#t.forward(50)
#t.left(90)
#t.forward(50)
#print(t)

#2
#t_t = turtle.Pen()
#for i in range(0,8):
#    t_t.forward(50)
#    t_t.left(45)
#    print(t_t)

#3
#t.reset()
#for i in range(1,38):
#    t.forward(100)
#    t.left(175)
#    print(t)

#4
#t.reset()
#for i in range(1,20):
#    t.forward(100)
#    t.left(95)
#    print(t)

#5
#t.reset()
#t.left(180)
#t.forward(100)
#t.right(180)
#for i in range(1,20):
#    t.forward(100)
#    t.left(95)
#    print(t)

#t.up()
#t.forward(100)
#t.forward(40)

#t.down()
#for i in range(1,20):
 #   t.forward(100)
 #   t.left(95)
 #   print(t)

#6
t = turtle.Pen()
t.color(0,0,1)
t.begin_fill()
t.forward(150)
t.left(90)
t.forward(30)
t.left(90)
t.forward(40)
t.right(90)
t.forward(40)
t.left(90)
t.forward(70)
t.left(90)
t.forward(40)
t.right(90)
t.forward(40)
t.left(90)
t.forward(30)
t.end_fill()
t.up()
t.right(90)
t.right(180)
t.forward(40)
t.color(0,0,0)
t.down()
t.begin_fill()
t.right(90)
t.forward(15)
t.forward(15)
t.left(90)
t.circle(15)
t.end_fill()
t.up()
t.forward(70)
t.begin_fill()
t.down()
t.circle(15)
t.end_fill()

#7
t = turtle.Pen()
def square(side):
    for i in range (0,5):
        t.forward(side)
        t.left(90)
        print(square)

square(10)
square(20)
square(50)

def circle(radius):
    t.circle(radius)
    print(circle)

circle(10)
circle(50)
circle(100)