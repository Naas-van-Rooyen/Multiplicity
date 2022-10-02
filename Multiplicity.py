import pandas as pd
import matplotlib.pyplot as plt
import math as m
import numpy as np

# Array decleration for the different variables:
N_a = []
N_b = []
q_a = []
q_b = []
Ohm_a = []
Ohm_b = []
Ohm_tot = []

# Multiplicity formula:
def Multiplicity(N, q):
    M = (m.factorial(q + N - 1))/((m.factorial(q))*(m.factorial(N-1)))
    return M
    

# Multiplicity for the N = 3 and q = 6 case
q_a = 0
q_b = 6
Ohm_a.clear()
Ohm_b.clear()
Ohm_tot.clear()


for i in range(0,7):
    Ohm_a.append(Multiplicity(3, q_a))
    q_a += 1

for i in range(0,7):
    Ohm_b.append(Multiplicity(3, q_b))
    q_b -= 1

Ohm_tot = np.multiply(Ohm_a, Ohm_b)
qa = np.arange(0,7)
qb = np.arange(6,-1,-1)

data = {'q_a': qa, 'Omega_A': Ohm_a, 'q_b': qb, 'Omega_B': Ohm_b, 'Omega_Total': Ohm_tot}

df = pd.DataFrame(data)

print(df.to_string(index = False))

plt.bar(qa, Ohm_tot, label = 'Omega_Total')
plt.plot(qa, Ohm_a, color = 'yellow', label = 'Omega_a')
plt.plot(qa, Ohm_b, color = 'red', label = 'Omega_b')
plt.ylabel('Omega Total')
plt.xlabel('q_a')
plt.legend()
plt.show()


# Multiplicity for the N_A = 8, N_B = 4 and q = 6 case
q_a = 0
q_b = 6
Ohm_a.clear()
Ohm_b.clear()
np.delete(Ohm_tot,0)

for i in range(0,7):
    Ohm_a.append(Multiplicity(8, q_a))
    q_a += 1

for i in range(0,7):
    Ohm_b.append(Multiplicity(4, q_b))
    q_b -= 1

Ohm_tot = np.multiply(Ohm_a, Ohm_b)

data = {'q_a': qa, 'Omega_A': Ohm_a, 'q_b': qb, 'Omega_B': Ohm_b, 'Omega_Total': Ohm_tot}

df = pd.DataFrame(data)

print(df.to_string(index = False))

plt.bar(qa, Ohm_tot, label = 'Omega_Total')
plt.plot(qa, Ohm_a, color = 'yellow', label = 'Omega_a')
plt.plot(qa, Ohm_b, color = 'red', label = 'Omega_b')
plt.ylabel('Omega Total')
plt.xlabel('q_a')
plt.legend()
plt.show()

# Multiplicity for the N_A = 8, N_B = 4 and q = 100 case
q_a = 0
q_b = 100
Ohm_a.clear()
Ohm_b.clear()
np.delete(Ohm_tot,0)

for i in range(0,101):
    Ohm_a.append(Multiplicity(8, q_a))
    q_a += 1

for i in range(0,101):
    Ohm_b.append(Multiplicity(4, q_b))
    q_b -= 1

Ohm_tot = np.multiply(Ohm_a, Ohm_b)
qa_new = np.arange(0,101)

plt.bar(qa_new, Ohm_tot, label = 'Omega_Total')
plt.plot(qa_new, Ohm_a, color = 'yellow', label = 'Omega_a')
plt.plot(qa_new, Ohm_b, color = 'red', label = 'Omega_b')
plt.ylabel('Omega Total x 10^13')
plt.xlabel('q_a')
plt.legend()
plt.show()

# From these results, we observe that the system exhibits irreversible behaviour, where energy may flow 
# from B to A but not from A to B. From this we may deduce the Second Law of Thermodynamics, which states:
# The spontaneous flow of energy stops when a system is at, or very near its most likely macrostate. 
# That is the macrostate with the greatest multiplicity (Schroeder, 1999).
