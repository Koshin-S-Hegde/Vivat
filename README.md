import sys
import pygame

pygame.init()
    
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Amogus Adventures')
clock = pygame.time.Clock()


StartButton = pygame.image.load('Graphics/STARTAS.png')
StartButton_rect = StartButton.get_rect()
StartButton2 = pygame.image.load('Graphics/STARTAS2.png')
StartButton2_rect = StartButton.get_rect()
test_font = pygame.font.Font('Graphics/Pixeltype.ttf', 50)
GameStart = pygame.image.load('Graphics/gamestart.png')
text_surface = test_font.render('Click start to play!', True, 'Green')


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 400))
        self.position = (100, 70)
        self.size = (325,125)
        self.rect = pygame.Rect(self.position, self.size)
        self.color = pygame.Color("red")
        pygame.display.set_caption('Amogus Adventures')

    def run(self):
        FPS = 60
        clock = pygame.time.Clock()
    
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
 
            mouse_position = pygame.mouse.get_pos()
            left_button,_,_ = pygame.mouse.get_pressed()
            if self.rect.collidepoint(mouse_position) and left_button:
                # Clicked, do your code, start your game
                clicked = print('clicked')
                if clicked == True :
                    screen.blit(StartButton2,(0,0))
                    
            else:
                # Not clicked, do normal stuff
                screen.blit(GameStart,(0,0))
                screen.blit(StartButton,(0,0))
                screen.blit(text_surface,(115,25))
 
            clock.tick(FPS)
            pygame.display.update()

            
if __name__ == '__main__':
    pygame.init()
    Game().run()
