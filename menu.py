import pygame
import sys
from button import Button
import main

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("ARKANOID") # когда игрок открывает игру, он попадает в главное меню

bg = pygame.image.load("assets/Background.png")
# изначально я хотел поставить на фон всей игры картинку космоса, но он сильно отвлекал от игры и я закрасил его в черный



def get_font(size): # функция берет нужный шрифт (он всего один) и нужный размер
    return pygame.font.Font("assets/font.ttf", size)

def play(): # функция запускает игру
    if main.play(): # если игра закончилась
        gameover() # выводится экран gameover

def tab(): # функция создает текст таблицы рекордов
    l1 = list()
    f = open("data/score.txt", encoding="utf8")
    for number, line in enumerate(f):
        l1.append(line)
    l1.sort(key=lambda x: int(x.split(' ')[1]), reverse=True) # всё содержимое score.txt сортируется по убыванию счета
    l1 = list(map(lambda x: x.replace('\n', ''), l1)) # и убирается все переносы строки
    return l1[:10]

def gameover(): # экран game over
    while True:
        screen.blit(bg, (0, 0))
        go_pos = pygame.mouse.get_pos()
        # на каждом экране (их всего два) считываются свои координаты мыши, чтобы не нажать невидимую кнопку с другого экрана
        go_text = get_font(30).render("GAME OVER", True, "#b68f40") # текст game over
        go_rect = go_text.get_rect(center=(150, 150))

        again_button = Button(image=pygame.image.load("assets/lil Rect.png"), pos=(150, 250),
                            text_input="Again", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        # кнопка again
        tomenu_button = Button(image=pygame.image.load("assets/lil Rect.png"), pos=(150, 350),
                            text_input="Menu", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        # кнопка menu
        screen.blit(go_text, go_rect)
        tb = tab()
        screen.blit(get_font(20).render('HIGHSCORE', True, "#b68f40"),
                    get_font(20).render('HIGHSCORE', True, "#b68f40").get_rect(center=(480, 30)))
        # надпись highscore
        for i in range(len(tb)):
            # выводятся 10 наилучщих рекордов
            screen.blit(get_font(20).render(tb[i], True, "#b68f40"),
                        get_font(20).render(tb[i], True, "#b68f40").get_rect(center=(460, 70 + i * 40)))
        for button in [again_button, tomenu_button]:
            button.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if again_button.checkForInput(go_pos): # при нажатии на again игра начинается с начала
                    play()
                if tomenu_button.checkForInput(go_pos): # при нажатии на menu игрок возвращается в главное меню
                    main_menu()

        pygame.display.update()

def main_menu(): # экран главного меню
    while True:
        screen.blit(bg, (0, 0))
        menu_pos = pygame.mouse.get_pos()
        menu_text = get_font(60).render("ARKANOID", True, "#b68f40") # заглавный текст
        menu_rect = menu_text.get_rect(center=(320, 100))
        play_button = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(320, 220),
                            text_input="PLAY", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        # кнопка play
        quit_button = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(320, 370),
                            text_input="QUIT", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        # кнопка quit
        screen.blit(menu_text, menu_rect)
        for button in [play_button, quit_button]:
            button.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(menu_pos): # при нажатии на play начинается игра
                    play()
                if quit_button.checkForInput(menu_pos): # при нажаьтии на quit, программа завершается
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

main_menu()