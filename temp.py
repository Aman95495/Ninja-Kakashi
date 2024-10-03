import sys

import pygame

from scripts.entities import PhysicalEntity
from scripts.utils import load_image,load_images
from scripts.tilemap import TileMap

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Ninja Kakashi")
        # pygame.display.set_icon("")
        
        self.screen = pygame.display.set_mode((640,480))
        self.display = pygame.Surface((320,240))
        self.clock = pygame.time.Clock()

        self.movement = [False, False]

        self.assets = {
            'decor'  : load_images('tiles/decor'),
            'grass'  : load_images('tiles/grass'),
            'large_decor'  : load_images('tiles/large_decor'),
            'spawners'  : load_images('tiles/spawners'),
            'stone'  : load_images('tiles/stone'),
            'player' : load_image('entities/player.png')
        }


        self.player = PhysicalEntity(self, 'player', (50,50), (8,15))
        self.tilemap = TileMap(self, tile_size=16)


    def run(self):
        while True:
            self.display.fill((14, 219, 248))

            self.tilemap.render(self.display)

            self.player.update(self.tilemap, (self.movement[1]-self.movement[0],0))
            self.player.render(self.display)



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:            # If key is pressed
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_s:
                        self.movement[1] = True
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.player.velocity[1] = -3

                if event.type == pygame.KEYUP:             # If Key is not pressed
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_s:
                        self.movement[1] = False

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))
            pygame.display.update()
            self.clock.tick(60)





if __name__ == "__main__":
    game = Game()
    game.run()