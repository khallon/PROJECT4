import pygame
import random
pygame.init()
pygame.mixer.init()


from pygame.locals import Rect, DOUBLEBUF, QUIT, K_ESCAPE, KEYDOWN, K_DOWN, \
    K_LEFT, K_UP, K_RIGHT, KEYUP, K_LCTRL, K_RETURN, K_w, K_a, K_s, K_d, FULLSCREEN

white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
cyan = (0,255,255)

display_width = 800
display_height = 600

FPS = 30 #Setting the pixels

#Classes
gameDisplay = pygame.display.set_mode((display_width,display_height))
class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		#self.image = pygame.Surface((50,50))
		#self.image.fill(green)
		self.image = pygame.image.load('Blinky.png')
		self.image.set_colorkey()
		self.rect = self.image.get_rect()
		self.rect.center = (display_width/2, display_height/2)
		self.x_speed = 0
		self.y_speed = 0
		
	def update(self):
		
		self.rect.x += self.x_speed
		self.rect.y += self.y_speed
		if self.rect.right > display_width:
			self.rect.right = display_width
		if self.rect.bottom > display_height:
			self.rect.bottom = display_height
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.top < 0:
			self.rect.top = 0
			
class Player2(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		#self.image = pygame.Surface((50,50))
		#self.image.fill(green)
		self.image = pygame.image.load('arrow.png')
		self.image.set_colorkey(black)
		self.rect = self.image.get_rect()
		self.rect.center = (display_width/2, display_height/2)
		

		self.x_speed = 0
		self.y_speed = 0
	def update(self):
		self.rect.x += self.x_speed
		self.rect.y += self.y_speed	
		if self.rect.right > display_width:
			self.rect.right = display_width
		if self.rect.bottom > display_height:
			self.rect.bottom = display_height
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.top < 0:
			self.rect.top = 0

class horde(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

#Setting the title
pygame.display.set_caption('A rather whimsical game')


#Setting the internal clock
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

player = Player()
player2 = Player2()
all_sprites.add(player)
all_sprites.add(player2)

#All game logic will come here!


Img = pygame.image.load('Blinky.png')

#Make the image show up]
def car(x,y):
	gameDisplay.blit(Img, (x,y))
	
running = True

while running: 
	for event in pygame.event.get():
			
		if event.type == pygame.QUIT:
			running = False
			
		if event.type == pygame.KEYDOWN:
			if event.key == K_UP:
				player.y_speed -= 10	 
			if event.key == K_DOWN:
				player.y_speed += 10
			if event.key == K_LEFT:
				player.x_speed -= 10
			if event.key == K_RIGHT:
				player.x_speed += 10
			if event.key == K_w:
				player2.y_speed -= 20
			if event.key == K_s:
				player2.y_speed += 20
			if event.key == K_a:
				player2.x_speed-= 20
			if event.key == K_d:
				player2.x_speed += 20
	   

		if event.type == pygame.KEYUP:
			if event.key == K_LEFT or event.key == K_RIGHT:
				player.x_speed = 0
			if event.key == K_UP or event.key== K_DOWN:
				player.y_speed = 0
			if event.key == K_a or event.key == K_d:
				player2.x_speed = 0
			if event.key == K_w or event.key== K_s:
				player2.y_speed = 0	

				
		player.update()	
	#Update
	all_sprites.update()
	
		
	#Draw
	gameDisplay.fill(cyan)
		
	all_sprites.draw(gameDisplay)
		
		
	#car(x,y)
							
	pygame.display.flip() # WATCH OUT FOR THIS	2nd tut
	#pygame.display.update()
	clock.tick(30) #This is effectively just frame rate. Right now it is at 30 fps


#game()		
	
pygame.quit()