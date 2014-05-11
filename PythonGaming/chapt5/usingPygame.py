#import a library of functions called 'pygame'
import pygame
#initialise the game engine
pygame.init()

#Defining some colours
BLACK = (   0,   0,   0)
WHITE = ( 255, 255, 255)
GREEN = (   0, 255,   0)
RED   = ( 255,   0,   0)

PI = 3.141592653

#opening and setting a window
size = (400, 500)
screen = pygame.display.set_mode(size)

#setting title window
pygame.display.set_caption("Profressor Cool's game")
                           
#setting up the main loop
#loop until the users presses close button
done = False

#Used to manage how fast the screen updates
clock = pygame.time.Clock()

#---Main loop -----
while not done:
    #event processing. This handles keystrokes and mouse clicks
    for event in pygame.event.get():#user did something
        if event.type == pygame.QUIT: #if used clicked close
            done = True #flag that the loop with exit
    #event processing goes above here
            
    #ALL game logic goes below here

    #ALL game logic goes above here

    
    #ALL code to draw goes below here
    #clearing the screen white
    screen.fill(WHITE)
    
    pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    
    #VERY important to flip the screen. This command flips the graphics to the screen
    pygame.display.flip()
    
    #ALL code to draw goes above here

    #limit to 20 frames per second
    clock.tick(60)

#shutting down the program
pygame.quit()
