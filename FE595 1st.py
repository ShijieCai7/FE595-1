##import needed packages
import matplotlib.pyplot as plt
import numpy as np
##define period and define functions
x = np.arange(0,2*np.pi,0.1)
y = np.sin(x)
z = np.cos(x)
##plot them and add labels
plt.plot(x,y,x,z)
plt.xlabel('0 to 2pi')
plt.ylabel('sin(x) and cos(x)')
plt.title('Plot of sin and cos form 0 to 2pi')
plt.legend(['sin(x)','cos(x)'])
plt.show()



