import sys
f = open('fibboachi03', 'w', errors="ignore")
x = 1

for y in range(0, 10000):
    try:
        x = x + x
        x = str(x)
        f.write(x)
        x = int(x)
        print(x)
        print('')
    except:
        f.close()