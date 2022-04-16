# Console tilemap generator

An experiment on generating game maps in the console, using python.

## Usage
**Basic usage**

*Generates a 15x10 map and prints it to the console.*
```
import generator

map = generator.new_map()
generator.load_map(map)
```
*You can also modify the number of rows or columns generated*
```
import generator

map = generator.new_map(columns = 50)
generator.load_map(map)
```

