import pygame
pygame.init()

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
end = False-

while not end: 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			end = True
		print (event)
		
	pygame.display.update()
	clock.tick(30) #This is effectively just frame rate. Right now it is at 30 fps
	
	
pygame.quit()