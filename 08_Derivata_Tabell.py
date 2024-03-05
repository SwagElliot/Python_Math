import matplotlib.pyplot as plt
import numpy as np

h = 0.00001

func = input("Function: ")

a = int(input("x-Value: "))

f = lambda x:eval(func)

fx = f(a)
fxh = f(a+h)

derivate = (fxh - fx) / h

print("The derivate is:",derivate)