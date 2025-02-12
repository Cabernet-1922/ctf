# Tuning Parkour [794 points] (6 solves)
```python
path = """Glass Pane 102
Melon Stem 105
Nether Brick Stairs 114
Iron Bars 101
Stone Bricks 98
Melon Stem 105
Nether Brick Stairs 114
Red Mushroom Block 100
Redstone Lamp (inactive) 123
Wooden Pressure Plate 72
Moss Stone 48
End Portal 119
White Stained Glass 95
Red Mushroom Block 100
Moss Stone 48
Fire 51
Oak Wood Stairs 53
White Stained Glass 95
Obsidian 49
Redstone Wire 55
White Stained Glass 95
Glass Pane 102
Fire 51
Fire 51
Brick Stairs 108
White Stained Glass 95
Jukebox 84
Moss Stone 48
White Stained Glass 95
Oak Fence Gate 107
Mycelium 110
Ice 79
End Portal 119
White Stained Glass 95
Rail 66
Brick Stairs 108
Moss Stone 48
Brown Mushroom Block 99
Oak Fence Gate 107
White Stained Glass 95
Obsidian 49
Red Mushroom Block 100
Oak Wood Stairs 53
Double Oak Wood Slab 125"""

import re
res = ""
for i in path.splitlines():
    res += chr(int(re.findall(r'(\d+)', i)[0]))
print(res)
```

The path of parkour is actually representing the ids of items|blocks, so simply record block in the path and get the corresponding ids.