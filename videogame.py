#This is a two-player game in which both players must work together to achieve their highest score.
#One player uses the arrow keys and space bar in order to attack enemies by shooting at them.
#The other player uses 'w, a, s, d, lctrl' in order to defend the other player

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

display_width = 1000
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
		self.image = pygame.image.load('spaceship.png')
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
		self.image = pygame.image.load('arrow.bmp')
		self.image.set_colorkey(black)
		self.radius = 63
		
		self.rect = self.image.get_rect()
		self.rect.center = (display_width/2, display_height/2)
		pygame.draw.circle(self.image, red, self.rect.center, self.radius)
		

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
	def shield(self):
		shield = Shield(self.rect.centerx, self.rect.top)
		all_sprites.add(shield)
		shieldgroup.add(shield)
		#if pygame.mixer.get_init():
		#	self.shield_sound.play(maxtime = 200)

globalhordespeed = 0 			
 			
class horde(pygame.sprite.Sprite):
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('enemy.bmp')
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(display_width - self.rect.width)
		self.rect.y = random.randrange(-100, - 40)
		
		self.randx = random.uniform(-2,2)
		self.randy = random.uniform(0.8,2.2)
		self.x_speed = self.randx
		self.y_speed = self.randy 
		
	def update (self):
		self.rect.x += self.x_speed
		self.rect.y += self.y_speed + globalhordespeed
		if self.rect.top > display_height + 10: #or self.rect.right > display_width or self.rect.left < display_width:
			self.rect.x = random.randrange(display_width - self.rect.width)
			self.rect.y = random.randrange(-100, -40)
			self.y_speed =random.randrange(1, 10)
		
		
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
		
	
	def update (self):
		self.rect.y +=self.speed
		if pygame.mixer.get_init():
			self.explosion_sound.play(maxtime=200)
				
		if self.rect.bottom < 0:
			self.kill()


	
			
class Shield(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((50,5))
		self.image.fill(green)
		self.rect = self.image.get_rect()
		self.rect.bottom = y
		self.rect.centerx = x
		self.shield_sound = pygame.mixer.Sound('shield.wav')
		self.shield_sound.set_volume(0.2)
		if pygame.mixer.get_init():
			self.shield_sound.play(maxtime = 400)
	#def update (self):
		#self.rect.bottom = y
		#self.rext.centerx = x
		
		
		
			
		

#Setting the title
pygame.display.set_caption('A Rather Dramatic Game')


#Setting the internal clock
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

players = pygame.sprite.Group()

hordes = pygame.sprite.Group()

bullets = pygame.sprite.Group()

shieldgroup = pygame.sprite.Group()

player = Player()
player2 = Player2()

players.add(player)
players.add(player2)
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
fortuna.set_volume(1.0)

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
if pygame.mixer.get_init():
	fortuna.play(maxtime=100000)
	

score = 0

font1 = pygame.font.match_font('impact')			
def drawscore(text, size):
	font = pygame.font.Font(font1, size)
	text = font.render(text, True, white)
	text_rect = text.get_rect()
	text_rect.midtop = (display_width/2, 0 ) 
	gameDisplay.blit(text, text_rect)

def shieldstatus(text, size):
	font = pygame.font.Font(font1,18)
	text = font.render(text, True, red)
	text_rect = text.get_rect()
	text_rect.topleft = (0,0)
	gameDisplay.blit(text, text_rect)
	
shields = 20

player1lives = 20
player2lives = 20

def lifestatus(text, size):
	font = pygame.font.Font(font1,18)
	text = font.render(text, True, white)
	text_rect = text.get_rect()
	text_rect.bottomleft = (0,display_height)
	gameDisplay.blit(text, text_rect)
	
def lifestatus2(text, size):
	font = pygame.font.Font(font1,18)
	text = font.render(text, True, white)
	text_rect = text.get_rect()
	text_rect.bottomright = (display_width,display_height)
	gameDisplay.blit(text, text_rect)

def endgame(text, size):
	font = pygame.font.Font(font1,50)
	text = font.render(text, True, red)
	text_rect = text.get_rect()
	text_rect.center = (display_width/2,display_height/2)
	gameDisplay.blit(text, text_rect)
	
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
			if event.key == K_LCTRL:
				if shields > 0:
					player2.shield()
					shields -= 1
					

	   

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
			
		
	hits2 = pygame.sprite.spritecollide(player2, hordes, True)
	
		
	hits3 = pygame.sprite.groupcollide(bullets, hordes, True, True)
	hits4 = pygame.sprite.groupcollide(shieldgroup, hordes, True, True)
	#hits5 = 
	if hits3:
		globalhordespeed += (len(hits3.values())* 0.05)
		score += 1
	
	scorestring = "Your score is " + str(score)
		
	all_sprites.update()
	
	
	
	shieldstring = "You have " + str(shields) + " shields left"
	
	if hits:
		if player1lives > 0:
			player1lives -= 1
	
	if hits2:
		if player2lives > 0:
			player2lives -= 1
	lifestring1 = "Player 1 has " + str(player1lives) + " lives remaining"
	lifestring2 = "Player 2 has " + str(player2lives) + " lives remaining"
	lifestatus(lifestring1, 20)
	lifestatus2(lifestring2, 20)
	endgametext = "This is the end of the road, Your final score is " + str(score)
			
	
	all_sprites.draw(gameDisplay)
	
	drawscore(scorestring, 20)
	shieldstatus(shieldstring, 20)
	if player1lives == 0 and player2lives == 0:
		
		endgame(endgametext, 50)
		all_sprites.empty()
		#all_sprites.kill()
	
							
	pygame.display.flip() # WATCH OUT FOR THIS	2nd tut
	#pygame.display.update()
	clock.tick(60) #This is effectively just frame rate. Right now it is at 30 fps
	#if len(hordes) = 0:
	#	running = False
		

print (score)
#game()		
	
pygame.quit()