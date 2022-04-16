import tiles
import random

def load_map(map):
    for tile in map:
        print(tile['type'], end = '')

def new_map(rows = 10, columns = 15):
    map = []
    for row in range(rows):
        for tile in range(columns):
            if tile != 0:
                if map[tile - 1]['type'] == tiles.water:
                    # Increase chance of water generating in bigger chunks
                    try:
                        if map[tile - 2]['type'] == tiles.water:
                            tile_type = random.choices([tiles.grass, tiles.water, tiles.blank], weights = [10, 100, 5])[0]
                    except:
                        pass
                    tile_type = random.choices([tiles.grass, tiles.water, tiles.blank], weights = [60, 100, 5])[0]
                elif map[tile - 1]['type'] == tiles.blank:
                    # Prevent more than 1 ## tile from generating together (in most cases)
                    tile_type = random.choices([tiles.grass, tiles.water], weights = [100, 30])[0]
                else:
                    tile_type = random.choices([tiles.grass, tiles.water, tiles.blank], weights = [100, 30, 10])[0]
            else:
                tile_type = random.choices([tiles.grass, tiles.water, tiles.blank], weights = [100, 30, 10])[0]

            tile_data = {'type': tile_type}
            map.append(tile_data)
        map.append({'type': '\n'})

    return map