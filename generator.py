import tiles
import random

def load_map(map):
    for tile in map:
        print(tile, end = '')

def new_map(rows = 10, columns = 15):
    map = []
    for row in range(rows):
        for tile in range(columns):
            map.append(random.choices([tiles.grass, tiles.water, tiles.blank], weights = [100, 30, 10])[0])
        map.append('\n')

    return map