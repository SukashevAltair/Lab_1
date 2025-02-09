#1

def san(f):
    for i in range(f):
        yield i ** 2
f = int(input())
for j in san(f):
    print(j)

#2

def even(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i
n = int(input())
for i in even(n):
    print(i, end=", ")

#3

def sana(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0 :
            yield i
n = int(input())
for j in sana(n):
    print(j, end=", ")

#4

def squares(a, b):
    for i in range(a, b + 1):
        yield i * i
a = int(input())
b = int(input())
for i in squares(a, b):
    print(i, end = " ")

#5

def down(N):
    for i in range(N, -1, -1):
        yield i
N = int(input())
for i in down(N):
    print(i, end=" ")