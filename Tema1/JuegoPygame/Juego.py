#Simple pygame program

# Import and initialize the pygame library
import pygame
import random
import os
import sys


ruta = os.path.dirname(__file__)
base = os.path.join(ruta, "resources")



'''Teclas que vamos a utilizar'''
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_SPACE,
    K_q,
    KEYDOWN,
    QUIT
)




class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        
        self.surf = pygame.image.load(os.path.join(base,"jet.png")).convert()
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            move_up_sound.play()
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            move_down_sound.play()
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)    

        '''Evitamos que el jugador salga de la pantalla'''
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Enemy(pygame.sprite.Sprite):
    
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load(os.path.join(base,"missile.png")).convert()
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect(
            center =(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT)
            )
        )
        self.speed = random.randint(5, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill() 
            global score
            score+=10             
            

class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load(os.path.join(base,"cloud.png")).convert()
        self.surf.set_colorkey((0, 0, 0), pygame.RLEACCEL)
        self.rect = self.surf.get_rect(
            center = (
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 200),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(2, 4)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH + 20
            self.rect.centery = random.randint(0, SCREEN_HEIGHT // 2)    
  

'''puntuacion y vidas del jugador'''
def puntos_vidas(screen):
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {score}', True, (37,40,80))
    score_rect = score_text.get_rect(topleft=(10,10))
    screen.blit(score_text, score_rect)
    lives_text = font.render(f'Lives: {lives}', True, (139,0,0))
    lives_rect = lives_text.get_rect(topleft=(700,10))
    screen.blit(lives_text, lives_rect)
'''leer maxima puntuacion'''
def leer_maxima_puntuacion():

    try:
        with open("record.txt","r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0    
'''guarda maxima puntuacion'''
def guarda_maxima_puntuacion(record):
    with open("record.txt", "w") as file:
        file.write(str(record))

'''funcion para la pantalla inicial'''
def pantalla_inicial(screen):
    font = pygame.font.Font(None, 36)
    text = font.render("Press SPACE to Start", True, (255, 255, 255))
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.fill((0, 0, 0))
    screen.blit(text, text_rect)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_SPACE:
                waiting = False
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()


'''funcion para la pantalla de GAME OVER'''
def pantalla_game_over(screen):
    
    font = pygame.font.Font(None, 50)
    game_over_text = font.render("GAME OVER", True, (139, 0, 0))
    game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40))

    restart_text = font.render("Press SPACE to Restart", True, (255, 255, 255))
    restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))

    quit_text = font.render("Press QUIT to Exit", True, (255, 255, 255))
    quit_rect = quit_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80))

    record_text = font.render(f'Record: {record}', True, (229,190,1))
    record_rect = record_text.get_rect(topleft=(10,10))
    
    
    screen.fill((0, 0, 0))
    screen.blit(record_text, record_rect)
    screen.blit(game_over_text, game_over_rect)
    screen.blit(restart_text, restart_rect)
    screen.blit(quit_text, quit_rect)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    return True  # Volver a jugar
                elif event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()  # Salir del juego
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()

'''1 Iniciamos el mexclador de sonido'''
pygame.mixer.init()
pygame.mixer.music.load(os.path.join(base,"Apoxode_-_Electric_1.ogg"))

move_up_sound = pygame.mixer.Sound(os.path.join(base,"Rising_putter.ogg"))
move_down_sound = pygame.mixer.Sound(os.path.join(base,"Falling_putter.ogg"))
collision_sound = pygame.mixer.Sound(os.path.join(base,"Collision.ogg"))

'''2 Iniciamos pygame'''
pygame.init()



'''Tamaño de la pantalla'''
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set up the drawing window
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))


ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

'''Velocidad del juego'''
clock = pygame.time.Clock()

'''Instanciamos player'''
player = Player()
'''enemigos'''
enemies = pygame.sprite.Group()
'''nubes'''
clouds = pygame.sprite.Group()


all_sprites = pygame.sprite.Group()
all_sprites.add(player)






pantalla_inicial(screen)
score = 0
record = 0 
lives = 3
# Run until the user asks to quit
running = True
pygame.mixer.music.play(loops=-1)
while running:
    
    record = leer_maxima_puntuacion()
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == pygame.QUIT:
            running = False

        
        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
            

            
        elif event.type == ADDCLOUD:
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)
           



    
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    '''comprobamos si hay colision'''
    if pygame.sprite.spritecollideany(player,enemies):
        collision_sound.play()
        player.kill()
        '''vidas'''
        lives -= 1
        if lives <= 0:
            running = False
            '''record'''
            if score > record: 
                record = score
                guarda_maxima_puntuacion(record)
            pygame.mixer.music.stop()
            if pantalla_game_over(screen):
                player = Player()
                enemies = pygame.sprite.Group()
                clouds = pygame.sprite.Group()
                all_sprites = pygame.sprite.Group()
                all_sprites.add(player)
                pygame.time.set_timer(ADDENEMY, 250)
                score = 0
                lives = 3
                running = True
                pygame.mixer.music.play(loops=-1)
        else:
            player = Player()
            all_sprites = pygame.sprite.Group()
            all_sprites.add(player)
            enemies = pygame.sprite.Group()
            pygame.time.set_timer(ADDENEMY, 250)
           


    # Get all the keys currently pressed
    pressed_keys = pygame.key.get_pressed()

    
    
    # Update the player sprite based on user keypresses
    player.update(pressed_keys)
    enemies.update()
    clouds.update()
    
    

   
    #surf = pygame.Surface((50,50))
    screen.fill((135, 206, 250))

    '''Dibujamos las nubes'''
    for cloud in clouds:
        screen.blit(cloud.surf, cloud.rect)
    
    '''Dibujamos los enemigos'''
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    '''Aqui dibujamos el objeto surf, al jugador'''
    screen.blit(player.surf, player.rect)
    '''Imagen de presentacion'''
    puntos_vidas(screen)
 
   

    # Flip the display
    pygame.display.flip()

    '''30 frames por segundo'''
    clock.tick(30)
# Done! Time to quit.
pygame.mixer.music.stop()
pygame.mixer.quit()
pygame.quit()
