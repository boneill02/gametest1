import sys
import display
import pygame
import player
import game_map
import random

block_scale = display.display_scale * 4
block_size = 16


def get_subimage(tile, image):
    image_surface = pygame.surface.Surface(
    (block_size, block_size), pygame.SRCALPHA)
    image_surface.blit(image, (0, 0), (tile.image_x * block_size,
                                       tile.image_y * block_size, block_size, block_size))
    return image_surface


class Game:
    def __init__(self):
        self.window = display.Display()
        game_map.init_tiles()

        tilemap_l1 = []

        for i in range(0, display.display_ratio[0]):
            tilemap_l1.append([])

        for x in range(display.display_ratio[0]):
            for y in range(display.display_ratio[1]):
                if random.randint(0, 6) is not 0:
                    tilemap_l1[x].append(12)
                else:
                    tilemap_l1[x].append(15)

        tilemap_l2 = []
        for i in range(0, display.display_ratio[0] + 1):
            tilemap_l2.append([])
        
        for x in range(display.display_ratio[0] + 1):
            for y in range(display.display_ratio[1] + 1):
                if x == 5 and y == 5:
                    tilemap_l2[x].append(27)
                else:
                    tilemap_l2[x].append(-1)

        

        tilemaps = [tilemap_l1, tilemap_l2]
        self.current_map = game_map.GameMap(tilemaps)
        self.spritesheets = []
        self.spritesheets.append(pygame.image.load('img/spritesheet.png'))
        self.spritesheets[0].convert_alpha()

        self.entities = {}

        self.game_player = player.Player(
            block_size * block_scale, block_size * block_scale, self)
        self.game_player.set_image(0, 7)
        self.game_player.state = 0
        self.entities['player'] = self.game_player

        self.clock = pygame.time.Clock()

        self.ticks = 0

    def put_item(self, item, x, y, layer):
        self.current_map.tile_map[layer][x][y] = item

    def remove_item(self, x, y, layer):
        self.current_map.tile_map[layer][x][y] = -1
                    

    def start(self):
        self.running = True
        while self.running:
            if self.window.handle_events():
                keys = pygame.key.get_pressed()
                self.entities['player'].keys_check(keys, self)

                self.window.fill_screen((255, 255, 255))
                for layer in self.current_map.tile_map:
                    self.draw_layer(layer)

                for entity in self.entities.values():
                    entity.blit_image(self.window)

                self.window.refresh()
                self.clock.tick(60)

                self.ticks += 1
            else:
                self.running = False

    def draw_layer(self, layer):
        i = 0
        for x in range(display.display_ratio[0]):
            for y in range(display.display_ratio[1]):
                if len(layer[x]) > i:
                    current_tile = layer[x][y]
                    if current_tile is not -1:
                        self.window.blit(get_subimage(game_map.tiles_by_id[current_tile], self.spritesheets[0]), x * block_scale *
                                            block_size, y * block_scale * block_size, block_scale * block_size, block_scale * block_size)
                i += 1
            i = 0


if __name__ == "__main__":
    Game().start()
