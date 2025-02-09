import datetime

#1

a = datetime.datetime.now() - datetime.timedelta(days=5)
print("answer", a)

#2

print(datetime.datetime.now() - datetime.timedelta(days=1))
print(datetime.datetime.now())
print(datetime.datetime.now() + datetime.timedelta(days=1))

#3

print(datetime.datetime.now().replace(microsecond=0))

#4

zmixan = datetime.datetime(2007, 11, 7, 12, 30, 0)
tokha = datetime.datetime(2007, 11, 30, 1, 34, 0)
difference = tokha - zmixan
print(difference)
