import pygame
import  random
from random import uniform
import pygame.mixer



pygame.init()

pygame.mixer.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()

window_width = 800
window_height = 600


window = pygame.display.set_mode((window_width, window_height))
background = pygame.image.load("fon.jpg")
pygame.display.set_caption("Racing")


car_width = 100
car_height = 140
#img_back = "fon.jpg"
car_image = pygame.image.load("player.png")
car_image = pygame.transform.scale(car_image, (car_width, car_height))
enemy1_image = pygame.image.load("enemy1.png")
enemy1_image = pygame.transform.scale(enemy1_image, (100, 140))

#enemy2_image = pygame.image.load("enemy2.jpg")
#enemy2_image = pygame.transform.scale(enemy2_image, (100, 160))



player_x = (window_width - car_width) // 2
player_y = window_height - car_height - 50
enemy_x = random.randint(0, window_width - car_width)
enemy_y = -car_height
#enemy2_x = random.randint(0, window_width - car_width)
#enemy2_y = -car_height
enemy_speed = random.uniform(0.1, 0.3)



score = 0
font = pygame.font.Font(None, 36)


running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    
    player_move = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 5:
        player_move = -0.8
    elif keys[pygame.K_RIGHT] and player_x < window_width - 80:
        player_move = 0.8
    player_x += player_move
    
    enemy_y += enemy_speed
    #enemy2_y += enemy_speed

    if enemy_y > window_height:
        enemy_x = random.randint(0, window_width - car_width)
        enemy_y = -car_height
        score += 1
    #if enemy2_y > window_height:
      #  enemy2_x = random.randint(0, window_width - car_width)
       # enemy2_y = -140
        #score += 1
    
    if score > 9:
        enemy_speed = random.uniform(0.4, 0.5)
        
    if score > 19:
        enemy_speed = random.uniform(0.6, 0.7)

    if score > 29:
        enemy_speed = random.uniform(0.8, 0.9)

    if score > 49:
        enemy_speed = 1
        
        

    
    #window.fill((255, 255, 255))
    window.blit(background, (0, 0))
    window.blit(car_image, (player_x, player_y))
    window.blit(enemy1_image, (enemy_x, enemy_y))
    #window.blit(enemy2_image, (enemy2_x, enemy2_y))
        
    
    #pygame.draw.rect(window, 0, (enemy_x, enemy_y, car_width, car_height))
    
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    window.blit(score_text, (10, 10))
    pygame.display.flip()
    
    
    if player_x + car_width > enemy_x and player_x < enemy_x + car_width and player_y < enemy_y + car_height and player_y + car_height > enemy_y:
        running = False

    #gameDisplay.blit(bg, (0, 0))


pygame.quit()