import random


nummer = random.randint(0,101)
gissning = 0
försök = 0

print("Jag tänker på ett nummer mellan 1 och 100. Vad gissar du?")

while gissning != nummer:
    gissning = int(input(""))
    försök +=1

    if gissning > nummer:
        print("Fel, lägre.")
    if gissning < nummer:
        print("Fel, högre.")

print("RÄTT! Numret var ", nummer,". Du gissade rätt på ",försök," försök.")