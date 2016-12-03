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



class Player(pygame.sprite.Sprite):
  
    # Set speed vector
    change_x=0
    change_y=0
  
    # Constructor function
    def __init__(self,x,y, filename):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
   
        # Set height, width
        self.image = pygame.image.load(filename).convert()
  
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x
        self.prev_x = x
        self.prev_y = y
		#gameDisplay.blit(self.image, (x,y))
		
		
def game():
	b = Player(100,100, 'Blinky.png')
	
	
	
	
	end = False

	while not end: 
		
			
			
		
		
		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				end = True
			
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
					
		#x = x+ x_change
		#y = y + y_change
			
		#gameDisplay.fill(white)
		
		player1 = Player(400, 400, 'Blinky.png')
		
		
							
			
		pygame.display.update()
		clock.tick(30) #This is effectively just frame rate. Right now it is at 30 fps


game()		
	
pygame.quit()