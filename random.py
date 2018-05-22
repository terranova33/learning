

import random

#choice() fn
print("random number from range(100) : ", random.choice[(range(100))])
list = ([1, 3, 5, 7, 2, 6])
print("random element from list : ", random.choice(list))
str = ("Hello World!")
print("random character from string: ", random.choice(str))

#randrange() fn
print("random range from range(100): ", random.randrange(1,100, 2)) #(start, end, step)
print("randrange(100): ", random.randrange(100))

#random() fn
print("random():", random.random())
print("random():", random.random())

#seed() fn
random.seed()
print("random number with default seed", random.random())
random.seed(10)
print("random number with int seed: ", random.random())
random.seed("hello", 2)
print("random number with string seed: ", random.random())

#shuffle fn
list = [20, 15, 10, 5]
random.shuffle(list)
print("reshuffled list: ", list)
print("reshuffled list: ", list)

#uniform fn
print("random float uniform(5, 10): ", random.uniform(5,10))
print("random float uniform(7, 14): ", random.uniform(7,14))
