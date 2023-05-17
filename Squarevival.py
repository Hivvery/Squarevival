#Import modules and initialize Pygame
import math, pygame, random, sys
pygame.init()

#DICTIONARIES
#Window info
Config = {
    "Framerate"    : 30           ,
    "ScreenCaption": "Squarevival Alpha",
    "ScreenX"      : 720          ,
    "ScreenY"      : 720          ,
}
#Images
Images = {
    "entity-item-apple"         : pygame.image.load("Images/squarevival-entity-item-apple.png"         ),
    "entity-item-bright_wood"   : pygame.image.load("Images/squarevival-entity-item-bright_wood.png"   ),
    "entity-item-cactus_spike"  : pygame.image.load("Images/squarevival-entity-item-cactus_spike.png"  ),
    "entity-item-coal"          : pygame.image.load("Images/squarevival-entity-item-coal.png"          ),
    "entity-item-dark_wood"     : pygame.image.load("Images/squarevival-entity-item-dark_wood.png"     ),
    "entity-item-diamond"       : pygame.image.load("Images/squarevival-entity-item-diamond.png"       ),
    "entity-item-iron_bar"      : pygame.image.load("Images/squarevival-entity-item-iron_bar.png"      ),
    "entity-item-leaf"          : pygame.image.load("Images/squarevival-entity-item-leaf.png"          ),
    "entity-u"                  : pygame.image.load("Images/squarevival-entity-u.png"                  ),
    "ground-cold_water"         : pygame.image.load("Images/squarevival-ground-cold_water.png"         ),
    "ground-dark_grass"         : pygame.image.load("Images/squarevival-ground-dark_grass.png"         ),
    "ground-dirt"               : pygame.image.load("Images/squarevival-ground-dirt.png"               ),
    "ground-grass"              : pygame.image.load("Images/squarevival-ground-grass.png"              ),
    "ground-ice"                : pygame.image.load("Images/squarevival-ground-ice.png"                ),
    "ground-lava"               : pygame.image.load("Images/squarevival-ground-lava.png"               ),
    "ground-mud"                : pygame.image.load("Images/squarevival-ground-mud.png"                ),
    "ground-sand"               : pygame.image.load("Images/squarevival-ground-sand.png"               ),
    "ground-sand_bricks_ground" : pygame.image.load("Images/squarevival-ground-sand_bricks_ground.png" ),
    "ground-snow"               : pygame.image.load("Images/squarevival-ground-snow.png"               ),
    "ground-stone_bricks_ground": pygame.image.load("Images/squarevival-ground-stone_bricks_ground.png"),
    "ground-stone_ground"       : pygame.image.load("Images/squarevival-ground-stone_ground.png"       ),
    "ground-warm_water"         : pygame.image.load("Images/squarevival-ground-warm_water.png"         ),
    "ground-water"              : pygame.image.load("Images/squarevival-ground-water.png"              ),
    "item-apple"                : pygame.image.load("Images/squarevival-item-apple.png"                ),
    "item-bright_wood"          : pygame.image.load("Images/squarevival-item-bright_wood.png"          ),
    "item-cactus_spike"         : pygame.image.load("Images/squarevival-item-cactus_spike.png"         ),
    "item-coal"                 : pygame.image.load("Images/squarevival-item-coal.png"                 ),
    "item-dark_wood"            : pygame.image.load("Images/squarevival-item-dark_wood.png"            ),
    "item-diamond"              : pygame.image.load("Images/squarevival-item-diamond.png"              ),
    "item-iron_bar"             : pygame.image.load("Images/squarevival-item-iron_bar.png"             ),
    "item-leaf"                 : pygame.image.load("Images/squarevival-item-leaf.png"                 ),
    "object-apple_tree"         : pygame.image.load("Images/squarevival-object-apple_tree.png"         ),
    "object-box"                : pygame.image.load("Images/squarevival-object-box.png"                ),
    "object-bright_tree"        : pygame.image.load("Images/squarevival-object-bright_tree.png"        ),
    "object-bright_wood"        : pygame.image.load("Images/squarevival-object-bright_wood.png"        ),
    "object-cactus"             : pygame.image.load("Images/squarevival-object-cactus.png"             ),
    "object-cave"               : pygame.image.load("Images/squarevival-object-cave.png"               ),
    "object-christmas_tree"     : pygame.image.load("Images/squarevival-object-christmas_tree.png"     ),
    "object-coal_ore"           : pygame.image.load("Images/squarevival-object-coal_ore.png"           ),
    "object-dark_tree"          : pygame.image.load("Images/squarevival-object-dark_tree.png"          ),
    "object-dark_wood"          : pygame.image.load("Images/squarevival-object-dark_wood.png"          ),
    "object-diamond_ore"        : pygame.image.load("Images/squarevival-object-diamond_ore.png"        ),
    "object-iron_ore"           : pygame.image.load("Images/squarevival-object-iron_ore.png"           ),
    "object-sand_bricks"        : pygame.image.load("Images/squarevival-object-sand_bricks.png"        ),
    "object-stone"              : pygame.image.load("Images/squarevival-object-stone.png"              ),
    "object-stone_bricks"       : pygame.image.load("Images/squarevival-object-stone_bricks.png"       ),
    "object-torch"              : pygame.image.load("Images/squarevival-object-torch.png"              ),
}
#Pressed keys
Keys = {
    "A": False,
    "D": False,
    "S": False,
    "W": False,
}
#Text to be shown in-game
Names = {
    ""                        : ""              ,
    "entity-item-apple"       : "Apple"         ,
    "entity-item-bright_wood" : "Bright Wood"   ,
    "entity-item-cactus_spike": "Cactus Spike"  ,
    "entity-item-coal"        : "Coal"          ,
    "entity-item-dark_wood"   : "Dark Wood"     ,
    "entity-item-diamond"     : "Diamond"       ,
    "entity-item-iron_bar"    : "Iron Bar"      ,
    "entity-item-leaf"        : "Leaf"          ,
    "entity-u"                : "U"             ,
    "ground-cold_water"       : "Cold Water"    ,
    "ground-dark_grass"       : "Dark Grass"    ,
    "ground-dirt"             : "Dirt"          ,
    "ground-grass"            : "Grass"         ,
    "ground-ice"              : "Ice"           ,
    "ground-lava"             : "Lava"          ,
    "ground-mud"              : "Mud"           ,
    "ground-sand"             : "Sand"          ,
    "ground-snow"             : "Snow"          ,
    "ground-stone_ground"     : "Stone Ground"  ,
    "ground-warm_water"       : "Warm Water"    ,
    "ground-water"            : "Water"         ,
    "item-apple"              : "Apple"         ,
    "item-bright_wood"        : "Bright Wood"   ,
    "iten-cactus_spike"       : "Cactus Spike"  ,
    "item-dark_wood"          : "Dark Wood"     ,
    "item-leaf"               : "Leaf"          ,
    "object-apple_tree"       : "Apple Tree"    ,
    "object-box"              : "Box"           ,
    "object-bright_tree"      : "Bright Tree"   ,
    "object-bright_wood"      : "Bright Wood"   ,
    "object-cactus"           : "Cactus"        ,
    "object-cave"             : "Cave"          ,
    "object-christmas_tree"   : "Christmas Tree",
    "object-coal_ore"         : "Coal Ore"      ,
    "object-dark_tree"        : "Dark Tree"     ,
    "object-dark_wood"        : "Dark Wood"     ,
    "object-iron_ore"         : "Iron Ore"      ,
    "object-stone"            : "Stone"         ,
    "object-torch"            : "Torch"         ,
}
#World settings
Settings = {
    "GridH"   : 90,
    "GridW"   : 90,
    "Points"  : 6,
    "TileSize": 0,
}
Settings["TileSize"] = Config["ScreenY"] / Settings["GridH"]
#Walk speeds
Speeds = {
    ""                          : 1,
    "ground-cold_water"         : 0.4,
    "ground-dark_grass"         : 1,
    "ground-dirt"               : 1,
    "ground-grass"              : 1,
    "ground-ice"                : 2,
    "ground-lava"               : 0.5,
    "ground-mud"                : 0.25,
    "ground-sand"               : 1,
    "ground-sand_bricks_ground" : 1,
    "ground-snow"               : 1,
    "ground-stone_bricks_ground": 1,
    "ground-stone_ground"       : 1,
    "ground-warm_water"         : 0.6,
    "ground-water"              : 0.5,
    "object-apple_tree"         : 1,
    "object-box"                : 1,
    "object-bright_tree"        : 1,
    "object-bright_wood"        : 1,
    "object-cactus"             : 0.5,
    "object-cave"               : 1,
    "object-christmas_tree"     : 1,
    "object-coal_ore"           : 1,
    "object-dark_tree"          : 1,
    "object-dark_wood"          : 1,
    "object-diamond_ore"        : 1,
    "object-iron_ore"           : 1,
    "object-sand_bricks"        : 1,
    "object-stone"              : 1,
    "object-stone_bricks"       : 1,
    "object-torch"              : 1,
}
#Boolean variables
VariablesBoolean = {
    "key_a"         : False,
    "key_d"         : False,
    "key_s"         : False,
    "key_w"         : False,
    "menu_debug"    : False,
    "menu_inventory": False,
}
#Number variables
VariablesNumber = {
    "camera_x"           : 0,
    "camera_y"           : 0,
    "camera_z"           : Settings["GridW"] / 18,
    "hotbar"             : 0,
    "player_posx"        : 0,
    "player_posy"        : 0,
    "player_tile"        : 0,
    "player_tileposx"    : 0,
    "player_tileposy"    : 0,
    "player_vel"         : 0,
    "structure_depth"    : 0,
    "time_day_length"    : 300,
    "time_day_percentage": 0,
    "time_frames"        : 0,
    "time_seconds"       : 0,
}
VariablesNumber["camera_z"]

