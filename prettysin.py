import math
import time
numCycle = 2
pi = math.pi

def sin(x):
    return math.sin(x)

x = 0
while x < (numCycle*1*pi):
    bar = int(20*sin(x))
    x += 0.3
    print((20+bar)*'=')
    time.sleep(0.05)
