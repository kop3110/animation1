import matplotlib.pyplot as pyplot
import matplotlib.animation as animation
import numpy as np
import random
import time

class Scatter_animation(object):
	def __init__(self, sleep=False):
		self.tol = 0.5
		self.x = 1.0
		self.y = 1.0
		self.shmeia = 150
		self.kykloi = 4
		self.xronos = self.kykloi * np.pi
		self.x1 = np.linspace(0, self.xronos, self.shmeia)
		self.x2= np.sin(self.x1) * self.kykloi + self.xronos/1.5
		self.y1 = np.sin(self.x1)
		self.y2 = np.cos(self.x1)
		self.y3 = np.tan(self.x1)/4
		self.y4 = (1-self.x1*self.x1)**(1/2)
		self.y5=np.cos(self.x1)*np.sin(self.x1)
		self.y6=np.cos(self.x1)*np.sin(self.x1)/(np.cos(self.x1)-np.sin(self.x1))
		self.y7=1-np.sin(self.x2)
		self.xwork = np.copy(self.x1)
		self.ywork = np.copy(self.y1)
		self.mode = 1
		self.ylist = [(self.x1, self.y1), (self.x1, self.y2), (self.x1, self.y3),(self.x1, self.y5),(self.x2, self.y7)]
		self.clist = [1, 1, 0.2,0.1,0.15]
		self.fig = pyplot.figure()
		self.ax = self.fig.add_subplot(111)
		self.ani = animation.FuncAnimation(self.fig, self.update, interval=10,init_func=self.setup_plot, blit=True,repeat=False)
		random.seed()
		self.first = sleep
	def setup_plot(self):
		self.ax.axis([-1, self.xronos+1, -self.y*1.1, self.y*1.1])
		self.scat = self.ax.scatter(self.xwork, self.ywork, c="RED", s=100, animated=True)
		self.ax.set_title("TEAM 7 ANIMATION",fontsize=14)
		pyplot.style.use('ggplot')
		return self.scat,  
	
	def update(self, i):
		if self.first:
			time.sleep(50)
			self.first = False
		self.xwork = self.analog_filter(self.xwork, self.ylist[self.mode][0],self.clist[self.mode])
		self.ywork = self.analog_filter(self.ywork, self.ylist[self.mode][1],self.clist[self.mode])
		if np.allclose((self.xwork, self.ywork), self.ylist[self.mode], atol=self.tol):
			mode = self.mode
			while mode == self.mode:
			 mode = random.randrange(0, len(self.ylist), 1)
			self.mode = mode	
		colors = ["red", "orange", "yellow", "green", "blue", "violet"]
		self.scat = self.ax.scatter(self.xwork, self.ywork, c=random.choice(colors), s=100, animated=True)
		return self.scat,
	def show(self):
		pyplot.show()
	def analog_filter(self, old, new, factor=0.2):
		old = old * (1.0 - factor) + new * factor
		return old

def main():
	a = Scatter_animation()
	a.show()
if __name__ == '__main__':
	main()
			
			
			
			
			
			
			
			
			
			
			
			