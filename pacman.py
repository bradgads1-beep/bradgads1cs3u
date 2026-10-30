import pygame

def check_collision(player, walls):
       """
       Checks whether the player collides with any of the maze walls.
       Parameters:
           player (pygame.Rect): The rectangle representing the player.
           walls (list): A list of rectangles representing the maze walls.
       
       Returns:
           bool: True if the player collides with a wall, False otherwise.
       """
       for wall in walls:
           if player.colliderect(wall):
               return True
       return False
 
   # Initialize Pygame
pygame.init()
 
pygame.mixer.music.load("freesound_community-playing-pac-man-6783.mp3")


pygame.mixer.music.play(1)


pygame.mixer.music.set_volume(0.5)
   # Set screen resolution
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
 
   # Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PAC-MAN!!!")
 
   # Set up colours
WHITE = (255, 255, 255)
BLUE = (0, 0, 200)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
 
   # Set up the player
player_x = 300
player_y = 20
player_size = 16
speed = 3
enemy_x = 300
enemy_y = 300
enemy_size = 16
enemy_speed = 0.5

   # Create the exit
exit_rect = pygame.Rect(540, 340, 30, 30)
 
   # Create the maze walls
walls = [
       pygame.Rect(45, 395, 495, 20),
       pygame.Rect(45, 0, 20, 170),
       pygame.Rect(45, 250, 20, 175),
       pygame.Rect(0, 150, 65, 20),
       pygame.Rect(0, 250, 45, 20),
       
       
       pygame.Rect(100, 40, 20, 325),
       pygame.Rect(155, 0, 20, 150),
       
       pygame.Rect(155, 200, 20, 50), #
       pygame.Rect(155, 300, 20, 100),
       
       pygame.Rect(260, 40, 20, 100),
       pygame.Rect(320, 40, 20, 100),
       pygame.Rect(375, 40, 20, 325),
       pygame.Rect(210, 40, 20, 325),
       pygame.Rect(265, 275, 20, 95),
       pygame.Rect(320, 275, 20, 95),
       pygame.Rect(265, 275, 20, 95),
       
       pygame.Rect(430, 200, 20, 50), #
       pygame.Rect(430, 300, 20, 100),
       
       pygame.Rect(375, 40, 20, 325),
       pygame.Rect(430, 0, 20, 150),
       pygame.Rect(485, 40, 20, 325),
       
       pygame.Rect(540, 0, 20, 150),
       pygame.Rect(540, 250, 20, 175),
       pygame.Rect(540, 150, 65, 20),
       pygame.Rect(540, 250, 65, 20),
       
       
       pygame.Rect(270, 170, 70, 75),
       pygame.Rect(45, 0, 495, 10),
   ]
dots = [pygame.Rect(70, 200, 15, 15),
        pygame.Rect(127, 200, 15, 15),
        pygame.Rect(180, 200, 15, 15),
        pygame.Rect(239, 200, 15, 15),
        pygame.Rect(349, 200, 15, 15),
        pygame.Rect(405, 200, 15, 15),
        pygame.Rect(460, 200, 15, 15),
        pygame.Rect(525, 200, 15, 15),

        pygame.Rect(70, 40, 15, 15),
        pygame.Rect(127, 40, 15, 15),
        pygame.Rect(180, 40, 15, 15),
        pygame.Rect(239, 40, 15, 15),
        pygame.Rect(349, 40, 15, 15),
        pygame.Rect(405, 40, 15, 15),
        pygame.Rect(460, 40, 15, 15),
        pygame.Rect(525, 40, 15, 15),

        pygame.Rect(70, 120, 15, 15),
        pygame.Rect(127, 120, 15, 15),
        pygame.Rect(180, 120, 15, 15),
        pygame.Rect(239, 120, 15, 15),
        pygame.Rect(349, 120, 15, 15),
        pygame.Rect(405, 120, 15, 15),
        pygame.Rect(460, 120, 15, 15),
        pygame.Rect(525, 120, 15, 15),

        pygame.Rect(70, 270, 15, 15),
        pygame.Rect(127, 270, 15, 15),
        pygame.Rect(180, 270, 15, 15),
        pygame.Rect(239, 270, 15, 15),
        pygame.Rect(349, 270, 15, 15),
        pygame.Rect(405, 270, 15, 15),
        pygame.Rect(460, 270, 15, 15),
        pygame.Rect(525, 270, 15, 15),

        pygame.Rect(70, 350, 15, 15),
        pygame.Rect(127, 350, 15, 15),
        pygame.Rect(180, 350, 15, 15),
        pygame.Rect(239, 350, 15, 15),
        pygame.Rect(349, 350, 15, 15),
        pygame.Rect(405, 350, 15, 15),
        pygame.Rect(460, 350, 15, 15),
        pygame.Rect(525, 350, 15, 15),

        pygame.Rect(20, 200, 15, 15),
        pygame.Rect(295, 40, 15, 15),
        pygame.Rect(295, 120, 15, 15),
        pygame.Rect(295, 350, 15, 15),
        pygame.Rect(295, 270, 15, 15),
        pygame.Rect(570, 200, 15, 15),
        
       ]


   # Set up the game
