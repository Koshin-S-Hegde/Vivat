import sys
import pygame
import time

pygame.init()
    
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Amogus Adventures')
clock = pygame.time.Clock()


StartButton = pygame.image.load('Graphics/STARTAS.png')
StartButton_rect = StartButton.get_rect()
StartButton2 = pygame.image.load('Graphics/STARTAS2.png')
StartButton2_rect = StartButton.get_rect()
test_font = pygame.font.Font('Graphics/Pixeltype.ttf', 50)
GameStart = pygame.image.load('Graphics/gamestart.png').convert()
text_surface = test_font.render('', True, 'Green')


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 400))
        self.position = (100, 70)
        self.size = (325,125)
        self.rect = pygame.Rect(self.position, self.size)
        pygame.display.set_caption('Amogus Adventures')

    def run(self):
        FPS = 60
        clock = pygame.time.Clock()
    
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if mouse_position(self.rect):
                screen.blit(StartButton2,(0,0))
            mouse_position = pygame.mouse.get_pos()
            left_button,_,_ = pygame.mouse.get_pressed()
            if not (self.rect.collidepoint(mouse_position) and left_button):
                # Not clicked, do normal stuff
                screen.blit(StartButton,(0,0))
                    
            else:
                # Clicked, do your code, start your game
                clicked = print('clicked')
                
                screen.blit(StartButton2,(0,0))

            clock.tick(FPS)
            pygame.display.update()

            screen.blit(GameStart,(0,0))
            screen.blit(text_surface,(115,25))


            
if __name__ == '__main__':
    pygame.init()
    Game().run()
