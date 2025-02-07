#1

def grams(gram):
    ounces = 28.3495231 * gram
    return ounces
gram=float(input("gram:"))
print("ounces=",grams(gram))

#2

def temperature(tempF):
    return (5 / 9) * (tempF - 32)
tempF=float(input("Fahrenheit temperature:"))
print("centigrade temperature:",temperature(tempF))

#3

def solve(numheads, numlegs):
    Ty = ((4 * numheads) - numlegs)/2
    Kx = numheads - Ty
    print(Kx, "\n", Ty, sep="")
numheads=float(input("numheads:"))
numlegs=float(input("numlegs:"))
solve(numheads, numlegs)

#4

def filter_prime(l):
    k = []
    for i in l:
        if i > 1 :
            u = True
            for j in range(2,int(i**0.5 + 1)):
                if i % j == 0:
                    u = False
                    break
            if u:
                k.append(i)
    return k
l = [12,23,34,32,33,7,3]
print(filter_prime(l))

#5

import itertools
a = input()
b = itertools.permutations(a)
for c in b:
    print("".join(c))
    
#6

def rever(x):
    return x[::-1]
x = "We are ready".split()
print(rever(x))

#7

def has33(nums):
    for i in range(len(nums)):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

#8

def spy_game(a):
    code = [0, 0, 7] 
    index = 0

    for num in a:
        if num == code[index]: 
            index += 1
        if index == len(code): 
            return True

    return False
# 9.

import math
def VofSphere(r):
    return ((4 / 3) * math.pi * r ** 3)

# 10.

def UniItems(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return b

# 11.

def ispalindrome(a):
    return a == a[::-1]

# 12.

def histogram(a):
    for i in a:
        print("*" * i)

# 13.

import random
a = input("Hello! What is your name? \n")
print(f"Well, {a}, I am thinking of a number between 1 and 20.")
b = random.randint(1, 20)
i = 0
while True:
    i += 1
    c = int(input("Take a guess.\n"))
    print()
    if c == b:
        print(f"Good job, {a}! You guessed my number in {i} guesses!")
        break
    elif c < b:
        print("Your guess is too low.")
        continue
    elif c > b:
        print("Your guess is too high.")
        continue

# 14
import math
a = "frrferre"
if ispolindrome(a):
    print(a)

b = 3.14
if b == math.pi:
    print("stupid")
    
d = 0.67756567567
if d == ceil(d):
    print(asa)


