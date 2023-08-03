# bounce.py
#
# Exercise 1.5

initialHeight = 100

for i in range(1, 11):
    initialHeight *= 0.6
    print(i, round(initialHeight, 4))