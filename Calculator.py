import pygame
import sys

WIDTH = 15 * 2 + 60 * 4 - 10
HEIGHT = 80 + 60 * 5
FPS = 60

numbers = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
operators = ["/", "x", "-", "+", "="]
number = []
num_1 = 0
num_2 = 0
operator_1 = ""

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Calculator!")
clock = pygame.time.Clock()
font = pygame.font.SysFont("bold", 75)


def draw_buttons():
    pygame.draw.rect(screen, (174, 181, 179), (15, 80, 50 * 3 + 20, 50))
    txt = font.render("C", 1, (250, 250, 250))
    screen.blit(txt, (15 + 12.5, 80 + 2.5))

    for i in range(5):
        pygame.draw.rect(screen, (255, 157, 20), (15 + 3 * 60, 80 + 60 * i, 50, 50))

        if i == 0:
            txt = font.render("/", 1, (250, 250, 250))
            screen.blit(txt, (15 + 3 * 60 + 12.5, 80 + 60 * i + 2.5))
        elif i == 1:
            txt = font.render("x", 1, (250, 250, 250))
            screen.blit(txt, (15 + 3 * 60 + 12.5 - 4, 80 + 60 * i + 2.5 - 4))
        elif i == 2:
            txt = font.render("-", 1, (250, 250, 250))
            screen.blit(txt, (15 + 3 * 60 + 16.5 - 2, 80 + 60 * i + 2.5 - 2))
        elif i == 3:
            txt = font.render("+", 1, (250, 250, 250))
            screen.blit(txt, (15 + 3 * 60 + 12.5 - 4, 80 + 60 * i + 2.5 - 4))
        elif i == 4:
            txt = font.render("=", 1, (250, 250, 250))
            screen.blit(txt, (15 + 3 * 60 + 12.5 - 4, 80 + 60 * i + 2.5 - 4))

    for i in range(3):
        for p in range(3):
            pygame.draw.rect(screen, (82, 79, 75), (15 + p * 60, 80 + 60 + i * 60, 50, 50))
            txt = font.render(str(numbers[i][p]), 1, (250, 250, 250))
            screen.blit(txt, (15 + p * 60 + 12.5, 80 + 60 + i * 60 + 2.5))

    pygame.draw.rect(screen, (82, 79, 75), (15, 80 + 60 * 4, 170, 50))
    txt = font.render("0", 1, (250, 250, 250))
    screen.blit(txt, (15 + 12.5, 80 + 60 * 4 + 2.5))


display_number = ""
equal_pressed = False


def button_pressing():
    global display_number, operators, operator_1, num_1, num_2, equal_pressed
    mouse_pos = pygame.mouse.get_pos()
    mouse_press = pygame.mouse.get_pressed()
    if mouse_press[0] == 1:
        for i in range(3):
            for p in range(3):
                if 15 + p * 60 + 50 >= mouse_pos[0] >= 15 + p * 60:
                    if 80 + 60 + i * 60 + 50 >= mouse_pos[1] >= 80 + 60 + i * 60:
                        number.append(numbers[i][p])
                        pygame.time.delay(200)
                        display_number = display_number + str(number[len(number) - 1])

        if 15 + 12.5 + 50 * 3 >= mouse_pos[0] >= 15 + 12.5:
            if 80 + 60 * 4 + 2.5 + 50 >= mouse_pos[1] >= 80 + 60 * 4 + 2.5:
                number.append("0")
                pygame.time.delay(200)
                display_number = display_number + str(number[len(number) - 1])

        for i in range(5):
            if 15 + 3 * 60 + 50 >= mouse_pos[0] >= 15 + 3 * 60:
                if 80 + 60 * i + 50 >= mouse_pos[1] >= 80 + 60 * i:
                    if operators[i] == "=":
                        if num_1 == 0 or operator_1 == "":
                            print(num_1, num_2, operator_1)
                            break
                        else:
                            if num_2 == 0:
                                num_2 = int(display_number)

                            if operator_1 == operators[0]:
                                num = num_1 / num_2
                                display_number = str(num)
                                equal_pressed = True

                            elif operator_1 == operators[1]:
                                num = num_1 * num_2
                                display_number = str(num)
                                equal_pressed = True

                            elif operator_1 == operators[2]:
                                num = num_1 - num_2
                                display_number = str(num)
                                equal_pressed = True

                            elif operator_1 == operators[3]:
                                num = num_1 + num_2
                                display_number = str(num)
                                equal_pressed = True
                    else:
                        if operator_1 == "":
                            operator_1 = operators[i]
                            if num_1 == 0:
                                num_1 = int(display_number)
                            elif num_2 == 0:
                                num_2 = int(display_number)

                            display_number = ""
                            number.clear()

                    pygame.time.delay(300)

        if 15 + 50 * 3 >= mouse_pos[0] >= 15:
            if 80 + 50 >= mouse_pos[1] >= 80:
                number.clear()
                display_number = ""
                num_1 = 0
                num_2 = 0
                operator_1 = ""
                equal_pressed = False

    num = font.render(display_number, 1, (250, 250, 250))
    if equal_pressed:
        screen.blit(num, (15, 10))
    else:
        screen.blit(num, (WIDTH - 30 * len(number) - 1, 10))


run = True
while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((10, 10, 10))
    draw_buttons()
    button_pressing()
    pygame.display.update()
    pygame.display.flip()
