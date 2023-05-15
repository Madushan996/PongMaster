import pygame

# Set up the Pygame module
pygame.init()

# Define the screen size
screen_width = 800
screen_height = 600

# Set up the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define the paddles
paddle_width = 15
paddle_height = 60
paddle_speed = 5

player_paddle = pygame.Rect(50, screen_height/2 - paddle_height/2, paddle_width, paddle_height)
computer_paddle = pygame.Rect(screen_width - 50 - paddle_width, screen_height/2 - paddle_height/2, paddle_width, paddle_height)

# Define the ball
ball_size = 10
ball_speed = 5

ball = pygame.Rect(screen_width/2 - ball_size/2, screen_height/2 - ball_size/2, ball_size, ball_size)

# Define the ball direction
ball_direction_x = ball_speed
ball_direction_y = ball_speed

# Define the font
font = pygame.font.SysFont(None, 48)

# Define the scores
player_score = 0
computer_score = 0

# Define the game loop
while True:
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # Handle keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_paddle.move_ip(0, -paddle_speed)
    if keys[pygame.K_DOWN]:
        player_paddle.move_ip(0, paddle_speed)
        
    # Move the computer paddle
    if ball_direction_x > 0:
        if computer_paddle.centery < ball.centery:
            computer_paddle.move_ip(0, paddle_speed)
        elif computer_paddle.centery > ball.centery:
            computer_paddle.move_ip(0, -paddle_speed)
            
    # Move the ball
    ball.move_ip(ball_direction_x, ball_direction_y)
    
    # Check for collisions with the walls
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_direction_y *= -1
    if ball.left <= 0:
        computer_score += 1
        ball_direction_x = ball_speed
        ball_direction_y = ball_speed
        ball.center = (screen_width/2, screen_height/2)
    if ball.right >= screen_width:
        player_score += 1
        ball_direction_x = -ball_speed
        ball_direction_y = ball_speed
        ball.center = (screen_width/2, screen_height/2)
        
    # Check for collisions with the paddles
    if ball.colliderect(player_paddle) or ball.colliderect(computer_paddle):
        ball_direction_x *= -1
        
    # Draw the screen
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player_paddle)
    pygame.draw.rect(screen, WHITE, computer_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    score_text = font.render(f"{player_score} : {computer_score}", True, WHITE)
    screen.blit(score_text, (screen_width/2 - score_text.get_width()/2, 10))
    pygame.display.flip()
    
    # Set the frame rate
    pygame.time.Clock().tick(60)
