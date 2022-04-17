import tiles
import random

def load_map(map):
    for tile in map:
        print(tile['type'], end = '')

    seed = ''
    for tile in map:
        if tile['type'] == '\n':
            seed += '0'
        elif tile['type'] == tiles.blank:
            seed += '1'
        elif tile['type'] == tiles.grass:
            seed += '2'
        elif tile['type'] == tiles.water:
            seed += '3'

    return seed

def load_map_from_seed(seed):
    '''
    Loads a map from a given seed
    '''
    map = []
    for char in seed:
        if char == '0':
            tile_data = {'type': '\n'}
        elif char == '1':
            tile_data = {'type': tiles.blank}
        elif char == '2':
            tile_data = {'type': tiles.grass}
        elif char == '3':
            tile_data = {'type': tiles.water}
        else:
            tile_data = {'type': '??'}

        map.append(tile_data)
    
    load_map(map)

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