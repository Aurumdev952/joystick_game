# made my crash devz

import pygame, sys, random
import threading


import serial
POWER_UP_CONSTANT = 0.02
PORT = "COM10"
BASE = 502

def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time, power_up
    ball.x += ball_speed_x * power_up
    ball.y += ball_speed_y * power_up
    # print("power up:",power_up)
    if ball.top <= 0 or ball.bottom >= screen_height:
        pygame.mixer.Sound.play(pong_sound)
        ball_speed_y *= -1


    if ball.left <= 0:
        pygame.mixer.Sound.play(score_sound)
        player_score += 1
        score_time = pygame.time.get_ticks()
        power_up = 1


    if ball.right >= screen_width:
        pygame.mixer.Sound.play(score_sound)
        opponent_score += 1
        score_time = pygame.time.get_ticks()
        power_up = 1

    if ball.colliderect(player) and ball_speed_x > 0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.right - player.left) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - player.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - player.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1
        power_up += POWER_UP_CONSTANT

    if ball.colliderect(opponent) and ball_speed_x < 0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.left - opponent.right) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - opponent.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - opponent.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1
        power_up += POWER_UP_CONSTANT


def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height


def opponent_animation():
    global power_up
    if opponent.top < ball.y - (15 + (power_up / 2)):
        opponent.y += opponent_speed + (power_up)
    if opponent.bottom > ball.y + (15 + (power_up / 2)):
        opponent.y -= opponent_speed + (power_up)

    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height


def ball_start():
    global ball_speed_x, ball_speed_y, score_time

    current_time = pygame.time.get_ticks()
    ball.center = (screen_width / 2, screen_height / 2)

    if current_time - score_time < 700:
        number_three = game_font.render("3", False, white)
        screen.blit(number_three, (screen_width / 2 - 10, screen_height / 2 + 20))
    if 700 < current_time - score_time < 1400:
        number_number = game_font.render("2", False, white)
        screen.blit(number_number, (screen_width / 2 - 10, screen_height / 2 + 20))
    if 1400 < current_time - score_time < 2100:
        number_one = game_font.render("2", False, white)
        screen.blit(number_one, (screen_width / 2 - 10, screen_height / 2 + 20))

    if current_time - score_time < 2100:
        ball_speed_x, ball_speed_y = 0, 0
    else:
        ball_speed_y = 7 * random.choice((1, -1))
        ball_speed_x = 7 * random.choice((1, -1))
        score_time = None


# shared_data = None
def move_left():
    ev = pygame.event.Event(pygame.USEREVENT)
    ev.code = 12
    pygame.event.post(ev)


def move_right():
    # ev = pygame.event.Event(pygame.USEREVENT)
    ev = pygame.event.Event(pygame.USEREVENT)
    ev.code = 13
    pygame.event.post(ev)


def move_reset():
    ev = pygame.event.Event(pygame.USEREVENT)
    ev.code = 11
    pygame.event.post(ev)


def pyserial_thread():
    print("pyserial initialised")
    ser = serial.Serial(PORT, 19200, timeout=0.01)
    while True:
        try:
            arduino_data = ser.readline().decode().strip().split("\t")
            # print(arduino_data)
            if len(arduino_data) == 2:
                y = int(arduino_data[1])
                if y >= BASE + 5:
                    move_left()
                elif y <= BASE - 5:
                    move_right()
                else:
                    move_reset()
        except:
            pass
    ser.close()


serial_thread = threading.Thread(target=pyserial_thread)
serial_thread.daemon = True


pygame.mixer.pre_init()
pygame.init()
serial_thread.start()
clock = pygame.time.Clock()


screen_width = 1080
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Joystick game - Pong")



ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10, 140)


bg_color = pygame.Color(0, 0, 0)
ball_color = (255, 255, 255)
line_color = (132, 132, 130)
player_color = (0, 255, 0)
opponent_color = (255, 0, 0)
white = (255, 255, 255)

ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7
power_up = 1


score_time = True



player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 32)


pong_sound = pygame.mixer.Sound("sound/sfx_point.wav")
score_sound = pygame.mixer.Sound("sound/sfx_swooshing.wav")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7
        if event.type == pygame.USEREVENT:
            if event.code == 13:
                player_speed = 10
            if event.code == 12:
                player_speed = -10
            if event.code == 11:
                player_speed = 0

    ball_animation()
    player_animation()
    opponent_animation()


    screen.fill(bg_color)
    pygame.draw.rect(screen, player_color, player)
    pygame.draw.rect(screen, opponent_color, opponent)
    pygame.draw.ellipse(screen, ball_color, ball)
    pygame.draw.aaline(
        screen, line_color, (screen_width / 2, 0), (screen_width / 2, screen_height)
    )

    if score_time:
        ball_start()

    player_text = game_font.render(f"{player_score}", False, white)
    screen.blit(player_text, (660 - 100, 470))

    opponent_text = game_font.render(f"{opponent_score}", False, white)
    screen.blit(opponent_text, (600 - 100, 470))


    pygame.display.flip()
    clock.tick(75)
