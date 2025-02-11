import numpy as np

with open('config.secret') as file:
    secret = file.read()

print("hello main")
print("hello yop")
print("hahahahaha")
print(secret)
print(np.zeros(10))

def add(a: float, b: float) -> float:
    return a + b

def sub(a, b):
    return a - b
