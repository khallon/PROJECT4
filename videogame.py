import pygame
import random
pygame.init()
pygame.mixer.init()


from pygame.locals import Rect, DOUBLEBUF, QUIT, K_ESCAPE, KEYDOWN, K_DOWN, \
    K_LEFT, K_UP, K_RIGHT, KEYUP, K_LCTRL, K_RETURN, K_w, K_a, K_s, K_d, K_SPACE, FULLSCREEN

white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
cyan = (0,255,255)

display_width = 1400
display_height = 600

FPS = 30 #Setting the pixels

bg = pygame.image.load("background.png")

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
	def shoot(self):
		cannon = Cannon(self.rect.centerx, self.rect.top)
		all_sprites.add(cannon)
		bullets.add(cannon)
		
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

globalhordespeed = 0 			
 			
class horde(pygame.sprite.Sprite):
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('enemy.bmp')
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(display_width - self.rect.width)
		self.rect.y = random.randrange(-100, - 40)
		self.randx = random.uniform(-5,5)
		self.randy = random.uniform(0.35,2.2)
		self.x_speed = self.randx
		self.y_speed = self.randy 
		
	def update (self):
		self.rect.x += self.x_speed
		self.rect.y += self.y_speed + globalhordespeed
		if self.rect.top > display_height + 10:
			self.rect.x = random.randrange(display_width - self.rect.width)
			self.rect.y = random.randrange(-100, -40)
			self.y_speed = 5 #random.randrange(1, 10)
	#def paralyse (self):
	
		#its = pygame.sprite.spritecollide(horde, bullets, True)
		#if hits: 
			#self.x_speed= 0
			#self.y_speed = 0
			#self.rect.center = display_width/2 
			#self.rect.center = display_height/2
			
#globalhordespeed = horde.randy
			
class Cannon(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((5,20))
		self.image.fill(red)
		self.rect = self.image.get_rect()
		self.rect.bottom = y 
		self.rect.centerx = x
		self.speed = -10
		self.explosion_sound = pygame.mixer.Sound("pew.wav")
		self.explosion_sound.set_volume(0.05)
		sounds.append(self.explosion_sound)
	
	def update (self):
		self.rect.y +=self.speed
		if pygame.mixer.get_init():
			self.explosion_sound.play(maxtime=500)
				
		if self.rect.bottom < 0:
			self.kill()
			
#class Shield(pygame.sprite.Sprite)
			
		

#Setting the title
pygame.display.set_caption('A Rather Dramatic Game')


#Setting the internal clock
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

hordes = pygame.sprite.Group()

bullets = pygame.sprite.Group()

player = Player()
player2 = Player2()
all_sprites.add(player)
all_sprites.add(player2)


for i in range(150):
	h = horde()
	hordes.add(h)
	all_sprites.add(h)

#All game logic will come here!


Img = pygame.image.load('Blinky.png')

running = True

fortuna = pygame.mixer.Sound("ofortuna.wav")
fortuna.set_volume(0.6)

sounds = []
sounds.append(fortuna)

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
if pygame.mixer.get_init():
	fortuna.play(maxtime=100000)

while running: 
	gameDisplay.blit(bg, (0,0))
	
	
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
			if event.key == K_SPACE:
				player.shoot()

	   

		if event.type == pygame.KEYUP:
			if event.key == K_LEFT or event.key == K_RIGHT:
				player.x_speed = 0
			if event.key == K_UP or event.key== K_DOWN:
				player.y_speed = 0
			if event.key == K_a or event.key == K_d:
				player2.x_speed = 0
			if event.key == K_w or event.key== K_s:
				player2.y_speed = 0	
 
				
		
	#Update
	all_sprites.update()
	
	hits = pygame.sprite.spritecollide(player, hordes, True)
			
		
	hits2 = pygame.sprite.spritecollide(player2, hordes, False)
	hits3 = pygame.sprite.groupcollide(bullets, hordes, True, True)
	if hits3:
		globalhordespeed += (len(hits3.values())* 0.05)
		
	all_sprites.update()
	
			
	#Draw
	#gameDisplay.fill(cyan)
		
	all_sprites.draw(gameDisplay)
		
							
	pygame.display.flip() # WATCH OUT FOR THIS	2nd tut
	#pygame.display.update()
	clock.tick(60) #This is effectively just frame rate. Right now it is at 30 fps


#game()		
	
pygame.quit()