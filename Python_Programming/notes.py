# --------------------------------------------

# matpotlib
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(fname='data/inflammation-01.csv', delimiter=',')

# plt.figure() creates a space into which we will place all of our plots.
# figsize tells Python how big to make this space.
fig = plt.figure(figsize=(10.0, 3.0))

# figure using its add_subplot() to place each subplot into it.
axes1 = fig.add_subplot(1,3,1)
axes2 = fig.add_subplot(1,3,2)
axes3 = fig.add_subplot(1,3,3)

# title and plot
axes1.set_ylabel('average')
axes1.plot(np.mean(data, axis=0))

axes2.set_ylabel('max')
axes2.plot(np.max(data, axis=0))

axes3.set_ylabel('min')
axes3.plot(np.min(data, axis=0))

# using tight_layout() to squeeze the graphs together more closely.
fig.tight_layout()

plt.show()

# ----------------------------------------

# swapping the contents of variables
left, right = [right, left]

# If you want variables with mutable values to be independent, 
# you must make a copy of the value when you assign it.
salsa = ['peppers', 'onions', 'cilantro', 'tomatoes']
mySalsa = salsa        # <-- mySalsa and salsa point to the *same* list data in memory
# mySalsa = list(salsa)        # <-- makes a *copy* of the list
salsa[0] = 'hot peppers'
print('Ingredients in my salsa:', mySalsa)

# -----------------------------------------------


# don't know why edited disappearing.
# python2 5/9 = 0 ,    ==> 5.0/9 = 0.5555556 or float(5)/9 = 0.555555556
# python3 5/9 = 0.555555556 , ==> 5//9 = 0
# differences among pass-by-value, pass-by-reference and pass-by-object
# python using pass-by-object: when parameter passed-by is mutable, then would be changed; otherwise, no.
# Assertitions
# assert len(sys.argv) == 4, 'Need exactly 3 arguments'

# ---------------------------------------------

import sys

# $python prac_command_line.py para1 para2 para3
# using sys.argv[] to receive these parameters

