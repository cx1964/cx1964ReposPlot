# File: vb_mathplotlib_subplots_py3.py
# Functie: Voorbeeld mbt het maken subplots (meerdere plots op 1 afbeelding)
# Documentatie: https://pythonprogramming.net/matplotlib-python-3-basics-tutorial/
# Opmerking: indien mathplotlib nog niet geinstalleerd is run:
#            pip install mathplotlib

from matplotlib import pyplot as plt

# Voorbeeld1
x = [5,8,10]
y = [12,16,6]
plt.plot(x,y)
plt.title('Titel van de grafiek voorbeeld1')
plt.ylabel('Y-as')
plt.xlabel('X-as')
plt.show()

# Voorbeeld2
#from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')
x1 = [0,1,2,3,4,5]
y1 = [0,1,4,9,16,25]
x2 = x1
y2 = [5,7,9,11,13,15]
# can plot specifically, after just showing the defaults:
plt.plot(x1,y1,linewidth=5, label='functie1', color='red')
plt.plot(x2,y2,linewidth=5, label='functie2', color='green')
plt.title('Titel van de grafiek voorbeeld2')
plt.ylabel('Y-as')
plt.xlabel('X-as')
plt.legend()
plt.show()