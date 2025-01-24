from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos, *groups):
        super().__init__(*groups)
        #it is the size of the object
        self.image = pygame.Surface((48,56))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)

        #movement
        self.direction = vector(2,0)
        self.speed = 2
    
    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            print('rigth')

    def move(self):
        self.rect.topleft += self.direction * self.speed

    def update(self):
        print('palyer')