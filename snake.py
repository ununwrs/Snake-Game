#งู.py
import pygame
import random

pygame.init()
font = pygame.font.SysFont('Arial', 25)

# Colours
blue = (0, 0, 255)
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

screen_width = 720
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the snake in the middle of the screen
snake_x = screen_width / 8
snake_y = screen_height / 8
snake_speed = 15
snake_size = 10
snake_length = 4
snake_blocks = []

fruit_x = 300
fruit_y = 400

speed_x = 0
speed_y = 10

game_over = False

running = True
clock = pygame.time.Clock()

# While "running" is true (always true unless user quits):
while running:
  # If the user hasn't lost the game:
  if not game_over:
    screen.fill((255,255,255)) # 255, 255, 255 is hexadecimal for the colour black

    # Set the snake head to the current position, append to snake blocks to
    # keep track
    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_blocks.append(snake_head)

    # Ensure the snake is only as big as the length we've set
    if len(snake_blocks) > snake_length:
      del snake_blocks[0]

    # Not counting the last block, check if any other existing snake
    # blocks are crossing over the snake head (dead)


    # Draw a snake block for each point the user has
    for block in snake_blocks:
      pygame.draw.rect(screen, blue, [block[0], block[1], snake_size, snake_size])
    pygame.draw.rect(screen, red, [fruit_x, fruit_y, snake_size, snake_size])

    # Update the speed of the snake
    snake_x += speed_x
    snake_y += speed_y

    # If the snake is touching fruit (x and y position match for snake head and
    # fruit), set the fruit to a new, random position and update snake length
    if snake_x == fruit_x and snake_y == fruit_y:
      fruit_x = round(random.randrange(0, screen_width - snake_size) / 10.0) * 10.0
      fruit_y = round(random.randrange(0, screen_height - snake_size) / 10.0) * 10.0
      snake_length += 1

    # If the snake goes beyond the left or right side of the screen,
    if (snake_x >= screen_width or snake_x < 0 or
      # if the snake goes beyond the top of bottom of the screen,
      snake_y >= screen_height or snake_y < 0):
        # Set game over to true
        game_over = True

  # Game over logic (screen showing users score + how to continue)
  else:
    screen.fill(black)
    
    if snake_length-4 > 5:
        font = pygame.font.SysFont('Arial', 22)
        score = font.render('You scored ' + str(snake_length-4), False, green)
        text = font.render('You did that very well! Press \'esc\' to quit, or Spacebar to play again', False, white)
    else:
        score = font.render('You scored ' + str(snake_length-4), False, red)
        text = font.render('Nice try! Press \'esc\' to quit, or Spacebar to play again', False, white)

    screen.blit(score, (10, screen_height / 2 - 100))
    screen.blit(text, (10, screen_height / 2))


  # Update the screen
  pygame.display.flip()
  clock.tick(snake_speed)

  ### Event Loop
  # Get the next events from the queue
  # For each event returned from get(),
  for event in pygame.event.get():
    # If the event is "KEYDOWN"
    if event.type == pygame.KEYDOWN:
        # If "esc" is pressed, stop game
        if event.key == pygame.K_ESCAPE:
            running = False
        # If space is pressed, reset game
        if event.key == pygame.K_SPACE:
            game_over = False
            snake_x = screen_width / 4
            snake_y = screen_height / 4
            snake_blocks = []
            snake_length = 4
        # Movement (up, down, left, right arrow keys)
        if event.key == pygame.K_w:
            speed_x = 0
            speed_y = -10
        if event.key == pygame.K_s:
            speed_x = 0
            speed_y = 10
        if event.key == pygame.K_a:
            speed_y = 0
            speed_x = -10
        if event.key == pygame.K_d:
            speed_y = 0
            speed_x = 10
    # If the event is "QUIT" (when user clicks X on window)
    if event.type == pygame.QUIT:
      # Set running to False, stop event loop
      running = False
