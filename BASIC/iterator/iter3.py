from itertools import cycle,repeat
# The function count counts up infinitely from a value.
#count has two arguments: count(x, y) where x is a start value and y is the increment/decrement pace (with y being a positive or negative number, respectively).
# The function cycle infinitely iterates through an iterable (for instance a list or string).
# The function repeat repeats an object, either infinitely or a specific number of times


# Gimme a list which has "Huri" string 5 times
print(list(repeat("Huri", 5)))  #specifying no. of time repeat should run by defeault infinite


for i in cycle("Huri"): #cannot give 2 arguments it will be infinite always
    print(i)
