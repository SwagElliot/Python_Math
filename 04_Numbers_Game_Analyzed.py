import random

gissning = 0
försök = 0

for i in range (10000):
    nummer = random.randint(0,100)
    lägsta = 0
    högsta = 100
    while gissning != nummer:
        gissning = random.randint(lägsta,högsta)
        försök +=1
        if gissning > nummer:
            högsta = gissning
        if gissning < nummer:
            lägsta = gissning

försökMedel = försök / 10000

print("Det tog I medelvärde ",försökMedel," försök att gissa numret.")
