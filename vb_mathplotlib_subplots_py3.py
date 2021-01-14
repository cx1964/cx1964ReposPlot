# File: vb_mathplotlib_subplots_py3.py
# Functie: Voorbeeld mbt het maken subplots (meerdere plots op 1 afbeelding)
# Documentatie: https://pythonprogramming.net/matplotlib-python-3-basics-tutorial/
# 
# Opmerking: voor gebruik van dit script met
#            visual code
#            set in settings: 
#            "python.pythonPath": "C:\\tmp\\cx1964ReposPlot\\env_python3_plot\\Scripts
#
#            indien mathplotlib nog niet geinstalleerd is run:
#            pip install mathplotlib
#
#            Nadat een grafiek wordt gelsoten wordt de volgende getoond.

from matplotlib import pyplot as plt

# Voorbeeld1: 1 grafieken in een afbeelding
x = [5,8,10]
y = [12,16,6]
plt.plot(x,y)
plt.title('Titel van de grafiek voorbeeld1')
plt.ylabel('Y-as')
plt.xlabel('X-as')
plt.show()


# Voorbeeld2: 2 grafieken in een afbeelding
#from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')
x1 = [0,1,2,3,4,5]
y1 = [0,1,4,9,16,25]
x2 = x1
y2 = [5,7,9,11,13,15]
# can plot specifically, after just showing the defaults:
plt.plot(x1,y1,linewidth=5, label='$f1(x)=x^2$', color='red')     # label maken gebruik van Latex express
plt.plot(x2,y2,linewidth=5, label='$f2(x)=2x+5$', color='green')  # label maken gebruik van Latex express
plt.title('Titel van de grafiek voorbeeld2')
plt.ylabel('Y-as')
plt.xlabel('X-as')
plt.legend()
plt.show()


# Voorbeeld3: 2 grafieken in een afbeelding met gebruik van lamda functie
#from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')
x= range(0, 50) # genereer x-waarden
f1 = list(map(lambda xi: xi**2 + 2*xi +5, x)) # functie definitie mbv een lambda functie
f2 = list(map(lambda xi: -2*xi+500, x))
# can plot specifically, after just showing the defaults:
plt.plot(x,f1,linewidth=5, label='$f1(x)=x^2+2x+5$', color='red')     # label maken gebruik van Latex express
plt.plot(x,f2,linewidth=5, label='$f2(x)=-2x+500$'  , color='green')  # label maken gebruik van Latex express
plt.title('Titel van de grafiek voorbeeld2')
plt.ylabel('Y-as')
plt.xlabel('X-as')
plt.legend()
plt.show()

# Voorbeeld4: 2 grafieken in 4 afbeelding (met subplot)
# https://www.tutorialspoint.com/matplotlib/matplotlib_subplots_function.htm
#import matplotlib.pyplot as plt

# subplots(nrows, ncols)
fig,a =  plt.subplots(2,2)
import numpy as np
x = np.arange(1,5,0.1)
a[0][0].plot(x,x*x)
a[0][0].set_title('square')

a[0][1].plot(x,np.sqrt(x))
a[0][1].set_title('square root')

a[1][0].plot(x,np.exp(x))
a[1][0].set_title('exp')

a[1][1].plot(x,np.log10(x))
a[1][1].set_title('log')

plt.show()


# Voorbeeld5: 2 grafieken in 4 afbeelding (met subplot)
# https://www.tutorialspoint.com/matplotlib/matplotlib_subplots_function.htm
import matplotlib.pyplot as plt

# subplots(nrows, ncols)
fig,a =  plt.subplots(2,2)
import numpy as np
x = np.arange(1,5,0.1)
a[0][0].plot(x,x*x)
a[0][0].set_title('square')

a[0][1].plot(x,np.sqrt(x))
a[0][1].set_title('square root')

a[1][0].plot(x,np.exp(x))
a[1][0].set_title('exp')

x=np.linspace(-2*np.pi, 2*np.pi, num=100) 
#print(x)
a[1][1].plot(x,np.sin(x))
a[1][1].set_title('cyclisch')

plt.show()
