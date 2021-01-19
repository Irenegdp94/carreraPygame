import pygame,sys
width = 640
height = 480
class Game():
    runners = []
    __starLine = 20
    __finishLine = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((width,height))
#       self.__screen.fill((255,125,85))
        self.__background = pygame.image.load("imagen/background.png")
        pygame.display.set_caption("Carrera")
        
    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
            self.__screen.blit(self.__background,(0,0))
            pygame.display.flip()
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    pygame.init()
    game.competir()