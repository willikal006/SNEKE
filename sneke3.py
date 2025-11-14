import pygame, random

# Initialize pygame
pygame.init()

# Set display window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
display_surface = pygame.display.set_mode(size)
pygame.display.set_caption("~~SNEKE~~")

# Set FSP and clock

clock = pygame.time.Clock()

# Set game values

snake_size = 20

head_x = WINDOW_WIDTH // 2


head_y = WINDOW_HEIGHT // 2 + 100

snake_dx = 0

snake_dy = 0

score = 0
# Set colors
GREEN = (0, 255, 0)  # (r, g, b)

rgb = (10, 50, 10)

RED = (255, 0, 0)

white = (255, 255, 255)

# Set fonts
font = pygame.font.SysFont('gabriola', 48)
font.set_bold(True)

# Set text
title_text = font.render("~~Snake~~", True, GREEN, DARKRED)  # make a text object
title_rect = title_text.get_rect()  # gets the box containing the text object
title_rect.center = (WINDOW_WIDTH // 2,
                     WINDOW_HEIGHT // 2)  # places the box containing the text object's center to the middle of the screen.


score_text = font.render(f"Score: {score}", True, GREEN, DARKRED)

score_rect = score_text.get_rect()

score_rect.topleft = (10, 10)


game_over_text = font.render("GAMEOVER", True, RED, DARKRED)

game_over_rect = game_over_text.get_rect()

game_over_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

continue_text = font.render("Press any key to play again", True, RED, DARKGREEN)

continue_rect = continue_text.get_rect()

continue_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 64)
# Set sounds and music
pick_up_sound = pygame.mixer.Sound("pickup_sound.wav")

# Set images (in this case, use simple rects...so just create their coordinates)
# For a rectangle you need (top-left x, top-left y, width, height)
apple_coord = (500, 500, SNAKE_SIZE, SNAKE_SIZE)
apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)


tuple = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)

head_rect = pygame.draw.rect(display_surface, GREEN, tuple)


# The main game loop
running = True
while running:
    # Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Move the snake

    # Add the head coordinate to the first index of the body coordinate list
    # This will essentially move all the snakes body by one position in the list

    # Update the x,y position of the snakes head and make a new coordinate

    # Check for game over

    # Check for collisions

    # Update HUD
   
    score_text = font.render(f"Score: {score}", True, GREEN, DARKRED)

    continue_text = font.render("Press any key to play again", True, RED, DARKGREEN)

    # Fill the surface

    ''' 
    The display_surface has a function we can use called fill, which takes one color argument.  
    The act of using display_surface's fill is said as
    "Call display_surface's fill function and pass WHITE in as it's argument."
    It looks like this:  
    1. display_surface.fill(WHITE)
    '''

    # Blit HUD

    '''
    Blitting means copying an image from it's source (the code) to it's destination (the display) 
    This is necessary after updating the source (score changes, snake, and apple change etc.)
    1. "Call display_surface's blit function.  It takes 2 arguments, text and rect surrounding that text.  
    Pass in title_text and title_rect to blit the title to the screen
    2. repeat for a new call to display_surface's blit function passing in score_text and score_rect.  
    "We've just told the title and score to display.  
    '''

    # Blit assets

    '''
    Calling pygame.draw.rect is a way to blit rectangles.  
    The blit function for display_surface is for direct blitting.  
    2 ways to do similar things.  Update the display
    1. "Call pygame.draw.rect and passing in display_surface, GREEN, and head_coord for the head of the snake
    2. "Call pygame.draw.rct again pass in display_surface, RED, and apple_coord for the apple.  
    '''

    # Update display and tick clock
 '''
    1. Now we update the display by calling pygame.display's update function passing in no arguments.

    2. The while loop we are in is super fast.  We actually need to slow it down to our FPS of 20 seconds.  
    That's what our clock variable will do for us.  What until 20 frames have passed every second.  Then continue.  
    This is ticking the clock.   
    to tick the clock call the clock object's tick function passing in FPS
    '''

# End the game
pygame.quit()
