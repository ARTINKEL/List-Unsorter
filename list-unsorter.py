import random

done = False
counter = 0
array = []

def unsort(array):
    return random.sample(array, len(array))

while (not done):
    number = input(("Enter Element " + str(counter) + ": "))
    try:
        array.append(int(number))
    except ValueError:
        done = True
        print(unsort(array))
    counter += 1