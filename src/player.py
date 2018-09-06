import pygame
import gametest1
import game_map


class Player:
    def __init__(self, w, h, game):
        self.spritesheet = game.spritesheets[0]
        self.spritesheet.convert_alpha()
        self.x = 0
        self.y = 0
        self.w = w
        self.h = h
        self.movement_length = 5
        self.anim_speed = 15
        self.moving = False
        self.moving_ticks = 0
        self.state = 0
        self.look_direction = 3  # 0: Left 1: Up 2: Down 3: Right
        self.has_item = False
        self.edown = False
        self.item_loc = [5, 5]

    def blit_image(self, window):
        self.set_image(self.state, self.look_direction)

        window.blit(self.cropped_image, self.x, self.y, self.w, self.h)

    def set_image(self, x, y):
        self.cropped_image = gametest1.get_subimage(
            game_map.Tile(x, y), self.spritesheet)

    def keys_check(self, keys, game):
        self.moving = False
        if keys[pygame.K_LSHIFT]:
            self.movement_length = 10
            self.anim_speed = 5
        else:
            self.movement_length = 5
            self.anim_speed = 10
        if keys[pygame.K_w]:
            self.moving = True
            self.move('N', game)
            self.look_direction = 1
        if keys[pygame.K_s]:
            self.moving = True
            self.move('S', game)
            self.look_direction = 2
        if keys[pygame.K_a]:
            self.moving = True
            self.move('W', game)
            self.look_direction = 0
        if keys[pygame.K_d]:
            self.moving = True
            self.move('E', game)
            self.look_direction = 3
        if keys[pygame.K_e]:
            if not self.edown:
                new_x = self.x / (gametest1.block_size * gametest1.block_scale)
                new_y = self.y / (gametest1.block_size * gametest1.block_scale)
                collisions = game.current_map.get_collide(new_x, new_y)
                if collisions[0] or collisions[1] or collisions[2] or collisions[3]:
                    game.remove_item(self.item_loc[0], self.item_loc[1], 1)
                    self.has_item = True
                else:
                    if self.has_item:
                        game.put_item(27, int(new_x) + 1, int(new_y) + 1, 1)
                        self.item_loc = [int(new_x) + 1, int(new_y) + 1]
                        self.has_item = False
                self.edown = True
        else:
            self.edown = False

        if not self.moving:
            self.state = 0

    def move(self, direction, game):
        new_x = self.x / (gametest1.block_size * gametest1.block_scale)
        new_y = self.y / (gametest1.block_size * gametest1.block_scale)
        
        collisions = game.current_map.get_collide(new_x, new_y)
        
        

        self.moving = True
        self.moving_ticks += 1
        if self.moving_ticks % self.anim_speed == 1 and self.state == 1:
            self.state = 2
        elif self.moving_ticks % self.anim_speed == 1 and self.state == 2:
            self.state = 1
        elif self.moving_ticks % self.anim_speed == 1 and self.state == 0:
            self.state = 1

        if direction == 'N' and not collisions[3]:
            self.y -= self.movement_length
        elif direction == 'S' and not collisions[2]:
            self.y += self.movement_length
        elif direction == 'E' and not collisions[0]:
            self.x += self.movement_length
        elif direction == 'W' and not collisions[1]:
            self.x -= self.movement_length
