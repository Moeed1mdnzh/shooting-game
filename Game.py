import pygame,time
import menu
import random as r
from math import *


class Game(menu.Menu):
	def __init__(self,deff):
		super().__init__()
		self.lives = "10"
		self.waveNum = "1"
		self.scoreNum = "0"
		self.Pcolor = deff
		self.Texts = [f"score : {self.scoreNum}",f"wave : {self.waveNum}",f"lives : {self.lives}",f"prepare for wave number {self.waveNum}"]
		self.font = pygame.font.SysFont("arial",30,"light")
		self.Tcrdnts = [(0,0),(0,30),(0,60)]
		self.Pradius = 30
		self.Pxy = [400,605]
		self.dead = False
		self.LineXy = [[400,590],[400,550]]
		self.Lcolor = (252, 65, 3)
		self.key = None
		self.bttns = None
		self.center = [400,590]
		self.vector = [1,1]
		self.angle = None
		self.endPoint = None
		self.Cep = None
		self.vector2 = None
		self.shootS = 120
		self.get = False
		self.lineL = None
		self.dis = None
		self.xs =self.ys = None
		self.xytest = None
		self.num = 0
		self.Eradius = 40
		self.Ecolor = None
		self.details = []
		self.Espeed = 2
		self.height = -400
		self.Enum = 20
		self.loss_text = "YOU LOST"
		self.new_wave = True
		self.Wfont = pygame.font.SysFont("arial",30,"light")
	def keys(self):
		self.key = pygame.key.get_pressed()
		self.bttns = {pygame.K_d:50,pygame.K_a:-50}
		for s in self.bttns.items():
			if self.key[s[0]]:
				self.Pxy[0] += s[1]
				self.LineXy[0][0] += s[1]
				self.LineXy[1][0] += s[1]
				self.center[0] += s[1]
			if self.Pxy[0] < 0:
				self.Pxy = [800,605]
				self.LineXy = [[800,590],[800,550]]
				self.center = [800,590]
			elif self.Pxy[0] > 800:
				self.Pxy = [0,605]
				self.LineXy = [[0,590],[0,550]]
				self.center = [0,590]
	def wave(self):
		if self.details == []:
			self.new_wave = True
			if self.Eradius != 4:
				self.Eradius -= 1
			self.Espeed += 2
			self.height -= 400
			self.waveNum = str(int(self.waveNum)+1)
			self.win.fill((0,0,0))
			self.Texts = [f"score : {self.scoreNum}",f"wave : {self.waveNum}",f"lives : {self.lives}",f"prepare for wave number {self.waveNum}"]
			self.win.blit(pygame.font.SysFont("arial",30,"light").render(self.Texts[3],True,(180,0,0)),(200,270))
			self.refresh()
			time.sleep(4)

	def display_T(self):
		for i in range(3):
			self.test = self.font.render(self.Texts[i],True,(255,255,255))
			self.win.blit(self.test,self.Tcrdnts[i])

	def display_E(self):
		for i in range(len(self.details)):
			self.details[i][1] += self.Espeed
			self.details[i][0] += r.randint(-10,10)
			if self.details[i][0] not in range(0,800):
				self.details[i][0] = 400
			pygame.draw.circle(self.win,self.Ecolor,(self.details[i][0],self.details[i][1]),self.Eradius)
	def enemy_gen(self):
		if self.new_wave:
			self.Ecolor = (r.randint(1,255),r.randint(1,255),r.randint(1,255))
			for i in range(self.Enum):
				self.details.append([r.randint(1,799),r.randint(self.height,1)])
			self.new_wave = False
				
	def Score(self):
		for i,v in enumerate(self.details):
			if int(self.xs+self.xytest[0]) in range(v[0]-self.Eradius,v[0]+self.Eradius) and int(self.ys+self.xytest[1]) in range(v[1]-self.Eradius,v[1]+self.Eradius):
				self.scoreNum = str(int(self.scoreNum)+1)
				self.Texts = [f"score : {self.scoreNum}",f"wave : {self.waveNum}",f"lives : {self.lives}",f"prepare for wave number {self.waveNum}"]
				self.details.remove(v)			
	def lose(self):
		if int(self.lives) <= 0:
			self.win.fill((0,0,0))
			self.win.blit(pygame.font.SysFont("arial",35,"light").render(self.loss_text,True,(255,255,255)),(300,200))
			self.Texts = [f"score : {self.scoreNum}",f"wave : {self.waveNum}",f"lives : {self.lives}",f"prepare for wave number {self.waveNum}"]
			for i in range(3):
				self.win.blit(self.font.render(self.Texts[i],True,(255,255,255)),(320,240+i*40))
			self.refresh()
			time.sleep(5)
			m = menu.Menu()
			st = m.main()
			if st[0]:
				g = Game(st[1])
				g.gameLoop()
		for i,v in enumerate(self.details):
			if v[1] > 600:
				self.lives = str(int(self.lives)-1)
				self.details.remove(v)
			self.Texts = [f"score : {self.scoreNum}",f"wave : {self.waveNum}",f"lives : {self.lives}"]
	def dirc(self):
		if self.vector[0] != 0 or self.vector[1] != 0:
			try:
				self.pos = pygame.mouse.get_pos()
				self.vector = [self.LineXy[0][0]-self.pos[0],self.LineXy[0][1]-self.pos[1]]
				self.angle = int(degrees(atan(self.vector[1]/self.vector[0])))
				if self.angle < 0:
					self.angle += 180
				self.LineL = 40
				self.vector2 = pygame.math.Vector2(-self.LineL,0)
				self.Cep = self.LineXy[0] + self.vector2.rotate(self.angle)
				self.LineXy[1] = self.Cep
			except:
				pass
			



	def shoot(self):
		self.xs = self.LineXy[1][0]
		self.ys = self.LineXy[1][1]
		self.pos = pygame.mouse.get_pos()
		self.dis = [self.pos[0]-self.xs,self.pos[1]-self.ys]
		self.xytest = [self.dis[0]/4,self.dis[1]/4]
		while self.num <= 4:
			self.fill()
			self.delay(60)
			self.keys()
			self.enemy_gen()
			self.display_E()
			self.display_T()
			self.player()
			self.dirc()
			self.lose()
			self.Texts = [f"score : {self.scoreNum}",f"wave : {self.waveNum}",f"lives : {self.lives}",f"prepare for wave number {self.waveNum}"]
			self.Score()
			self.wave()
			self.xs += self.xytest[0]
			self.ys += self.xytest[1]
			pygame.draw.line(self.win,(255,255,0),(int(self.xs),int(self.ys)),(int(self.xs+self.xytest[0])
				,(self.ys+self.xytest[1])),2)
			self.quit()
			self.refresh()
			self.num += 1
		self.num = 0

	def fill(self):
		self.win.fill((0,0,0))
	def player(self):
		pygame.draw.circle(self.win,self.Pcolor,self.Pxy,self.Pradius)
		pygame.draw.line(self.win,self.Lcolor,self.LineXy[0],self.LineXy[1],3)
		pygame.draw.circle(self.win,self.Lcolor,self.center,self.Pradius//6)
	def gameLoop(self):
		while not self.dead:
			self.fill()
			self.delay(60)
			self.keys()
			self.enemy_gen()
			self.display_E()
			self.display_T()
			self.player()
			self.dirc()
			self.lose()
			self.shoot()
			self.Texts = [f"score : {self.scoreNum}",f"wave : {self.waveNum}",f"lives : {self.lives}",f"prepare for wave number {self.waveNum}"]
			self.Score()
			self.quit()
			self.refresh()
			self.wave()


if __name__ == "__main__":
	m = menu.Menu()
	st = m.main()
	if st[0]:
		g = Game(st[1])
		g.gameLoop()
