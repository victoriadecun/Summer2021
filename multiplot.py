import matplotlib.pyplot as plt
import numpy as np

'''
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)
x2 = np.linspace(0, 2 * np.pi, 400)
y2 = np.sin(x ** 2)
x3 = np.linspace(0, 2 * np.pi, 400)
y3 = np.sin(x ** 2)
x4 = np.linspace(0, 2 * np.pi, 400)
y4 = np.sin(x ** 2)
'''

x,y  = np.loadtxt('plot1.data', delimiter=',', unpack=True)
x2,y2 = np.loadtxt('plot2.data', delimiter=',', unpack=True)
x3,y3 = np.loadtxt('plot3.data', delimiter=',', unpack=True)
x4,y4 = np.loadtxt('plot4.data', delimiter=',', unpack=True)


fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(x, y, 'tab:blue')
#axs[0, 0].set_title('Axis [0, 0]')
axs[0,0].set_ylabel('y-label')
#axs[0,0].legend('z = 2', handlelength=2)
axs[0,0].text(300,400,  'z = 2', fontsize=12)

axs[0, 1].plot(x2, y2, 'tab:orange')
#axs[0, 1].set_title('Axis [0, 1]')


axs[1, 0].plot(x3, y3, 'tab:green')
#axs[1, 0].set_title('Axis [1, 0]')
axs[1,0].set_ylabel('y-label')
axs[1,0].set_xlabel('x-label')

axs[1, 1].plot(x4, y4, 'tab:red')
#axs[1, 1].set_title('Axis [1, 1]')
axs[1,1].set_xlabel('x-label')

#for ax in axs.flat:
 #   ax.set(xlabel='x-label', ylabel='y-label')



plt.show()