clock = pygame.time.Clock()
running = True
won = False
 
   # Main game loop
while running:
       # Check for events
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running = False
 
       # Get the keys being pressed
       keys = pygame.key.get_pressed()
 
       if not won:
           # Move left
           if keys[pygame.K_LEFT]:
               player_x -= speed
               player = pygame.Rect(player_x, player_y, player_size, player_size)
               if check_collision(player, walls):
                   player_x += speed
 
           # Move right
           if keys[pygame.K_RIGHT]:
               player_x += speed
               player = pygame.Rect(player_x, player_y, player_size, player_size)
               if check_collision(player, walls):
                   player_x -= speed
 
           # Move up
           if keys[pygame.K_UP]:
               player_y -= speed
               player = pygame.Rect(player_x, player_y, player_size, player_size)
               if check_collision(player, walls):
                   player_y += speed
 
           # Move down
           if keys[pygame.K_DOWN]:
               player_y += speed
               player = pygame.Rect(player_x, player_y, player_size, player_size)
               if check_collision(player, walls):
                   player_y -= speed
 
           # Keep the player inside the screen
           if player_x < 1:
               player_x = 582
               player_y = 200
           if player_x > SCREEN_WIDTH - player_size:
               player_x = SCREEN_WIDTH - player_size
           
        

           if enemy_x < player_x:
                enemy_x += enemy_speed
           elif enemy_x > player_x:
                enemy_x -= enemy_speed
           if enemy_y < player_y:
                enemy_y += enemy_speed
           elif enemy_y > player_y:
                enemy_y -= enemy_speed

           #print(player_x)
           #print(player_y)
           if player_x >582:
                player_x = 0
                player_y = 200
           if player_x > SCREEN_WIDTH - player_size:
                player_x = SCREEN_WIDTH - player_size
          
 
           # Update the player rectangle
           player = pygame.Rect(player_x, player_y, player_size, player_size)
           enemy = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)

           if player.colliderect(enemy):
                running = False 
 
           # Check if the player reaches the exit
           if player.colliderect(exit_rect):
               won = True
 
       # Draw the background
       screen.fill(BLACK)
 
       # Draw the maze walls
       for wall in walls:
           pygame.draw.rect(screen, BLUE, wall)

       for dot in dots:
           pygame.draw.rect(screen, WHITE, dot)    

       for dot in dots:
           if player.colliderect(dot):
               dot.x = 600
               dot.y = 600
 
       # Draw the player
       player = pygame.draw.circle(screen, YELLOW, (player_x, player_y), player_size)

       enemy = pygame.draw.circle(screen, RED, (enemy_x, enemy_y), enemy_size)

       if sum(1 for dot in dots if dot.x == 600 and dot.y == 600) >= 46:
            won = True
    
       # Display the winning message
       if won:
           font = pygame.font.SysFont(None, 48)
           message = font.render("YOU WIN!", True, WHITE)
           screen.blit(message, (220, 180))
 
       # Update the display
       pygame.display.flip()
 
       # Limit the game to 60 FPS
       clock.tick(60)
 
   # Close Pygame
pygame.quit()