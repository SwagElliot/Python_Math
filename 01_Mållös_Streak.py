import random

målchans = int(input("Hur stor är chansen i procent att spelaren gör mål en viss match?"))
mållösStreak = int(input("Hur många mål lösa matcher i rad vill du kolla efter?"))
antalSessonger = 10000
matcher = 52
streak = 0
mål = 0
antalStreaks = 0



for i in range(antalSessonger):
    for i in range(matcher):
        mål = random.randrange(0,100)
        if målchans <= mål:
            streak += 1
        else:
            streak = 0
        if streak == mållösStreak:
            antalStreaks += 1
            streak = 0
            break
            
            

print("Spelaren var mållös i ",mållösStreak," matcher i rad",antalStreaks / (antalSessonger * 0.01)," procent av sessongerna.")