#LISTS
#Tile list
#Grid[?][0]: Water level
#Grid[?][1]: Temperature
#Grid[?][2]: Humidity
#Grid[?][3]: Biome
#Grid[?][4]: Ground
#Grid[?][5]: Object
Grid = [[0, 0, 0, "Ocean", "ground-water", ""] for a in range(Settings["GridW"] * Settings["GridH"])]
#Images list
ImagesList = [
    "entity-item-apple"         ,
    "entity-item-bright_wood"   ,
    "entity-item-cactus_spike"  ,
    "entity-item-coal"          ,
    "entity-item-dark_wood"     ,
    "entity-item-diamond"       ,
    "entity-item-iron_bar"      ,
    "entity-item-leaf"          ,
    "entity-u"                  ,
    "ground-cold_water"         ,
    "ground-dark_grass"         ,
    "ground-dirt"               ,
    "ground-grass"              ,
    "ground-ice"                ,
    "ground-lava"               ,
    "ground-mud"                ,
    "ground-sand"               ,
    "ground-sand_bricks_ground" ,
    "ground-snow"               ,
    "ground-stone_bricks_ground",
    "ground-stone_ground"       ,
    "ground-warm_water"         ,
    "ground-water"              ,
    "item-apple"                ,
    "item-bright_wood"          ,
    "item-cactus_spike"         ,
    "item-coal"                 ,
    "item-dark_wood"            ,
    "item-diamond"              ,
    "item-iron_bar"             ,
    "item-leaf"                 ,
    "object-apple_tree"         ,
    "object-box"                ,
    "object-bright_tree"        ,
    "object-bright_wood"        ,
    "object-cactus"             ,
    "object-cave"               ,
    "object-christmas_tree"     ,
    "object-coal_ore"           ,
    "object-dark_tree"          ,
    "object-dark_wood"          ,
    "object-diamond_ore"        ,
    "object-iron_ore"           ,
    "object-sand_bricks"        ,
    "object-stone"              ,
    "object-stone_bricks"       ,
    "object-torch"              ,
]
#Inventory
Inventory = [["", 0] for a in range(32)]
InventoryMargins =  [[(i % 8) * 89 + 8, (i // 8) * -89 + Config["ScreenY"] - 89] for i in range(32)]
#Objects you can't walk through
ObjectsSolid = [
    "object-apple_tree"         ,
    "object-bright_tree"        ,
    "object-bright_wood"        ,
    "object-cave"               ,
    "object-christmas_tree"     ,
    "object-coal_ore"           ,
    "object-dark_tree"          ,
    "object-dark_wood"          ,
    "object-diamond_ore"        ,
    "object-iron_ore"           ,
    "object-sand_bricks"        ,
    "object-stone"              ,
    "object-stone_bricks"       ,
    "object-torch"              ,
]
#World terrain points
Points = [[a, 1, random.randrange(0, Config["ScreenX"]), random.randrange(0, Config["ScreenY"])] for a in range(3) for b in range(int(Settings["Points"] / 2))] + [[a, -1, random.randrange(0, Config["ScreenX"]), random.randrange(0, Config["ScreenY"])] for a in range(3) for b in range(int(Settings["Points"] / 2))]

#VARIABLES
structure_depth, sprites_group_entity, sprites_group_tile = 0, pygame.sprite.Group(), pygame.sprite.Group()

#CLASSES
#Entities (The player, items etc.)
class Entity(pygame.sprite.Sprite):
    def __init__(self, identity, type, posx, posy, sizx, sizy):
        pygame.sprite.Sprite.__init__(self)
        self.posx = posx
        self.posy = posy
        self.sizx = sizx
        self.sizy = sizy
        self.id = identity
        self.tile = round(self.posx / Settings["TileSize"] - 0.5) + round(self.posy / Settings["TileSize"] - 0.5) * Settings["GridH"]
        self.type = type
        self.image = Images[self.type]
        self.rect = self.image.get_rect()
        self.rect.center = ((self.posx - VariablesNumber["camera_x"]) * VariablesNumber["camera_z"] + Config["ScreenX"] / 2, (self.posy - VariablesNumber["camera_y"]) * VariablesNumber["camera_z"] + Config["ScreenY"] / 2)
    def update(self):
        if self.type.__contains__("entity-item"):
            #Collect items
            if math.sqrt((self.posx - VariablesNumber["player_posx"]) ** 2 + (self.posy - VariablesNumber["player_posy"]) ** 2) <= Settings["TileSize"]:
                item(self.type.replace("entity-", ""))
                self.kill()
        elif self.type == "entity-u":
            #Set player speed
            VariablesNumber["player_vel"] = (Settings["TileSize"] / 8) * Speeds[Grid[VariablesNumber["player_tile"]][4]] * Speeds[Grid[VariablesNumber["player_tile"]][5]]
            #Move player if the inventory is closed and in the opposite direction if the player walks into an object
            if not VariablesBoolean["menu_inventory"]:
                if Keys["A"]:
                    self.posx -= VariablesNumber["player_vel"]
                    if VariablesNumber["player_tileposx"] % 1 > 0.5 and ObjectsSolid.__contains__(Grid[VariablesNumber["player_tile"] - 1][5]):
                        self.posx += VariablesNumber["player_vel"]
                if Keys["D"]:
                    self.posx += VariablesNumber["player_vel"]
                    if VariablesNumber["player_tileposx"] % 1 < 0.5 and ObjectsSolid.__contains__(Grid[VariablesNumber["player_tile"] + 1][5]):
                        self.posx -= VariablesNumber["player_vel"]
                if Keys["S"]:
                    self.posy += VariablesNumber["player_vel"]
                    if VariablesNumber["player_tileposy"] % 1 < 0.5 and ObjectsSolid.__contains__(Grid[VariablesNumber["player_tile"] + Settings["GridW"]][5]):
                        self.posy -= VariablesNumber["player_vel"]
                if Keys["W"]:
                    self.posy -= VariablesNumber["player_vel"]
                    if VariablesNumber["player_tileposy"] % 1 > 0.5 and ObjectsSolid.__contains__(Grid[VariablesNumber["player_tile"] - Settings["GridW"]][5]):
                        self.posy += VariablesNumber["player_vel"]
            VariablesNumber["player_tileposx"] = self.posx * (Settings["GridW"] / Config["ScreenX"]) - 0.5
            VariablesNumber["player_tileposy"] = self.posy * (Settings["GridH"] / Config["ScreenY"]) - 0.5
            #Keep player away from the edge of the world
            if VariablesNumber["player_tileposx"] <= 0:
                self.posx = 4
            elif VariablesNumber["player_tileposx"] >= Settings["GridW"] - 1:
                self.posx = Config["ScreenX"] - 4
            if VariablesNumber["player_tileposy"] <= 0:
                self.posy = 4
            elif VariablesNumber["player_tileposy"] >= Settings["GridH"] - 1:
                self.posy = Config["ScreenY"] - 4
            VariablesNumber["player_posx"] = self.posx
            VariablesNumber["player_posy"] = self.posy
            self.tile = round(self.posx / Settings["TileSize"] - 0.5) + round(self.posy / Settings["TileSize"] - 0.5) * Settings["GridH"]
            VariablesNumber["player_tile"] = self.tile
        self.rect.center = ((self.posx - VariablesNumber["camera_x"]) * VariablesNumber["camera_z"] + Config["ScreenX"] / 2, (self.posy - VariablesNumber["camera_y"]) * VariablesNumber["camera_z"] + Config["ScreenY"] / 2)
#Tiles
class Tile(pygame.sprite.Sprite):
    def __init__(self, identity, posx, posy, sizx, sizy):
        pygame.sprite.Sprite.__init__(self)
        self.posx = posx
        self.posy = posy
        self.sizx = sizx
        self.sizy = sizy
        self.id = identity
        self.image = Images[Grid[self.id][4]]
        self.rect = self.image.get_rect()
        self.rect.center = ((self.posx - VariablesNumber["camera_x"]) * VariablesNumber["camera_z"] + Config["ScreenX"] / 2, (self.posy - VariablesNumber["camera_y"]) * VariablesNumber["camera_z"] + Config["ScreenY"] / 2)
    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == 1:
                if not Grid[self.id][5] == "":
                    if Grid[self.id][5] == "object-apple_tree":
                        itementity("entity-item-bright_wood", self.posx + random.randrange(-4, 4) * Settings["TileSize"] / 16, self.posy + random.randrange(-4, 4) * Settings["TileSize"] / 16)
                        if random.randrange(0, 100) <= 50:
                            itementity("entity-item-apple", self.posx + random.randrange(-4, 4) * Settings["TileSize"] / 16, self.posy + random.randrange(-4, 4) * Settings["TileSize"] / 16)
                    elif Grid[self.id][5] == "object-bright_tree":
                        itementity("entity-item-bright_wood", self.posx + random.randrange(-4, 4) * Settings["TileSize"] / 16, self.posy + random.randrange(-4, 4) * Settings["TileSize"] / 16)
                        if random.randrange(0, 100) <= 50:
                            itementity("entity-item-bright_wood", self.posx + random.randrange(-4, 4) * Settings["TileSize"] / 16, self.posy + random.randrange(-4, 4) * Settings["TileSize"] / 16)
                    elif Grid[self.id][5] == "object-cactus":
                        if random.randrange(0, 100) <= 25:
                            itementity("entity-item-cactus_spike", self.posx + random.randrange(-4, 4) * Settings["TileSize"] / 16, self.posy + random.randrange(-4, 4) * Settings["TileSize"] / 16)
                    elif Grid[self.id][5] == "object-coal_ore":
                        itementity("entity-item-coal", self.posx + random.randrange(-4, 4) * Settings["TileSize"] / 16, self.posy + random.randrange(-4, 4) * Settings["TileSize"] / 16)
                        if random.randrange(0, 100) <= 20:
                            itementity("entity-item-coal", self.posx + random.randrange(-4, 4) * Settings["TileSize"] / 16, self.posy + random.randrange(-4, 4) * Settings["TileSize"] / 16)
                    elif Grid[self.id][5] == "object-dark_tree":
                        itementity("entity-item-dark_wood", self.posx + random.randrange(-4, 4) * Settings["TileSize"] / 16, self.posy + random.randrange(-4, 4) * Settings["TileSize"] / 16)
                        if random.randrange(0, 100) <= 50:
                            itementity("entity-item-dark_wood", self.posx + random.randrange(-4, 4) * Settings["TileSize"] / 16, self.posy + random.randrange(-4, 4) * Settings["TileSize"] / 16)
                    elif Grid[self.id][5] == "object-diamond_ore":
                        itementity("entity-item-diamond", self.posx + random.randrange(-4, 4) * Settings["TileSize"] / 16, self.posy + random.randrange(-4, 4) * Settings["TileSize"] / 16)
                    elif Grid[self.id][5] == "object-iron_ore":
                        itementity("entity-item-iron_bar", self.posx + random.randrange(-4, 4) * Settings["TileSize"] / 16, self.posy + random.randrange(-4, 4) * Settings["TileSize"] / 16)
                        if random.randrange(0, 100) <= 10:
                            itementity("entity-item-iron_bar", self.posx + random.randrange(-4, 4) * Settings["TileSize"] / 16, self.posy + random.randrange(-4, 4) * Settings["TileSize"] / 16)
                    Grid[self.id][5] = ""
                Grid[self.id][4] = "ground-dirt"
        if not Grid[self.id][4] == "":
            self.image = Images[Grid[self.id][4]]
        self.rect.center = ((self.posx - VariablesNumber["camera_x"]) * VariablesNumber["camera_z"] + Config["ScreenX"] / 2, (self.posy - VariablesNumber["camera_y"]) * VariablesNumber["camera_z"] + Config["ScreenY"] / 2)

#FUNCTIONS
#Add an item to the inventory
def item(item):
    for a in range(len(Inventory)):
        if Inventory[a][0] == item and Inventory[a][1] < 32:
            Inventory[a][1] += 1
            break
        if Inventory[a][0] == "":
            Inventory[a][0] = item
            Inventory[a][1] = 1
            break
#Create an item entity
def itementity(item, posx, posy):
    sprite = Entity(0, item, posx, posy, Settings["TileSize"] / 2, Settings["TileSize"] / 2)
    sprites_group_entity.add(sprite)
#Make an island structure
def structure_island(tile):
    global structure_depth
    structure_depth += 1
    if not "ground-dark_grass, ground-grass".__contains__(Grid[tile][4]):
        if Grid[tile][1] <= -0.33:
            Grid[tile][4] = "ground-dark_grass"
            if random.randrange(0, 100) <= 10:
                Grid[tile][5] = "object-dark_tree"
        else:
            Grid[tile][4] = "ground-grass"
            if random.randrange(0, 100) <= 10:
                if random.randrange(0, 100) <= 5:
                    Grid[tile][5] = "object-apple_tree"
                else:
                    Grid[tile][5] = "object-bright_tree"
    if tile > Settings["GridW"] and "ground-cold_water, ground-water, ground-warm_water".__contains__(Grid[tile - Settings["GridW"]][4]):
            Grid[tile - Settings["GridW"]][4] = "ground-sand"
            Grid[tile - Settings["GridW"]][5] = ""
    if tile > 0 and "ground-cold_water, ground-water, ground-warm_water".__contains__(Grid[tile - 1][4]):
        Grid[tile - 1][4] = "ground-sand"
        Grid[tile - 1][5] = ""
    if tile < len(Grid) - 1 and "ground-cold_water, ground-water, ground-warm_water".__contains__(Grid[tile + 1][4]):
        Grid[tile + 1][4] = "ground-sand"
        Grid[tile + 1][5] = ""
    if tile < len(Grid) - Settings["GridW"] and "ground-cold_water, ground-water, ground-warm_water".__contains__(Grid[tile + Settings["GridW"]][4]):
        Grid[tile + Settings["GridW"]][4] = "ground-sand"
        Grid[tile + Settings["GridW"]][5] = ""
    if structure_depth < 6:
        if tile > Settings["GridW"]  and random.randrange(0, 100) <= 75:
            structure_island(tile - Settings["GridW"])
        if tile > 0 and random.randrange(0, 100) <= 75:
            structure_island(tile - 1)
        if tile < len(Grid) - 1 and random.randrange(0, 100) <= 75:
            structure_island(tile + 1)
        if tile < len(Grid) - Settings["GridW"] and random.randrange(0, 100) <= 75:
            structure_island(tile + Settings["GridW"])
    structure_depth -= 1
#Make a lake structure
def structure_lake(tile):
    global structure_depth
    structure_depth += 1
    if Grid[tile][1] <= -0.33:
        Grid[tile][4] = "ground-cold_water"
    elif Grid[tile][1] >= -0.33 and Grid[tile][1] <= 0.33:
        Grid[tile][4] = "ground-water"
    elif Grid[tile][1] >= 0.33:
        Grid[tile][4] = "ground-warm_water"
    Grid[tile][5] = ""
    if tile > Settings["GridW"] and not "ground-cold_water, ground-water, ground-warm_water".__contains__(Grid[tile - Settings["GridW"]][4]):
        Grid[tile - Settings["GridW"]][4] = "ground-sand"
        Grid[tile - Settings["GridW"]][5] = ""
    if tile > 0 and not "ground-cold_water, ground-water, ground-warm_water".__contains__(Grid[tile - 1][4]):
        Grid[tile - 1][4] = "ground-sand"
        Grid[tile - 1][5] = ""
    if tile < len(Grid) - 1 and not "ground-cold_water, ground-water, ground-warm_water".__contains__(Grid[tile + 1][4]):
        Grid[tile + 1][4] = "ground-sand"
        Grid[tile + 1][5] = ""
    if tile < len(Grid) - Settings["GridW"] and not "ground-cold_water, ground-water, ground-warm_water".__contains__(Grid[tile + Settings["GridW"]][4]):
        Grid[tile + Settings["GridW"]][4] = "ground-sand"
        Grid[tile + Settings["GridW"]][5] = ""
    if structure_depth < 4:
        if tile > Settings["GridW"]  and random.randrange(0, 100) <= 75:
            structure_lake(tile - Settings["GridW"])
        if tile > 0 and random.randrange(0, 100) <= 75:
            structure_lake(tile - 1)
        if tile < len(Grid) - 1 and random.randrange(0, 100) <= 75:
            structure_lake(tile + 1)
        if tile < len(Grid) - Settings["GridW"] and random.randrange(0, 100) <= 75:
            structure_lake(tile + Settings["GridW"])
    structure_depth -= 1
#Draw the screen
def draw():
    screen.fill((  0,   0,   0))
    sprites_group_tile.draw(screen)
    for a in range(len(Grid)):
        if not Grid[a][5] == "":
            screen.blit(Images[Grid[a][5]], [(((a + 0.5) % Settings["GridW"] * Settings["TileSize"] - Settings["TileSize"] / 2) - VariablesNumber["camera_x"]) * VariablesNumber["camera_z"] + Config["ScreenX"] / 2, ((round((a - ((Settings["GridW"] - 1) / 2)) / Settings["GridW"]) * Settings["TileSize"]) - VariablesNumber["camera_y"]) * VariablesNumber["camera_z"] + Config["ScreenY"] / 2])
    sprites_group_entity.draw(screen)
    screen.blit(screen_effect_time, (0, 0))
    if VariablesBoolean["menu_debug"] and not VariablesBoolean["menu_inventory"]:
        pygame.draw.rect(screen, (  0,   0,   0), [5, 5, Config["ScreenX"] - 10, 210])
        font = pygame.font.SysFont("bahnschrift", 20)
        text = font.render(Config["ScreenCaption"], True, (255, 255, 255))
        screen.blit(text, [10, 10])
        text = font.render("Position (X, Y): " + str(round(VariablesNumber["player_posx"] * (Settings["GridW"] / Config["ScreenX"]) - 0.5, 1)) + ", " + str(round(VariablesNumber["player_posy"] * (Settings["GridH"] / Config["ScreenY"]) - 0.5, 1)), True, (255, 255, 255))
        screen.blit(text, [10, 40])
        text = font.render("Tile (#, X, Y): " + str(VariablesNumber["player_tile"]) + ", " + str(round(VariablesNumber["player_posx"] / Settings["TileSize"] - 0.5)) + ", " + str(round(VariablesNumber["player_posy"] / Settings["TileSize"] - 0.5)), True, (255, 255, 255))
        screen.blit(text, [10, 70])
        text = font.render("Tile Features (Biome, Ground, Object):", True, (255, 255, 255))
        screen.blit(text, [10, 100])
        if Grid[VariablesNumber["player_tile"]][5] == "":
            text = font.render(str(Grid[VariablesNumber["player_tile"]][3]) + ", " + str(Names[Grid[VariablesNumber["player_tile"]][4]]), True, (255, 255, 255))
        else:
            text = font.render(str(Grid[VariablesNumber["player_tile"]][3]) + ", " + str(Names[Grid[VariablesNumber["player_tile"]][4]]) + ", " + str(Names[Grid[VariablesNumber["player_tile"]][5]]), True, (255, 255, 255))
        screen.blit(text, [10, 130])
        text = font.render("Biome Info (Water, Temperature, Humidity): " + str(round(Grid[VariablesNumber["player_tile"]][0], 3)) + ", " + str(round(Grid[VariablesNumber["player_tile"]][1], 3)) + ", " + str(round(Grid[VariablesNumber["player_tile"]][2], 3)), True, (255, 255, 255))
        screen.blit(text, [10, 160])
        text = font.render("Time (%, #): " + str(round(VariablesNumber["time_day_percentage"], 1)) + ", " + str(VariablesNumber["time_seconds"] // VariablesNumber["time_day_length"]), True, (255, 255, 255))
        screen.blit(text, [10, 190])
    if VariablesBoolean["menu_inventory"]:
        screen_effect_inventory.fill((  0,   0,   0, 128))
    else:
        screen_effect_inventory.fill((  0,   0,   0,   0))
        pygame.draw.rect(screen_effect_inventory, (  0,   0,   0, 128), [0, Config["ScreenY"] - 97, Config["ScreenX"], 97])
    screen.blit(screen_effect_inventory, (0, 0))
    for i in range(32):
        a = i // 8
        b = i % 8
        if i >= 8 and not VariablesBoolean["menu_inventory"]:
            break
        if VariablesNumber["hotbar"] == i and not VariablesBoolean["menu_inventory"]:
            pygame.draw.rect(screen, (255, 255, 192), [InventoryMargins[i][0] - 8, InventoryMargins[i][1] - 8, 97, 97])
        pygame.draw.rect(screen, (192, 192, 192), [InventoryMargins[i][0], InventoryMargins[i][1], 81, 81])
        if not Inventory[i][0] == "":
            screen.blit(Images[Inventory[i][0].replace(".png", "")], [InventoryMargins[i][0], InventoryMargins[i][1]])
            font = pygame.font.SysFont("bahnschrift", 36)
            text = font.render(str(Inventory[i][1]), True, (  0,   0,   0))
            screen.blit(text, [InventoryMargins[i][0], InventoryMargins[i][1]])
    pygame.display.update()
def main():
    global screen
    global screen_effect_inventory
    global screen_effect_time
    clock = pygame.time.Clock()
    #Screen and screen effects
    screen = pygame.display.set_mode((Config["ScreenX"], Config["ScreenY"]))
    screen_effect_inventory = pygame.Surface((Config["ScreenX"], Config["ScreenY"]), pygame.SRCALPHA)
    screen_effect_time = pygame.Surface((Config["ScreenX"], Config["ScreenY"]))
    screen_effect_time.set_alpha(64)
    screen_effect_time.fill((255, 128,   0))
    pygame.display.set_caption(Config["ScreenCaption"])
    pygame.display.set_icon(Images["entity-u"])
    #Resize images
    for a in range(len(Images)):
        if "entity-item" in ImagesList[a]:
            scale = Settings["TileSize"] * VariablesNumber["camera_z"] * 0.75
        elif "item" in ImagesList[a]:
            scale = 81
        else:
            scale = Settings["TileSize"] * VariablesNumber["camera_z"]
        Images[ImagesList[a]] = pygame.transform.scale(Images[ImagesList[a]], (scale, scale))
    #Generate world
    for a in range(len(Grid)):
        tile_posx = (a + 0.5) % Settings["GridW"] * Settings["TileSize"]
        tile_posy = round((a - ((Settings["GridW"] - 1) / 2)) / Settings["GridW"]) * Settings["TileSize"] + Settings["TileSize"] / 2
        for b in range(3):
            point_da = 9999
            point_db = 9999
            points_half = int(Settings["Points"] / 2)
            #Calculate total distance to two points
            for c in range(points_half):
                point_d = math.sqrt(((tile_posx - Points[int(c + b * Settings["Points"])][2]) ** 2) + ((tile_posy - Points[int(c + b * Settings["Points"])][3]) ** 2))
                if point_d <= point_da:
                    point_da = point_d
            for c in range(points_half):
                point_d = math.sqrt(((tile_posx - Points[int(c + b * Settings["Points"] + points_half)][2]) ** 2) + ((tile_posy - Points[int(c + b * Settings["Points"] + points_half)][3]) ** 2))
                if point_d <= point_db:
                    point_db = point_d
            #Find percentage of distange to one of the two points
            Grid[a][b] = ((point_da / (point_da + point_db)) * -2 + 1)
        #Set the biome, ground and object for the tile
        if Grid[a][0] < -1 or Grid[a][0] > 1 and Grid[a][1] < -1 or Grid[a][1] > 1 and Grid[a][2] < -1 or Grid[a][2] > 1:
            Grid[a][4] = ("ground-dirt")
        elif Grid[a][0] <= 0.1:
            if Grid[a][1] <= -0.33:
                Grid[a][3] = "Cold Ocean"
                if random.randint(0, 100) <= Grid[a][1] * -400 - 300:
                    Grid[a][4] = "ground-ice"
                else:
                    Grid[a][4] = "ground-cold_water"
            elif Grid[a][1] >= -0.33 and Grid[a][1] <= 0.33:
                Grid[a][3] = "Ocean"
                Grid[a][4] = "ground-water"
            elif Grid[a][1] >= 0.33:
                Grid[a][3] = "Warm Ocean"
                Grid[a][4] = "ground-warm_water"
        elif Grid[a][0] >= 0.1 and Grid[a][0] <= 0.2:
            Grid[a][3] = "Beach"
            Grid[a][4] = "ground-sand"
        elif Grid[a][0] >= 0.2:
            if Grid[a][1] <= -0.33:
                if Grid[a][2] <= -0.33:
                    Grid[a][3] = "Snow Plains"
                    if random.randrange(0, 100) <= 10:
                        Grid[a][4] = "ground-ice"
                    else:
                        Grid[a][4] = "ground-snow"
                        if random.randrange(0, 100) <= 5:
                            Grid[a][5] = "object-dark_tree"
                elif Grid[a][2] >= -0.33 and Grid[a][2] <= 0.33:
                    Grid[a][3] = "Snow Forest"
                    Grid[a][4] = "ground-snow"
                    if random.randrange(0, 100) <= 25:
                        Grid[a][5] = "object-dark_tree"
                elif Grid[a][2] >= 0.33:
                    Grid[a][3] = "Taiga"
                    Grid[a][4] = "ground-dark_grass"
                    if random.randrange(0, 100) <= 25:
                        Grid[a][5] = "object-dark_tree"
            elif Grid[a][1] >= -0.33 and Grid[a][1] <= 0.33:
                if Grid[a][2] <= -0.33:
                    Grid[a][3] = "Plains"
                    Grid[a][4] = "ground-grass"
                    if random.randrange(0, 100) <= 5:
                        if random.randrange(0, 100) <= 5:
                            Grid[a][5] = "object-apple_tree"
                        else:
                            Grid[a][5] = "object-bright_tree"
                elif Grid[a][2] >= -0.33 and Grid[a][2] <= 0.33:
                    Grid[a][3] = "Forest"
                    Grid[a][4] = "ground-grass"
                    if random.randrange(0, 100) <= 25:
                        if random.randrange(0, 100) <= 5:
                            Grid[a][5] = "object-apple_tree"
                        else:
                            Grid[a][5] = "object-bright_tree"
                elif Grid[a][2] >= 0.33:
                    Grid[a][3] = "Swamp"
                    if random.randrange(0, 100) <= Grid[a][2] * 75 - 25:
                        Grid[a][4] = "ground-mud"
                    elif random.randrange(0, 100) <= 75:
                        Grid[a][4] = "ground-dark_grass"
                        if random.randrange(0, 100) <= 12.5:
                            Grid[a][5] = "object-dark_tree"
                    else:
                        Grid[a][4] = "ground-water"
            elif Grid[a][1] >= 0.33:
                if Grid[a][2] <= -0.33:
                    Grid[a][3] = "Desert"
                    Grid[a][4] = "ground-sand"
                    if random.randrange(0, 100) <= 5:
                        Grid[a][5] = "object-cactus"
                elif Grid[a][2] >= -0.33 and Grid[a][2] <= 0.33:
                    Grid[a][3] = "Savanna"
                    if random.randrange(0, 100) <= 25:
                        Grid[a][4] = "ground-sand"
                    else:
                        Grid[a][4] = "ground-grass"
                        if random.randrange(0, 100) <= 12.5:
                            if random.randrange(0, 100) <= 5:
                                Grid[a][5] = "object-apple_tree"
                            else:
                                Grid[a][5] = "object-bright_tree"
                elif Grid[a][2] >= 0.33:
                    Grid[a][3] = "Jungle"
                    if random.randrange(0, 100) <= Grid[a][2] * 120 - 30:
                        Grid[a][4] = "ground-warm_water"
                    else:
                        Grid[a][4] = "ground-grass"
                        if random.randrange(0, 100) <= 50:
                            if random.randrange(0, 100) <= 10:
                                Grid[a][5] = "object-apple_tree"
                            else:
                                Grid[a][5] = "object-bright_tree"
        else:
            Grid[a][4] = "ground-dirt"
        #Make the tile sprites
        sprite = Tile(a, (a + 0.5) % Settings["GridW"] * Settings["TileSize"], round((a - ((Settings["GridW"] - 1) / 2)) / Settings["GridW"]) * Settings["TileSize"] + Settings["TileSize"] / 2, Settings["TileSize"], Settings["TileSize"])
        sprites_group_tile.add(sprite)
    #Make islands
    for a in range(round(len(Grid) / 1600)):
        structure_tile = random.randint(0, len(Grid))
        if "ground-water, ground-warm_water".__contains__(Grid[structure_tile][4]) and Grid[structure_tile][0] <= 0.1 and Grid[structure_tile][1] >= -0.1:
            structure_island(structure_tile)
    #Make lakes
    for a in range(round(len(Grid) / 800)):
        structure_tile = random.randint(0, len(Grid))
        if not "ground-cold_water, ground-ice, ground-water, ground-warm_water".__contains__(Grid[structure_tile][4]):
            structure_lake(structure_tile)
    #Make caves
    for a in range(round(len(Grid) / 800)):
        structure_tile = random.randint(0, len(Grid))
        while not "ground-dark_grass, ground-grass, ground-snow".__contains__(Grid[structure_tile][4]):
            structure_tile = random.randint(0, len(Grid))
        if "ground-dark_grass, ground-grass, ground-snow".__contains__(Grid[structure_tile][4]):
            Grid[structure_tile][5] = "object-cave"
    #Make the player
    sprite = Entity(0, "entity-u", Config["ScreenX"] / 2, Config["ScreenY"] / 2, Settings["TileSize"], Settings["TileSize"])
    sprites_group_entity.add(sprite)
    while True:
        mousex, mousey = pygame.mouse.get_pos()
        for event in pygame.event.get():
            #Exit window
            if event.type == pygame.QUIT:
                sys.exit()
            #Check for key presses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if not VariablesBoolean["menu_inventory"]:
                        VariablesNumber["hotbar"] = 0
                if event.key == pygame.K_2:
                    if not VariablesBoolean["menu_inventory"]:
                        VariablesNumber["hotbar"] = 1
                if event.key == pygame.K_3:
                    if not VariablesBoolean["menu_inventory"]:
                        VariablesNumber["hotbar"] = 2
                if event.key == pygame.K_4:
                    if not VariablesBoolean["menu_inventory"]:
                        VariablesNumber["hotbar"] = 3
                if event.key == pygame.K_5:
                    if not VariablesBoolean["menu_inventory"]:
                        VariablesNumber["hotbar"] = 4
                if event.key == pygame.K_6:
                    if not VariablesBoolean["menu_inventory"]:
                        VariablesNumber["hotbar"] = 5
                if event.key == pygame.K_7:
                    if not VariablesBoolean["menu_inventory"]:
                        VariablesNumber["hotbar"] = 6
                if event.key == pygame.K_8:
                    if not VariablesBoolean["menu_inventory"]:
                        VariablesNumber["hotbar"] = 7
                if event.key == pygame.K_a:
                    Keys["A"] = True
                if event.key == pygame.K_d:
                    Keys["D"] = True
                #Open/Close inventory
                if event.key == pygame.K_e:
                    if VariablesBoolean["menu_inventory"]:
                        VariablesBoolean["menu_inventory"] = False
                    else:
                        VariablesBoolean["menu_inventory"] = True
                #Open/Close debug screen
                if event.key == pygame.K_q:
                    if VariablesBoolean["menu_debug"]:
                        VariablesBoolean["menu_debug"] = False
                    else:
                        VariablesBoolean["menu_debug"] = True
                if event.key == pygame.K_s:
                    Keys["S"] = True
                if event.key == pygame.K_w:
                    Keys["W"] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    Keys["A"] = False
                if event.key == pygame.K_d:
                    Keys["D"] = False
                if event.key == pygame.K_s:
                    Keys["S"] = False
                if event.key == pygame.K_w:
                    Keys["W"] = False
        #Set camera X and Y and change them if the player is near the edge of the world
        VariablesNumber["camera_x"] = VariablesNumber["player_posx"]
        if VariablesNumber["camera_x"] < Config["ScreenX"] / VariablesNumber["camera_z"] / 2:
            VariablesNumber["camera_x"] = Config["ScreenX"] / VariablesNumber["camera_z"] / 2
        if VariablesNumber["camera_x"] > Config["ScreenX"] - Config["ScreenX"] / VariablesNumber["camera_z"] / 2:
            VariablesNumber["camera_x"] = Config["ScreenX"] - Config["ScreenX"] / VariablesNumber["camera_z"] / 2
        VariablesNumber["camera_y"] = VariablesNumber["player_posy"]
        if VariablesNumber["camera_y"] < Config["ScreenY"] / VariablesNumber["camera_z"] / 2:
            VariablesNumber["camera_y"] = Config["ScreenY"] / VariablesNumber["camera_z"] / 2
        if VariablesNumber["camera_y"] > Config["ScreenY"] - Config["ScreenY"] / VariablesNumber["camera_z"] / 2:
            VariablesNumber["camera_y"] = Config["ScreenY"] - Config["ScreenY"] / VariablesNumber["camera_z"] / 2
        sprites_group_entity.update()
        sprites_group_tile.update()
        #Set time and change time lighting
        VariablesNumber["time_frames"] += 1
        VariablesNumber["time_seconds"] = VariablesNumber["time_frames"] / Config["Framerate"]
        VariablesNumber["time_day_percentage"] = (100 / VariablesNumber["time_day_length"]) * (VariablesNumber["time_seconds"] % VariablesNumber["time_day_length"])
        if VariablesNumber["time_day_percentage"] <= 12.5:
            screen_effect_time.set_alpha(VariablesNumber["time_day_percentage"] * (-128 / 25) + 64)
            screen_effect_time.fill((255, 128,   0))
        elif VariablesNumber["time_day_percentage"] >= 12.5 and VariablesNumber["time_day_percentage"] <= 37.5:
            screen_effect_time.set_alpha(0)
            screen_effect_time.fill((255, 128,   0))
        elif VariablesNumber["time_day_percentage"] >= 37.5 and VariablesNumber["time_day_percentage"] <= 50:
            screen_effect_time.set_alpha(VariablesNumber["time_day_percentage"] * (128 / 25) - 192)
            screen_effect_time.fill((255, 128,   0))
        elif VariablesNumber["time_day_percentage"] >= 50 and VariablesNumber["time_day_percentage"] <= 62.5:
            screen_effect_time.set_alpha(VariablesNumber["time_day_percentage"] * (128 / 25) - 192)
            screen_effect_time.fill((VariablesNumber["time_day_percentage"] * (-512 / 25) + 1280, VariablesNumber["time_day_percentage"] * (-256 / 25) + 640, VariablesNumber["time_day_percentage"] * (256 / 25) - 512))
        elif VariablesNumber["time_day_percentage"] >= 62.5 and VariablesNumber["time_day_percentage"] <= 87.5:
            screen_effect_time.set_alpha(128)
            screen_effect_time.fill((  0,   0, 128))
        elif VariablesNumber["time_day_percentage"] >= 87.5:
            screen_effect_time.set_alpha(VariablesNumber["time_day_percentage"] * (-128 / 25) + 576)
            screen_effect_time.fill((VariablesNumber["time_day_percentage"] * (512 / 25) - 1792, VariablesNumber["time_day_percentage"] * (256 / 25) - 896, VariablesNumber["time_day_percentage"] * (-256 / 25) + 1024))
        draw()
        clock.tick(Config["Framerate"])
if __name__ == "__main__":
    main()
