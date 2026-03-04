import pygame
import sys

# --- Configuración ---
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Mario 2D")
clock = pygame.time.Clock()
FONT = pygame.font.SysFont("Arial", 32)

# --- Colores ---
WHITE = (255, 255, 255)
SKY = (135, 206, 235)
BROWN = (139, 69, 19)

# --- Cargar sprites ---
player_sprite = pygame.image.load("mario.png")
player_sprite = pygame.transform.scale(player_sprite, (50, 60))

enemy_sprite = pygame.image.load("enemigo.png")
enemy_sprite = pygame.transform.scale(enemy_sprite, (50, 40))

coin_sprite = pygame.image.load("moneda.png")
coin_sprite = pygame.transform.scale(coin_sprite, (30, 30))

princess_sprite = pygame.image.load("princesa.png")
princess_sprite = pygame.transform.scale(princess_sprite, (50, 60))

# --- Función para reiniciar el juego ---
def reset_game():
    global player_x, player_y, player_vel_y, score, coins, win, lives
    player_x, player_y = 100, HEIGHT - player_height - 50
    player_vel_y = 0
    score = 0
    coins = [
        pygame.Rect(180, 460, 30, 30),
        pygame.Rect(500, 410, 30, 30),
        pygame.Rect(120, 340, 30, 30),
        pygame.Rect(400, 260, 30, 30),
        pygame.Rect(650, 180, 30, 30),
    ]
    win = False
    lives = 3

# --- Jugador ---
player_width, player_height = 50, 60
player_x, player_y = 100, HEIGHT - player_height - 50
player_vel_x = 0
player_vel_y = 0
player_speed = 5
jump_speed = -15
gravity = 1
on_ground = False
score = 0
win = False
lives = 3

# --- Plataformas ---
platforms = [
    pygame.Rect(0, HEIGHT-50, WIDTH, 50),
    pygame.Rect(150, 500, 200, 20),
    pygame.Rect(450, 450, 200, 20),
    pygame.Rect(100, 380, 150, 20),
    pygame.Rect(350, 300, 200, 20),
    pygame.Rect(600, 230, 150, 20),
    pygame.Rect(300, 150, 200, 20),
]

# --- Enemigos ---
enemies = [
    {"rect": pygame.Rect(200, 410, 50, 40), "vel": 2},
    {"rect": pygame.Rect(500, 210, 50, 40), "vel": 3},
]

# --- Monedas ---
coins = [
    pygame.Rect(180, 460, 30, 30),
    pygame.Rect(500, 410, 30, 30),
    pygame.Rect(120, 340, 30, 30),
    pygame.Rect(400, 260, 30, 30),
    pygame.Rect(650, 180, 30, 30),
]

# --- Princesa ---
princess_rect = pygame.Rect(350, 90, 50, 60)

# --- Loop del juego ---
running = True
while running:
    clock.tick(60)
    screen.fill(SKY)

    # --- Eventos ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not win and lives > 0:
        # --- Teclas ---
        keys = pygame.key.get_pressed()
        player_vel_x = 0
        if keys[pygame.K_LEFT]:
            player_vel_x = -player_speed
        if keys[pygame.K_RIGHT]:
            player_vel_x = player_speed
        if keys[pygame.K_SPACE] and on_ground:
            player_vel_y = jump_speed
            on_ground = False

        # --- Física ---
        player_vel_y += gravity
        player_x += player_vel_x
        player_y += player_vel_y
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

        # --- Colisiones con plataformas ---
        on_ground = False
        for plat in platforms:
            if player_rect.colliderect(plat) and player_vel_y > 0:
                player_y = plat.y - player_height
                player_vel_y = 0
                on_ground = True

        # --- Movimiento enemigos ---
        for e in enemies:
            e["rect"].x += e["vel"]
            if e["rect"].left < 0 or e["rect"].right > WIDTH:
                e["vel"] *= -1

        # --- Colisiones con enemigos ---
        for e in enemies:
            if player_rect.colliderect(e["rect"]):
                lives -= 1
                player_x, player_y = 100, HEIGHT - player_height - 50
                player_vel_y = 0
                if lives <= 0:
                    # PERDISTE
                    game_over_text = FONT.render("¡PERDISTE!", True, (255, 0, 0))
                    screen.blit(game_over_text, (WIDTH//2 - 100, HEIGHT//2 - 20))
                    pygame.display.update()
                    pygame.time.delay(2000)
                    reset_game()

        # --- Recolección de monedas ---
        for c in coins[:]:
            if player_rect.colliderect(c):
                coins.remove(c)
                score += 1

        # --- Verificar victoria (princesa) ---
        if player_rect.colliderect(princess_rect):
            win = True

    # --- Dibujar plataformas ---
    for plat in platforms:
        pygame.draw.rect(screen, BROWN, plat)

    # --- Dibujar jugador ---
    screen.blit(player_sprite, (player_x, player_y))

    # --- Dibujar enemigos ---
    for e in enemies:
        screen.blit(enemy_sprite, (e["rect"].x, e["rect"].y))

    # --- Dibujar monedas ---
    for c in coins:
        screen.blit(coin_sprite, (c.x, c.y))

    # --- Dibujar princesa ---
    screen.blit(princess_sprite, (princess_rect.x, princess_rect.y))

    # --- Dibujar score y vidas ---
    score_text = FONT.render(f"Puntos: {score}", True, WHITE)
    lives_text = FONT.render(f"Vidas: {lives}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 50))

    # --- Mensaje de victoria ---
    if win:
        win_text = FONT.render("¡GANASTE!", True, (255, 0, 0))
        screen.blit(win_text, (WIDTH//2 - 100, HEIGHT//2 - 20))

    pygame.display.update()