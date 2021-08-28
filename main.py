import pygame
import pyjokes
from pygame.locals import *
import time
import sys
import random


class Game:
    def __init__(self):
        self.w = 750
        self.h = 500
        self.reset = True
        self.active = False
        self.input_text = ''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.accuracy = '0%'
        self.results = 'Time:0 Accuracy:0 % Wpm:0 '
        self.wpm = 0
        self.end = False
        self.HEAD_C = (255, 213, 102)
        self.TEXT_C = (240, 240, 240)
        self.RESULT_C = (255, 70, 70)


        pygame.init()
        self.open_img = pygame.image.load('images/icon.png')
        self.open_img = pygame.transform.scale(self.open_img, (self.w, self.h))

        self.bg = pygame.image.load('images/background.jpg')
        self.bg = pygame.transform.scale(self.bg, (750, 500))

        self.screen = pygame.display.set_mode((self.w, self.h))

    def draw_text(self, screen, msg, y, fsize, color):
        font = pygame.font.Font(None, fsize)
        text = font.render(msg, 1, color)
        text_rect = text.get_rect(center=(self.w / 2, y))
        screen.blit(text, text_rect)
        pygame.display.update()

    def get_sentence(self):
        sentence = pyjokes.get_joke()

        if len(sentence) <= 75:
            return sentence

    def show_results(self, screen):
        if not self.end:

            # Calculate time
            self.total_time = time.time() - self.time_start

            # Calculate accuracy
            count = 0

            for i, c in enumerate(self.word):
                try:
                    if self.input_text[i] == c:
                        count += 1
                except:
                    pass
            self.accuracy = count / len(self.word) * 100

            # Calculate words per minute
            self.wpm = len(self.input_text) * 60 / (5 * self.total_time)
            self.end = True
            print(self.total_time)
            print(self.results)
            pygame.display.update()

    def run(self):
        self.reset_game()
        self.running = True

        while self.running:
            clock = pygame.time.Clock()
            self.screen.fill((0, 0, 0), (50, 250, 650, 50))
            pygame.draw.rect(self.screen, self.HEAD_C, (50, 250, 650, 50), 2)

            # update the text of user input
            self.draw_text(self.screen, self.input_text, 274, 26, (250, 250, 250))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()

                    # position of input box
                    if 50 <= x <= 650 and 250 <= y <= 300:
                        self.active = True
                        self.input_text = ''
                        self.time_start = time.time()

                    # position of reset box
                    if 310 <= x <= 510 and y >= 390 and self.end:
                        self.reset_game()
                        x, y = pygame.mouse.get_pos()

                elif event.type == pygame.KEYDOWN:
                    if self.active and not self.end:
                        if event.key == pygame.K_RETURN:
                            print(self.input_text)
                            self.show_results(self.screen)
                            print(self.results)
                            self.draw_text(
                                self.screen, self.results, 350, 28, self.RESULT_C)
                            self.end = True

                        elif event.key == pygame.K_BACKSPACE:
                            self.input_text = self.input_text[:-1]
                        else:
                            try:
                                self.input_text += event.unicode
                            except:
                                pass

            pygame.display.update()

        clock.tick(60)

        def reset_game(self):
            self.screen.blit(self.open_img, (0, 0))
            pygame.display.update()
            time.sleep(1)
            self.reset = False
            self.end = False
            self.input_text = ''
            self.word = ''
            self.time_start = 0
            self.total_time = 0
            self.wpm = 0
            self.end = False
            self.HEAD_C = (255, 213, 102)
            self.TEXT_C = (240, 240, 240)
            self.RESULT_C = (255, 70, 70)

            pygame.init()
            self.open_img = pygame.image.load('images/type-speed-open.png')
            self.open_img = pygame.transform.scale(self.open_img, (self.w, self.h))

            self.bg = pygame.image.load('images/background.jpg')
            self.bg = pygame.transform.scale(self.bg, (750, 500))

            self.screen = pygame.display.set_mode((self.w, self.h))
            pygame.display.set_caption('Typing v.1')

        def draw_text(self, screen, msg, y, fsize, color):
            font = pygame.font.Font(None, fsize)
            text = font.render(msg, 1, color)
            text_rect = text.get_rect(center=(self.w / 2, y))
            screen.blit(text, text_rect)
            pygame.display.update()

        def get_sentence(self):
            sentence = pyjokes.get_joke()
            if len(sentence) <= 75:
                return sentence

        def show_results(self, screen):
            if not self.end:

                # Calculate time
                self.total_time = time.time() - self.time_start

                # Calculate accuracy
                count = 0
                for i, c in enumerate(self.word):
                    try:
                        if self.input_text[i] == c:
                            count += 1
                    except:
                        pass
                    self.accuracy = count / len(self.word) * 100

                    # Calculate words per minute
                    self.wpm = len(self.input_text) * 60 / (5 * self.total_time)
                    self.end = True
                    print(self.total_time)

                    self.results = 'Time:' + str(round(self.total_time)) + " secs   Accuracy:" + str(
                        round(self.accuracy)) + "%" + '   Wpm: ' + str(round(self.wpm))

                    # screen.blit(self.time_img, (80,320))
                    screen.blit(self.time_img, (self.w / 2 - 75, self.h - 140))
                    self.draw_text(screen, "Reset", self.h - 70, 26, (100, 100, 100))

                    print(self.results)
                    pygame.display.update()

            def run(self):
                self.reset_game()

                self.running = True
                while self.running:
                    clock = pygame.time.Clock()
                    self.screen.fill((0, 0, 0), (50, 250, 650, 50))
                    pygame.draw.rect(self.screen, self.HEAD_C, (50, 250, 650, 50), 2)

                    # update the text of user input
                    self.draw_text(self.screen, self.input_text, 274, 26, (250, 250, 250))
                    pygame.display.update()

                    for event in pygame.event.get():
                        if event.type == QUIT:
                            self.running = False
                            sys.exit()

                        elif event.type == pygame.MOUSEBUTTONUP:
                            x, y = pygame.mouse.get_pos()

                            # position of input box
                            if 50 <= x <= 650 and 250 <= y <= 300:
                                self.active = True
                                self.input_text = ''
                                self.time_start = time.time()

                            # position of reset box
                            if 310 <= x <= 510 and y >= 390 and self.end:
                                self.reset_game()
                                x, y = pygame.mouse.get_pos()
                            elif event.type == pygame.KEYDOWN:

                                if self.active and not self.end:

                                    if event.key == pygame.K_RETURN:
                                        print(self.input_text)
                                        self.show_results(self.screen)
                                        print(self.results)
                                        self.draw_text(
                                            self.screen, self.results, 350, 28, self.RESULT_C)
                                        self.end = True

                                    elif event.key == pygame.K_BACKSPACE:
                                        self.input_text = self.input_text[:-1]
                                    else:
                                        try:
                                            self.input_text += event.unicode
                                        except:
                                            pass

                            pygame.display.update()
