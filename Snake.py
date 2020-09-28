import sys, pygame, time, random, math, os
from gameClasses import *

def game_over():
    screen = pygame.display.get_surface()
    screen.fill((0, 0, 0))
    background = Background('game_over.png')
    screen.blit(background.image, background.rect)
    pygame.display.flip()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.__dict__['key'] == pygame.K_KP_ENTER or event.__dict__['key'] == pygame.K_RETURN:
                    start_page()

def new_game():
    pygame.mouse.set_visible(False)
    screen = pygame.display.get_surface()
    black = 0, 0, 0
    initial_position = [10, 350]
    movement = 20, 0

    player = snake(initial_position)
    background = Background('game_background.png')
    fig_fruit = Fruit()
    myfont = pygame.font.SysFont('Press Start 2P Médio', 55)
    score_text = myfont.render('Score', True, black)
    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.__dict__['key'] == pygame.K_a:
                    player.add()
                    fig_fruit = Fruit()
                movement = direction(event.__dict__['key'], movement, player)

        player.move(movement)

        if is_player_dead(player):
            game_over()
            # sys.exit()
            # break
        
        if player.segments[0].rect.topleft == fig_fruit.rect.topleft:
            player.add()
            fig_fruit = Fruit()
            score_text = myfont.render(
                "Score: %d" % player.score, True, black)

        screen.fill(black)
        screen.blit(background.image, background.rect)
        screen.blit(fig_fruit.image, fig_fruit.rect)
        screen.blit(score_text,(80, 28))
        player.draw(screen)

        pygame.display.flip()
        time.sleep(player.speed)

def start_page():
    pygame.mouse.set_visible(True)
    screen = pygame.display.get_surface()
    screen.fill((0, 0, 0))
    background = Background('initial_background.png')
    pygame.mouse.set_pos([400, 300])
    start_button = Button('start_off.png','start_on.png')
    screen.blit(background.image, background.rect)
    pygame.display.flip()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == 4:
                if start_button.rect.collidepoint(pygame.mouse.get_pos()):
                    screen.blit(start_button.image_mouse_on, start_button.rect)
                else: screen.blit(start_button.image_mouse_off, start_button.rect)
            if event.type == 5 and start_button.rect.collidepoint(pygame.mouse.get_pos()):
                new_game()


        pygame.display.update(start_button.rect)


def main():

    pygame.init()
    pygame.font.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size, 0, 0)
    pygame.display.set_caption('SNAKE GAME')

    start_page()

main()