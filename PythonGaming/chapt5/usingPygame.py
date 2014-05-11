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
    
    #Drawing a green line from 0,0 to 100,100 which is 5 pixels wide
    pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    
    #using a loop to draw 5 lines moving down by 10 pixel each time
    for y_offset in range(10,100,10):
        pygame.draw.line(screen, RED, [0,y_offset], [100,(100+y_offset)],5)
        y_offset += 10
    
    #drawing a rectangle needs the left corner orgin, height and width coordinates.
    pygame.draw.rect(screen, BLACK, [20, 60, 50, 100],5)

    #drawing an ellipse inside the rectangle
    pygame.draw.ellipse(screen, GREEN, [20,60,50,100],3)

    #printing text is a 3 stage process. Define the print, shape the text and print it.
    font = pygame.font.Font(None, 25)
    text = font.render("Some text", True, BLACK)
    screen.blit(text,[250,250])
    
    #VERY important to flip the screen. This command flips the graphics to the screen
    pygame.display.flip()
    
    #ALL code to draw goes above here

    #limit to 20 frames per second
    clock.tick(60)

#shutting down the program
pygame.quit()
