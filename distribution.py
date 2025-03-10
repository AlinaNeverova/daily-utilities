"""
Skyscraper Climbing Game
This program simulates a game where players attempt to climb a skyscraper. 
Players roll a dice on each step, with the following rules:
- Rolling 1 or 2: Step down one floor (minimum is floor 0).
- Rolling 3, 4, or 5: Step up one floor.
- Rolling 6: Step up a random number of floors between 1 and 6.
- With a 0.5% chance, the player falls to the ground (floor 0).

The program visualizes the distribution of outcomes after 100 steps for 500 players.
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)                           # Set seed so that the programme can be repeated with the same result
all_walks = []

for i in range(500):                          # Set the number of attempts and describe the rules
    random_walk = [0]
    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.005 :
            step = 0
        random_walk.append(step)

    all_walks.append(random_walk)

# print(all_walks)                            # Remove the grid to see the possible numbers in the lists

np_aw_t = np.transpose(np.array(all_walks)) 

# plt.plot(np_aw)                             # Remove the grid to see a graph of what each path looked like
# plt.show()

ends = np_aw_t[-1,:]                          # In the end, we look at the distribution of outcomes and understand the probability of each one using histogram
plt.hist(ends)
plt.show()