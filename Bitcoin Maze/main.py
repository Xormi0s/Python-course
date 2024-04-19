from pygame import *
from random import randint
from classes import *

WALL_COLOR = (52,82,63)
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (250,15,15)
GREEN = (15,250,15)
coin_counter = 0

font.init()
font = font.Font(None, 45)
win = font.render("You win!", True, GREEN)
lose = font.render("You lose!!!", True, RED)
coin_text = font.render("Coins:", True, WHITE)
coin_counter_text = font.render(str(coin_counter), True, WHITE)

mixer.init()
mixer.music.load("Bitcoin Maze/cave.mp3")
mixer.music.play()

coin_sound = mixer.Sound("Bitcoin Maze/coin_drop.mp3")
win_sound = mixer.Sound("Bitcoin Maze/win.wav")
lose_sound = mixer.Sound("Bitcoin Maze/lose.wav")

WIDHT = 700
HEIGHT = 500
FPS = 30

screen = display.set_mode((WIDHT, HEIGHT))
display.set_caption("Bitcoin Maze")
clock = time.Clock()
background = transform.scale(image.load("Bitcoin Maze/background.jpg"), (WIDHT, HEIGHT))

player = Player("Bitcoin Maze/miner.png", 10, 50, 8)
ghost = Ghost("Bitcoin Maze/ghost.png", 600, 200, 5)
coin_wallet = Player("Bitcoin Maze/bitcoin.png", 625, 425, 0)

wall1 = Border(WALL_COLOR, 0, 0, WIDHT, 10)
wall2 = Border(WALL_COLOR, 70, 10, 10, HEIGHT - 60)
wall3 = Border(WALL_COLOR, 140, HEIGHT-90, 10, 90)
wall4 = Border(WALL_COLOR, 230, 10, 10, HEIGHT-90)
wall5 = Border(WALL_COLOR, 300, 10, 10, HEIGHT - 90)
wall6 = Border(WALL_COLOR, 390, HEIGHT-300, 10, 300)
wall7 = Border(WALL_COLOR, 460, 10, 10, HEIGHT-200)

wall8 = Border(WALL_COLOR, 540, 250, 300, 10)
wall9 = Border(WALL_COLOR, 530, HEIGHT-150, 10, 150)
wall10 = Border(WALL_COLOR, 520, 10, 10, 120)


walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10]

coin1 = Coins(randint(50, WIDHT), randint(50, HEIGHT))
coin2 = Coins(randint(50, WIDHT), randint(50, HEIGHT))
coin3 = Coins(randint(50, WIDHT), randint(50, HEIGHT))
coin4 = Coins(randint(50, WIDHT), randint(50, HEIGHT))
coin5 = Coins(randint(50, WIDHT), randint(50, HEIGHT))
coin6 = Coins(randint(50, WIDHT), randint(50, HEIGHT))
coin7 = Coins(randint(50, WIDHT), randint(50, HEIGHT))
coin8 = Coins(randint(50, WIDHT), randint(50, HEIGHT))

coins = [coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8]


run = True
end = False
while run:
    for e in event.get():
        if e.type == QUIT:
            quit()
            run = False
        if end != True:
            screen.blit(background, (0,0))
            screen.blit(coin_text, (WIDHT-150, 35))
            screen.blit(coin_counter_text, (WIDHT-50, 35))
            player.controls()
            ghost.update()
            
            for w in walls:
                w.build_wall()
            
            for c in coins:
                c.draw_coin()
                if c.rect.colliderect(player.rect):
                    coins.remove(c)
                    coin_sound.play()
                    c.kill()
                    coin_counter += 1
                    coin_counter_text = font.render(str(coin_counter), True, WHITE)
            
            if sprite.collide_rect(player, coin_wallet) and coin_counter == 8:
                end = True
                screen.blit(win,(300, 325))
                win_sound.play()
                
            if sprite.collide_rect(player,ghost) or sprite.collide_rect(player,wall1) or sprite.collide_rect(player,wall2) or sprite.collide_rect(player,wall3) or sprite.collide_rect(player,wall4) or sprite.collide_rect(player,wall5) or sprite.collide_rect(player,wall6) or sprite.collide_rect(player,wall7) or sprite.collide_rect(player,wall8) or sprite.collide_rect(player,wall9) or sprite.collide_rect(player,wall10):
                end = True
                screen.blit(lose, (300, 325))
                lose_sound.play()
            
            player.game_end()
            ghost.game_end()
            coin_wallet.game_end()
        else:
            end = False
            coin_counter = 0
            for c in coins:
                c.kill()
            player = Player("Bitcoin Maze/miner.png", 10, 50, 8)
            coin_counter_text = font.render(str(coin_counter),True,WHITE)
            coin1 = Coins(randint(50, WIDHT), randint(50, HEIGHT))
            coin2 = Coins(randint(50, WIDHT), randint(50, HEIGHT))
            coin3 = Coins(randint(50, WIDHT), randint(50, HEIGHT))
            coin4 = Coins(randint(50, WIDHT), randint(50, HEIGHT))
            coin5 = Coins(randint(50, WIDHT), randint(50, HEIGHT))
            coin6 = Coins(randint(50, WIDHT), randint(50, HEIGHT))
            coin7 = Coins(randint(50, WIDHT), randint(50, HEIGHT))
            coin8 = Coins(randint(50, WIDHT), randint(50, HEIGHT))
            coins = [coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8]
            time.delay(3000)
        
    display.update()
    clock.tick(FPS)