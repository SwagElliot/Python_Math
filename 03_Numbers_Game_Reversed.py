import random


nummer = int(input("Välj ett nummer mellan 1 och 100: "))

lägsta = 0
högsta = 101

gissning = 0
försök = 0

while gissning != nummer:
    gissning = random.randint(lägsta,högsta)
    försök +=1
    print(gissning)
    
    if gissning > nummer:
        print("Fel, lägre.")
        högsta = gissning
    if gissning < nummer:
        print("Fel, högre.")
        lägsta = gissning


print("RÄTT! Numret var ", nummer,". Du gissade rätt på ",försök," försök.")