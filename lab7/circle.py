import pygame

red, white = (250, 0, 0), (255, 255, 255)

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Circle")

running = True
x, y = 550, 400

while running:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_DOWN] and y + 25 < 600:
        y += 20
    if keys[pygame.K_UP] and y - 25 > 0:
        y -= 20
    if keys[pygame.K_RIGHT] and x + 25 < 800:
        x += 20
    if keys[pygame.K_LEFT] and x - 25 > 0:
        x -= 20

    screen.fill(white)
    pygame.draw.circle(screen, red, (x, y), 25)
    pygame.display.update()

pygame.quit()