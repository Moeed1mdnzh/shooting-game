import pygame
import random
pygame.init()



class Menu:
	def __init__(self):
		global W,H
		pygame.display.set_caption("defender")
		self.win = pygame.display.set_mode((W,H))
		self.pos = None
		self.deff = (255,255,255)
		self.texts = ["Start","Themes","Quit"]
		self.ys = [50,170,250]
		self.test = None
		self.crdnts = []
		self.colors = []
		self.radius = []
		self.Pcolor = (255,255,255)
		self.sizes = [80,40,40]
		self.num = random.randint(10,20)
		for i in range(self.num):
			self.colors.append((random.randint(1,255),random.randint(1,255),random.randint(1,255)))
			self.crdnts.append([random.randint(0,600),random.randint(0,800)])
			self.radius.append(random.randint(10,30))
	def display(self,text,xy,color,size):
		self.test = self.font(size).render(text,True,color)
		self.win.blit(self.test,(xy[0],xy[1]))
	def balls(self,coordinates,color,radius):
		pygame.draw.circle(self.win,color,coordinates,radius)
	def font(self,size):
		return pygame.font.SysFont("arial",size,"light")
	def refresh(self):
		pygame.display.update()
	def quit(self):
		for event in pygame.event.get():
			if event == pygame.QUIT:
				pygame.quit()
				quit()
	def line(self):
		pygame.draw.line(self.win,(240,240,240),(0,127),(200,127),8)
	def delay(self,time):
		pygame.time.delay(time)
	def mouse(self):
		self.pos = pygame.mouse.get_pos()
		if self.pos[0] in range(0,250) and self.pos[1] in range(50,150):
			pygame.draw.rect(self.win,(255,255,0),(0,50,250,100),8)
		elif self.pos[0] in range(0,250) and self.pos[1] in range(150,250):
			pygame.draw.rect(self.win,(255,255,0),(0,150,250,80),8)
		elif self.pos[0] in range(0,250) and self.pos[1] in range(250,300):
			pygame.draw.rect(self.win,(255,255,0),(0,243,250,60),8)
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				if pygame.mouse.get_pressed()[0]:
					if self.check():
						return True
					elif self.check() == False:
						t = Theme()
						self.deff = t.Main()
					elif self.check() == None:
						pygame.quit()
						quit()
						
	def check(self):
		if self.pos[0] in range(0,250) and self.pos[1] in range(50,150):
			return True
		elif self.pos[0] in range(0,250) and self.pos[1] in range(150,250):
			return False
		elif self.pos[0] in range(0,250) and self.pos[1] in range(250,300):
			return None
	def main(self):
		while True:
			self.win.fill((0,0,0))
			self.delay(100)
			for i in range(self.num):
				self.crdnts[i][1] += 30
				if self.crdnts[i][1] > 620:
					self.crdnts[i] = [random.randint(0,600),random.randint(-20,0)]
					self.colors[i] = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
					self.radius[i] = random.randint(10,30)
				self.balls(self.crdnts[i],self.colors[i],self.radius[i])
			for i in range(3):
				self.display(self.texts[i],(0,self.ys[i]),(255,255,255),self.sizes[i])
			self.line()
			self.dec = self.mouse()
			if self.dec:
				return True,self.deff
			self.quit()
			self.refresh()

class Theme(Menu):
	def __init__(self):
		super().__init__()
		self.win.fill((0,0,0))
		self.font = pygame.font.SysFont("arial",40,"light")
		self.text = "select"
		self.index = 0
		self.render = None
		self.colors = [(255,255,255),(0,0,255),(255,0,0),(0,255,0),
		(255,255,0),(0,255,255),(255,0,255),(40,40,40)]
		self.default = self.colors[self.index]
		self.radius = 100
		self.leave = False
	def half_circle(self):
		pygame.draw.circle(self.win,self.default,[400,590],self.radius)
		pygame.draw.circle(self.win,(252, 65, 3),[400,590],self.radius//6)
		pygame.draw.line(self.win,(252, 65, 3),[400,590],[400,420],8)
		pass
	def switch(self):
		pygame.draw.polygon(self.win,self.colors[0],[(80,500),(180,470),(180,530)])
		pygame.draw.polygon(self.win,self.colors[0],[(720,500),(620,470),(620,530)])
		self.pos = pygame.mouse.get_pos()
		if self.pos[0] in range(80,180) and self.pos[1] in range(470,530):
			pygame.draw.rect(self.win,(255,255,0),(80,470,100,60),6)
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					if pygame.mouse.get_pressed()[0]:
						if self.index != 0:
							self.index -= 1
							self.default = self.colors[self.index]
						else:
							self.index = 7
							self.colors[self.index]
		elif self.pos[0] in range(620,720) and self.pos[1] in range(470,530):
			pygame.draw.rect(self.win,(255,255,0),(620,470,100,60),6)
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					if pygame.mouse.get_pressed()[0]:
						if self.index != 7:
							self.index += 1
							self.default = self.colors[self.index]
						else:
							self.index = 0
							self.colors[self.index]
		elif self.pos[0] in range(333,463) and self.pos[1] in range(200,250):
			pygame.draw.rect(self.win,(255,255,0),(333,200,130,50),5)
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					if pygame.mouse.get_pressed()[0]:
						self.leave = True
	def select(self):
		self.render = self.font.render(self.text,True,(255,255,255))
		self.win.blit(self.render,(343,200))
		pygame.draw.rect(self.win,(255,255,255),(333,200,130,50),5)
	def Main(self):
		while True:
			self.win.fill((0,0,0))
			self.select()
			self.switch()
			self.half_circle()
			self.quit()
			self.refresh()
			if self.leave:
				return self.default

W,H = 800,600

