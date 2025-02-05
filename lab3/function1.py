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
#6

def rever(x):
    return x[::-1]
x = "We are ready".split()
print(rever(x))

