import pygame
pygame.init()

from pygame.locals import Rect, DOUBLEBUF, QUIT, K_ESCAPE, KEYDOWN, K_DOWN, \
    K_LEFT, K_UP, K_RIGHT, KEYUP, K_LCTRL, K_RETURN, FULLSCREEN

white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

display_width = 800
display_height = 600
#Setting the pixels
gameDisplay = pygame.display.set_mode((display_width,display_height))


#Setting the title
pygame.display.set_caption('A rather whimsical game')


#Setting the internal clock
clock = pygame.time.Clock()

#All game logic will come here!


Img = pygame.image.load('Blinky.png')

#Make the image show up]
def car(x,y):
	gameDisplay.blit(Img, (x,y))
	
	

def game():

	x = display_width * 0.45
	y = display_height * 0.8	
		
	x_change = 0 #This is for changing directions and shit
	y_change = 0 
		
	end = False

	while not end: 
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				end = True\
			
			print (event)
			
			
			if event.type == pygame.KEYDOWN:
				if event.key == K_DOWN:
					y_change += 5
				if event.key == K_LEFT:
					x_change -= 5
				if event.key == K_RIGHT:
					x_change += 5
				if event.key == K_UP:
					y_change -= 5
							
			   

			if event.type == pygame.KEYUP:
				if event.key == K_LEFT or event.key == K_RIGHT:
					x_change = 0
				if event.key == K_UP or event.key== K_DOWN:
					y_change = 0
					
		x = x+ x_change
		y = y + y_change
			
		gameDisplay.fill(white)
		car(x,y)
							
			
		pygame.display.update()
		clock.tick(30) #This is effectively just frame rate. Right now it is at 30 fps
		
	
pygame.quit()