import pygame


red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
violet = (255, 0, 255)
white = (255, 255, 255)

field = {
    "x": [
        (40, 15),
        (200, 15),
        (360, 15),
        (40, 175),
        (200,175),
        (360, 175),
        (40, 335),
        (200, 335),
        (360, 335)
    ],
    "o": [
        (30, 15),
        (190, 15),
        (350, 15),
        (30, 175),
        (190, 175),
        (350, 175),
        (30, 335),
        (190, 335),
        (350, 335)
    ]
}


pygame.init()

screen = pygame.display.set_mode((480, 480))
screen.fill(white)
pygame.display.set_caption("TicTacToe")
clock = pygame.time.Clock()
clock.tick(60)

pygame.draw.line(screen, red, [10, 159], [149, 159], 2)
pygame.draw.line(screen, red, [169, 159], [309, 159], 2)
pygame.draw.line(screen, red, [329, 159], [470, 159], 2)
pygame.draw.line(screen, red, [0, 319], [149, 319], 2)
pygame.draw.line(screen, red, [169, 319], [309, 319], 2)
pygame.draw.line(screen, red, [329, 319], [470, 319], 2)
pygame.draw.line(screen, red, [159, 10], [159, 149], 2)
pygame.draw.line(screen, red, [159, 169], [159, 309], 2)
pygame.draw.line(screen, red, [159, 329], [159, 480], 2)
pygame.draw.line(screen, red, [319, 10], [319, 149], 2)
pygame.draw.line(screen, red, [319, 169], [319, 309], 2)
pygame.draw.line(screen, red, [319, 329], [319, 480], 2)

font = pygame.font.SysFont("Lucida Handwriting", 100)
font_go = pygame.font.SysFont("Lucida Handwriting", 60)

playground = [None, None, None, None, None, None, None, None, None]
active_player = "x"
active = True
gameover = False


def set_sign(player: str, set_field: int):
    global playground
    screen.blit(font.render(player.capitalize(), True, green), field[player][set_field])
    playground[set_field] = player

    if player == "x":
        return "o"
    else:
        return "x"


def set_winner(game_winner: str = "n"):
    f_game_over = font_go.render("GAME OVER!", True, blue)
    screen.blit(f_game_over, (40, 160))
    f_winner = font_go.render(f"{game_winner.capitalize()} WINS", True, blue)
    f_tie = font_go.render("IT's A TIE", True, blue)
    if game_winner == "x":
        screen.blit(f_winner, (115, 245))
    elif game_winner == "o":
        screen.blit(f_winner, (110, 245))
    else:
        screen.blit(f_tie, (80, 245))

    return True


while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(f"x: {x}; y: {y}")
            if gameover:
                active = False
                break
            if x <= 160 and y < 160 and playground[0] is None:
                active_player = set_sign(active_player, 0)
            elif 319 > x > 160 > y and playground[1] is None:
                active_player = set_sign(active_player, 1)
            elif x > 319 and y < 160 and playground[2] is None:
                active_player = set_sign(active_player, 2)
            elif x <= 160 < y < 320 and playground[3] is None:
                active_player = set_sign(active_player, 3)
            elif 319 > x > 160 and 160 < y < 320 and playground[4] is None:
                active_player = set_sign(active_player, 4)
            elif x > 319 and 160 < y < 320 and playground[5] is None:
                active_player = set_sign(active_player, 5)
            elif x <= 160 and y > 320 and playground[6] is None:
                active_player = set_sign(active_player, 6)
            elif 160 < x < 320 < y and playground[7] is None:
                active_player = set_sign(active_player, 7)
            elif x > 319 and y > 320 and playground[8] is None:
                active_player = set_sign(active_player, 8)

            if playground[0] == playground[1] == playground[2] == "x" or\
                    playground[3] == playground[4] == playground[5] == "x" or\
                    playground[6] == playground[7] == playground[8] == "x" or\
                    playground[0] == playground[3] == playground[6] == "x" or\
                    playground[1] == playground[4] == playground[7] == "x" or\
                    playground[2] == playground[5] == playground[8] == "x" or\
                    playground[0] == playground[4] == playground[8] == "x" or\
                    playground[2] == playground[4] == playground[6] == "x":
                gameover = set_winner("x")
            elif playground[0] == playground[1] == playground[2] == "o" or\
                    playground[3] == playground[4] == playground[5] == "o" or\
                    playground[6] == playground[7] == playground[8] == "o" or\
                    playground[0] == playground[3] == playground[6] == "o" or\
                    playground[1] == playground[4] == playground[7] == "o" or\
                    playground[2] == playground[5] == playground[8] == "o" or\
                    playground[0] == playground[4] == playground[8] == "o" or\
                    playground[2] == playground[4] == playground[6] == "o":
                gameover = set_winner("o")
            elif playground[0] and\
                    playground[1] and\
                    playground[2] and\
                    playground[3] and\
                    playground[4] and\
                    playground[5] and\
                    playground[6] and\
                    playground[7] and\
                    playground[8]:
                gameover = set_winner()


        pygame.display.flip()

pygame.quit()

