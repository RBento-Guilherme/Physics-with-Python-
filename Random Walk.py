# Importig the necessary packages

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

#Defining the seed of the die

np.random.seed(1)

#Defining the parameters for random walk

s = 100000  #Number of simulations
N = 1000    #Number of steps
p = []      #Array with the final positions

#Simulating the random walk

for i in range(s):
  x0 = 0 #Defining the initial position
  for j in range(N):
    die = np.random.rand()
    if die < 0.5:
      x0 = x0 - 1
    else:
      x0 = x0 + 1
  p.append(x0)

#Calculating the theoretical probabilities

pos = np.arange(-N, N+1, 1)
x = []
y = []
for pos_value in pos:
  if (N + pos_value) % 2 == 0:
    k = (N + pos_value) / 2
    pro = binom.pmf(k, N, 0.5)
    if pro > 10**-4: #Limiting what is going for the graph
      x.append(pos_value)
      y.append(pro)

#Plotting a histogram and theoretical probabilities

plt.hist(p, bins=np.arange(-N - 0.5, N + 0.5, 1), rwidth=0.8, edgecolor='black',density=True)
plt.plot(x, y, marker = 'o', color='r',linestyle = 'None', label='Theoretical Probability')
plt.xlim(min(x), max(x))
plt.xlabel('Position')
plt.ylabel('Probability')
plt.title('Random Walk')
plt.legend()
plt.show()
