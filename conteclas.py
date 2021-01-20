import pygame,sys
import random
from pygame.locals import *
width = 640
height = 480

class Runner():
    __customes = ("turtle", "fish" , "prawn", "moray", "octopus")
    def __init__(self,x=0,y=0):
        ixCustome = random.randint(0,4)
        self.custome = pygame.image.load("imagen/{}.png".format(self.__customes[ixCustome]))
        self.position = [x,y]
        self.name = ""
        

class Game():
    def __init__(self):
        self.__screen = pygame.display.set_mode((width,height))
        self.__background = pygame.image.load("imagen/background.png")
        pygame.display.set_caption("Carrera")
        
        self.runner = Runner(320,240)
    
    def start(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_UP:
                        #mover hacia arriba
                        self.runner.position[1] -= 15
                    elif event.key == K_DOWN:
                        #mover abajo
                        self.runner.position[1] += 15
                    elif event.key == K_LEFT:
                        #mover izquierda
                        self.runner.position[0] -= 15
                    elif event.key == K_RIGHT:
                        #mover derecha
                        self.runner.position[0] += 15
                    else:
                        pass
            self.__screen.blit(self.__background,(0,0))
            self.__screen.blit(self.runner.custome,self.runner.position)
            
            pygame.display.flip()
print("my name is {}".format(__name__))

if __name__ == "__main__":
    game = Game()
    pygame.font.init()
    game.start()