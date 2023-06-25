import pygame
import random

# Инициализируем pygame
pygame.init()

# Определяем размеры окна
window_width = 800
window_height = 600

# Создаем окно
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Racing")

# Загружаем изображения машин
car_width = 120
car_height = 180
car_image = pygame.image.load("player.jpg")
car_image = pygame.transform.scale(car_image, (car_width, car_height))
enemy1_image = pygame.image.load("enemy1.jpg")
enemy1_image = pygame.transform.scale(enemy1_image, (car_width, car_height))


# Задаем начальные координаты машин
player_x = (window_width - car_width) // 2
player_y = window_height - car_height - 50
enemy_x = random.randint(0, window_width - car_width)
enemy_y = -car_height
enemy_speed = 0.2


# Задаем параметры игры
score = 0
font = pygame.font.Font(None, 36)

# Основной игровой цикл
running = True
while running:
    # Обрабатываем события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Обновляем положение машин
    player_move = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_move = -1
    elif keys[pygame.K_RIGHT]:
        player_move = 1
    player_x += player_move
    
    enemy_y += enemy_speed
    if enemy_y > window_height:
        enemy_x = random.randint(0, window_width - car_width)
        enemy_y = -car_height
        score += 1
    
    if score > 4:
        enemy_speed = 0.5

    if score > 9:
        enemy_speed = 0.8

    # Рисуем объекты на экране
    window.fill((255, 255, 255))
    window.blit(car_image, (player_x, player_y))
    #window.blit(enemy1_image, (100, 150))
    pygame.draw.rect(window, 0, (enemy_x, enemy_y, car_width, car_height))
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    window.blit(score_text, (10, 10))
    pygame.display.flip()
    
    # Проверяем столкновение машин
    if player_x + car_width > enemy_x and player_x < enemy_x + car_width and player_y < enemy_y + car_height and player_y + car_height > enemy_y:
        running = False


# Завершаем игру
pygame.quit()