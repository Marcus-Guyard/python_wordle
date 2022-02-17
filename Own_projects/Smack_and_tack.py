import random

import pygame, sys


class Minion:
    health: int
    attack: int
    x_pos: int
    y_pos: int
    width: int
    height: int

    def __init__(self, health, attack, heal, x_pos, y_pos, width, height, color):
        self.health = health
        self.attack = attack
        self.heal = heal
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.color = color

    def draw_minion(self):
        if self.health <= 0:
            pygame.draw.rect(win, self.color, (self.x_pos, self.y_pos + 100, self.width + 75, self.height - 95))
            pygame.draw.rect(win, ('#DCDDD8'), (self.x_pos, self.y_pos, self.width, self.height))
        elif self.health > 0:
            pygame.draw.rect(win, self.color, (self.x_pos, self.y_pos, self.width, self.height))
            pygame.draw.rect(win, ('#DCDDD8'), (self.x_pos, self.y_pos + 100, self.width + 75, self.height - 95))

    def healthbar(self, x_pos, y_pos, width, height, original_health):
        pygame.draw.rect(win, red, (x_pos-3, y_pos - 43, width+6, height + 5))
        pygame.draw.rect(win, white, (x_pos, y_pos - 40, width, height))
        if self.health >= original_health:
            pygame.draw.rect(win, green, (x_pos, y_pos - 40, original_health, height))
        else:
            pygame.draw.rect(win, green, (x_pos, y_pos - 40, self.health, height))


buttons = []


class Button:
    def __init__(self, text, width, height, pos, elevation):
        # Core attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]

        # top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#475F77'

        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos, (width, height))
        self.bottom_color = '#354B5E'
        # text
        self.text = text
        self.text_surf = gui_font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)
        buttons.append(self)

    def change_text(self, newtext):
        self.text_surf = gui_font.render(newtext, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self):
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(win, self.bottom_color, self.bottom_rect, border_radius=12)
        pygame.draw.rect(win, self.top_color, self.top_rect, border_radius=12)
        win.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        global fight
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#D74B4B'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed:
                    print('click')
                    self.pressed = False
                    fight = True
        else:
            self.dynamic_elevation = self.elevation
            self.top_color = '#475F77'


pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Smack and Tack')
gui_font = pygame.font.Font(None, 30)

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# Attributes >>>  hp, atk, heal,    x_pos, y_pos    width, height, color
warrior = Minion(100, 15, 10,      100, 100,       50, 100, red)
mage = Minion(50, 25, 10,       350, 100,       50, 100, blue)

button1 = Button('Attack', 290, 90, (5, 300), 5)
button2 = Button('Heal', 290, 90, (5, 400), 5)
button3 = Button('Raise Attack', 190, 190, (300, 300), 5)


def buttons_draw():
    for b in buttons:
        b.draw()


turn = True
warrior_origin_health = warrior.health
mage_origin_health = mage.health
fight = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if turn:
        if fight:
            if button1.pressed:
                mage.health -= warrior.attack
                print(f"warr atk mage, mage health: {mage.health}")
                turn = False

            if button2.pressed:
                if warrior.health < 100:
                    warrior.health += warrior.heal
                    print(f"warrior heals, warrior health: {warrior.health}")
                    turn = False
                else:
                    print("You have full health, you cannot heal")

            if button3.pressed:
                warrior.attack += 5
                print(f"warrior boosts attack, warr atk: {warrior.attack}")
                turn = False

    if not turn:
        r = random.randint(0, 2)
        if r == 0:
            warrior.health -= mage.attack
            print(f"mage atk warrior, warrior health: {warrior.health}")
            turn = True
            fight = False
        if mage.health < 50:
            if r == 1:
                mage.health += mage.heal
                print(f"mage heals, mage health: {mage.health}")
                turn = True
                fight = False
        elif r == 2:
            mage.attack += 5
            print(f"mage boosts atk, mage attack: {mage.attack}")
            turn = True
            fight = False

    if warrior.health <= 0:
        print("Defeat")

    if mage.health <= 0:
        print("Victory")


    win.fill('#DCDDD8')
    buttons_draw()
    warrior.draw_minion()
    warrior.healthbar(75, 250, 100, 10, warrior_origin_health)
    mage.draw_minion()
    mage.healthbar(350, 250, 50, 10, mage_origin_health)

    pygame.display.update()
