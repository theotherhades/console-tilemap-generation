import generator

map = generator.new_map(columns = 50)
seed = generator.load_map(map)

while True:
    x = input('Do you want to save the map seed? (y/n) ')
    if x == 'y':
        print('Seed: ' + seed)
        break
    elif x == 'n':
        break

while True:
    load = input('Paste a seed you want to load: ')
    generator.load_map_from_seed(load)