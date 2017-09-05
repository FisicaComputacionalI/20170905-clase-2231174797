import matplotlib.pyplot as plt
x = [5000,6000,7000,8000,9000]
y = [65,78,88,89,93]
plt.plot(x, y, 'r')
x1 = [7000,8000,9000,10000,11000]
y1 = [65,75,85,86,90]
plt.plot(x1, y1,'b-.')
plt.xlabel('Voltaje[V]')
plt.ylabel('Eficiencia[%]')
plt.savefig('temp4.png')

