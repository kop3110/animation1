import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random
import os

#omada7-lakiotis klimis,mpessa anastasia,pittas konstantinos,stasinoulias dimitris

class Scatter(object):
    def __init__(self, shmeia=80):
        self.shmeia = shmeia
        self.stream = self.stream()
        self.fig, self.ax = plt.subplots()
        self.ani = animation.FuncAnimation(self.fig, self.update, interval=300,init_func=self.plot, blit=True)

        #Dhmiourgia xwrou diagrammatos

    def plot(self):
        x, y, s, c = next(self.stream)
        #Ta colors kai ta markers dialegontai me thn synarthsh random tyxaia kata thn ektelesh tou programmatos
        colors = ["red", "orange", "yellow", "green", "blue", "violet"]
        markers = ['s', 'o', 'h', '+']
        self.scat = self.ax.scatter(x, y, marker=random.choice(markers), c=random.choice(colors),s=s, animated=True)
        self.ax.axis([-10, 10, -10, 10])
        self.ax.set_axis_bgcolor(random.choice(colors))
        self.ax.set_title("TEAM 7 ANIMATION",fontsize=14)
        return self.scat,
    
    


    def stream(self):
        data = np.random.random((4, self.shmeia))
        xy = data[:2, :]
        s, c = data[2:, :]
        xy -= 0.5
        xy *= 10
        while True:
            xy += 0.5 * (np.random.random((2, self.shmeia)) - 0.5)
            s += 0.8 * (np.random.random(self.shmeia) - 0.5)
            c += 0.3 * (np.random.random(self.shmeia) - 0.5)
            yield data

    def update(self, i):
        data = next(self.stream)
        self.scat.set_offsets(data[:2, :])
        self.scat._sizes = 150 * abs(data[2])**2 + 80
        self.scat.set_array(data[3])
        return self.scat,

if __name__ == '__main__':
    a = Scatter()
    c=os.path.expanduser('~//public_html')
    a.ani.save(c+"//basic_animation5.mp4", fps=10)