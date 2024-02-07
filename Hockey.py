import random

målchans = int(input("Hur stor är chansen i procent att spelaren gör mål en viss match?"))
mållösa_matcher = int(input("Hur många mål lösa matcher i rad vill du kolla efter?"))
sessonger = 10000
matcher = 52
streak = 0
mål = 0
antal_tillfällen = 0



for i in range(sessonger):
    for i in range(matcher):
        mål = random.randint(0,100)
        if målchans > mål:
            streak = streak +1
        else:
            streak = 0
        if streak == mållösa_matcher:
            antal_tillfällen +=1

print("Spelaren var mållös i ",mållösa_matcher," matcher i rad",antal_tillfällen / sessonger," procent av sessongerna.")