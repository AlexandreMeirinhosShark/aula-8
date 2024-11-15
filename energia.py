import time
x = 0
y = 0
z = 0
while True:
    print(f"{z}:{y}:{x}")
    x += 1
    if x == 60:
        x = 0
        y += 1
    if y == 60:
        y = 0
        z += 1
    time.sleep(1)

 # 06:03:14
