#import a library of functions called 'pygame'
import pygame
#initialise the game engine
pygame.init()

#Defining some colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)



PI = 3.141592653

#opening and setting a window
size = (700,500)
screen = pygame.display.set_mode(size)

#setting title window
pygame.display.set_caption("Profressor Cool's game")
                           
#setting up the main loop
#loop until the users presses close button
done = FALSE

#Used to manage how fast the screen updates
clock = pygame.time.Clock()

#---Main loop -----

while not done:
 
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    # All drawing code happens after the for loop and but
    # inside the main while not done loop.
     
    # Clear the screen and set the screen background
    screen.fill(WHITE)


    
    pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    
    #VERY important to flip the screen. This command flips the graphics to the screen
    pygame.display.flip()
    
    #ALL code to draw goes above here

    #limit to 20 frames per second
    clock.tick(20)

#shutting down the program
pygame.quit()
