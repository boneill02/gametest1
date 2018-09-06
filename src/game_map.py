import display


class Tile:
    def __init__(self, image_x, image_y):
        self.image_x = image_x
        self.image_y = image_y
        self.draw_x = 0
        self.draw_y = 0


class GameMap:
    def __init__(self, tile_map):
        self.tile_map = tile_map

    def get_collide(self, x, y):
        directions = [False, False, False, False]
        bounds = (int(x), int(y), int(x) + 1, int(y) + 1)

        coll_tiles = self.tile_map[1]


        # Right collide
        if x > display.display_ratio[0] - 1:
            directions[0] = True
        else:
            if coll_tiles[bounds[2]][bounds[3]] != -1 or coll_tiles[bounds[2]][bounds[1]] != -1:
                directions[0] = True
        
        # Left collide
        if x < 0:
            directions[1] = True
        else:
            if coll_tiles[bounds[0]][bounds[1]] != -1 or coll_tiles[bounds[2]][bounds[1]] != -1 or coll_tiles[bounds[0]][bounds[3]] != -1:
            	directions[1] = True

        # Down collide
        if y > display.display_ratio[1] - 1:
            directions[2] = True
        else:
            if coll_tiles[bounds[0]][bounds[3]] != -1 or coll_tiles[bounds[2]][bounds[3]] != -1:
                directions[2] = True

        # Up collide
        if y < 0:
            directions[3] = True
        else:
            if coll_tiles[bounds[0]][bounds[3]] != -1 or coll_tiles[bounds[0]][bounds[1]] != -1:
                directions[3] = True


        return directions


tiles_by_id = []


def init_tiles():
    global tiles_by_id
    for y in range(4):
        for x in range(8):
            tiles_by_id.append(Tile(x, y))
    print('Initialized ' + str(len(tiles_by_id)) + ' tiles.', )
