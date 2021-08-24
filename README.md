import sys
import pygame

pygame.init()
    
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Amogus Adventures')
clock = pygame.time.Clock()

test_font = pygame.font.Font('Graphics/Pixeltype.ttf', 50)
StartButton = pygame.image.load('Graphics/STARTAS.png')
GameStart = pygame.image.load('Graphics/gamestart.png')
text_surface = test_font.render('Press enter to play!', True, 'Green')
StartButton2 = pygame.image.load('Graphics/STARTAS2.png')

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
                print('clicked')
                
                pygame.draw.rect(self.screen, pygame.Color("green"), self.rect)
            else:
                # Not clicked, do normal stuff
                pygame.draw.rect(self.screen, pygame.Color("red"), self.rect)
 
            clock.tick(FPS)
            pygame.display.update()

            screen.blit(GameStart,(0,0))
            screen.blit(StartButton,(0,0))
            screen.blit(text_surface,(115,25))
            
if __name__ == '__main__':
    pygame.init()
    Game().run()
