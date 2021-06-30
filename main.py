import pygame
import sys
import random

class Snek():
	def __init__(self):
		self.length=1
		self.positons=[((SCREEN_W/2),(SCREEN_H/2))]
		self.dir=random.choice([UP,DOWN,LEFT,RIGHT])
		self.color=(17, 24, 47)
		self.score=0

	def get_head_pos(self):
		return self.positons[0]

	def turn(self,point):
		if self.length > 1 and (point[0]*-1,point[1]*-1)==self.dir:
			return
		else:
			self.dir = point

	def move(self):
		cur=self.get_head_pos()
		x,y=self.dir
		new=(((cur[0]+(x*GRIDSIZE))%SCREEN_W),(cur[1]+(y*GRIDSIZE))%SCREEN_H)		
		if len(self.positons) > 2 and new in self.positons[2:]:
			self.reset()
		else:
			self.positons.insert(0,new)
			if len(self.positons) > self.length:
				self.positons.pop()

	def reset(self):
		self.length=1
		self.positons=[((SCREEN_W/2),(SCREEN_H/2))]
		self.dir=random.choice([UP,DOWN,LEFT,RIGHT])
		self.score=0

	def draw(self,surface):
		for p in self.positons:
			r=pygame.Rect((p[0],p[1]),(GRIDSIZE,GRIDSIZE))
			pygame.draw.rect(surface,self.color,r)
			pygame.draw.rect(surface,(93,216,228),r,1)

	def handle_keys(self):
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type==pygame.KEYDOWN:
				if event.key==pygame.K_UP:
					self.turn(UP)
				elif event.key==pygame.K_DOWN:
					self.turn(DOWN)
				elif event.key==pygame.K_LEFT:
					self.turn(LEFT)
				elif event.key==pygame.K_RIGHT:
					self.turn(RIGHT)
				elif event.key==pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()


class Food():
	def __init__(self):
		self.pos=(0,0)
		self.color=(223,163,49)
		self.rand_pos()

	def rand_pos(self):
		self.pos=(random.randint(0,GRID_W-1)*GRIDSIZE,random.randint(0,GRID_H-1)*GRIDSIZE)

	def draw(self, surface):
		r=pygame.Rect((self.pos[0],self.pos[1]),(GRIDSIZE,GRIDSIZE))
		pygame.draw.rect(surface,self.color,r)
		pygame.draw.rect(surface,(93,216,228),r,1)

def drawGrid(surface):
	for y in range(0,int(GRID_H)):
		for x in range(0,int(GRID_W)):
			if (x+y)%2==0:
				r=pygame.Rect((x*GRIDSIZE,y*GRIDSIZE),(GRIDSIZE,GRIDSIZE))
				pygame.draw.rect(surface,(93,216,228),r)
			else:
				rr=pygame.Rect((x*GRIDSIZE,y*GRIDSIZE),(GRIDSIZE,GRIDSIZE))
				pygame.draw.rect(surface,(84,194,205),rr)

SCREEN_W=480
SCREEN_H=480

GRIDSIZE=20
GRID_W=SCREEN_H/GRIDSIZE
GRID_H=SCREEN_W/GRIDSIZE

UP=(0,-1)
DOWN=(0,1)
LEFT=(-1,0)
RIGHT=(1,0)

def main():
	pygame.init()

	clock=pygame.time.Clock()
	screen=pygame.display.set_mode((SCREEN_W,SCREEN_H),0,32)

	surface=pygame.Surface(screen.get_size())
	surface=surface.convert()
	drawGrid(surface)

	snek=Snek()
	food=Food()

	myfont=pygame.font.SysFont('monospace',16)

	score=0
	while(True):
		clock.tick(10)
		snek.handle_keys()
		drawGrid(surface)
		snek.move()
		if snek.get_head_pos()==food.pos:
			snek.length+=1
			score+=1
			food.rand_pos()
		snek.draw(surface)
		food.draw(surface)
		screen.blit(surface,(0,0))
		text=myfont.render('Score: {0}'.format(score),1,(0,0,0))
		screen.blit(text,(5,10))
		pygame.display.update()

main()