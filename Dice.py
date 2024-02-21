import random
number = 0
attempts = 0

while number != 1:
    number = random.randint(1, 1000000)
    attempts +=1
print("Attempts: ",attempts)