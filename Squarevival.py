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
    #Entity images
    "entity-fake_stone"             : pygame.image.load("Images/squarevival-entity-fake_stone.png"             ),
    "enitty-fish-red"               : pygame.image.load("Images/squarevival-entity-fish-red.png"               ),
    "entity-fish-teal"              : pygame.image.load("Images/squarevival-entity-fish-teal.png"              ),
    "entity-item-apple"             : pygame.image.load("Images/squarevival-entity-item-apple.png"             ),
    "entity-item-bright_wood"       : pygame.image.load("Images/squarevival-entity-item-bright_wood.png"       ),
    "entity-item-cactus_spike"      : pygame.image.load("Images/squarevival-entity-item-cactus_spike.png"      ),
    "entity-item-coal"              : pygame.image.load("Images/squarevival-entity-item-coal.png"              ),
    "entity-item-dark_grass_seed"   : pygame.image.load("Images/squarevival-entity-item-dark_grass_seed.png"   ),
    "entity-item-dark_wood"         : pygame.image.load("Images/squarevival-entity-item-dark_wood.png"         ),
    "entity-item-diamond"           : pygame.image.load("Images/squarevival-entity-item-diamond.png"           ),
    "entity-item-grass_seed"        : pygame.image.load("Images/squarevival-entity-item-grass_seed.png"        ),
    "entity-item-ice"               : pygame.image.load("Images/squarevival-entity-item-ice.png"               ),
    "entity-item-iron_bar"          : pygame.image.load("Images/squarevival-entity-item-iron_bar.png"          ),
    "entity-item-leaf"              : pygame.image.load("Images/squarevival-entity-item-leaf.png"              ),
    "entity-item-mud"               : pygame.image.load("Images/squarevival-entity-item-mud.png"               ),
    "entity-item-sand"              : pygame.image.load("Images/squarevival-entity-item-sand.png"              ),
    "entity-item-snow"              : pygame.image.load("Images/squarevival-entity-item-snow.png"              ),
    "entity-sheep"                  : pygame.image.load("Images/squarevival-entity-sheep.png"                  ),
    "entity-spider"                 : pygame.image.load("Images/squarevival-entity-spider.png"                 ),
    "entity-u"                      : pygame.image.load("Images/squarevival-entity-u.png"                      ),
    "entity-villager"               : pygame.image.load("Images/squarevival-entity-villager.png"               ),
    "entity-wolf"                   : pygame.image.load("Images/squarevival-entity-wolf.png"                   ),
    #Ground images
    "ground-bright_wood_floor"      : pygame.image.load("Images/squarevival-ground-bright_wood_floor.png"      ),
    "ground-cold_water"             : pygame.image.load("Images/squarevival-ground-cold_water.png"             ),
    "ground-dark_grass"             : pygame.image.load("Images/squarevival-ground-dark_grass.png"             ),
    "ground-dark_wood_floor"        : pygame.image.load("Images/squarevival-ground-dark_wood_floor.png"        ),
    "ground-dirt"                   : pygame.image.load("Images/squarevival-ground-dirt.png"                   ),
    "ground-grass"                  : pygame.image.load("Images/squarevival-ground-grass.png"                  ),
    "ground-ice"                    : pygame.image.load("Images/squarevival-ground-ice.png"                    ),
    "ground-lava"                   : pygame.image.load("Images/squarevival-ground-lava.png"                   ),
    "ground-mud"                    : pygame.image.load("Images/squarevival-ground-mud.png"                    ),
    "ground-sand"                   : pygame.image.load("Images/squarevival-ground-sand.png"                   ),
    "ground-sand_bricks_ground"     : pygame.image.load("Images/squarevival-ground-sand_bricks_ground.png"     ),
    "ground-snow"                   : pygame.image.load("Images/squarevival-ground-snow.png"                   ),
    "ground-stone_bricks_ground"    : pygame.image.load("Images/squarevival-ground-stone_bricks_ground.png"    ),
    "ground-stone_ground"           : pygame.image.load("Images/squarevival-ground-stone_ground.png"           ),
    "ground-warm_water"             : pygame.image.load("Images/squarevival-ground-warm_water.png"             ),
    "ground-water"                  : pygame.image.load("Images/squarevival-ground-water.png"                  ),
    #Item images
    "item-apple"                    : pygame.image.load("Images/squarevival-item-apple.png"                    ),
    "item-bright_wood"              : pygame.image.load("Images/squarevival-item-bright_wood.png"              ),
    "item-cactus_spike"             : pygame.image.load("Images/squarevival-item-cactus_spike.png"             ),
    "item-coal"                     : pygame.image.load("Images/squarevival-item-coal.png"                     ),
    "item-dark_grass_seed"          : pygame.image.load("Images/squarevival-item-dark_grass_seed.png"          ),
    "item-dark_wood"                : pygame.image.load("Images/squarevival-item-dark_wood.png"                ),
    "item-diamond"                  : pygame.image.load("Images/squarevival-item-diamond.png"                  ),
    "item-grass_seed"               : pygame.image.load("Images/squarevival-item-grass_seed.png"               ),
    "item-ice"                      : pygame.image.load("Images/squarevival-item-ice.png"                      ),
    "item-iron_bar"                 : pygame.image.load("Images/squarevival-item-iron_bar.png"                 ),
    "item-leaf"                     : pygame.image.load("Images/squarevival-item-leaf.png"                     ),
    "item-mud"                      : pygame.image.load("Images/squarevival-item-mud.png"                      ),
    "item-sand"                     : pygame.image.load("Images/squarevival-item-sand.png"                     ),
    "item-snow"                     : pygame.image.load("Images/squarevival-item-snow.png"                     ),
    #Object images
    "object-apple_tree"             : pygame.image.load("Images/squarevival-object-apple_tree.png"             ),
    "object-bright_tree"            : pygame.image.load("Images/squarevival-object-bright_tree.png"            ),
    "object-bright_wood"            : pygame.image.load("Images/squarevival-object-bright_wood.png"            ),
    "object-bright_wood_box"        : pygame.image.load("Images/squarevival-object-bright_wood_box.png"        ),
    "object-bright_wood_door-closed": pygame.image.load("Images/squarevival-object-bright_wood_door-closed.png"),
    "object-bright_wood_door-open"  : pygame.image.load("Images/squarevival-object-bright_wood_door-open.png"  ),
    "object-cactus"                 : pygame.image.load("Images/squarevival-object-cactus.png"                 ),
    "object-cave"                   : pygame.image.load("Images/squarevival-object-cave.png"                   ),
    "object-christmas_tree"         : pygame.image.load("Images/squarevival-object-christmas_tree.png"         ),
    "object-coal_ore"               : pygame.image.load("Images/squarevival-object-coal_ore.png"               ),
    "object-dark_tree"              : pygame.image.load("Images/squarevival-object-dark_tree.png"              ),
    "object-dark_wood"              : pygame.image.load("Images/squarevival-object-dark_wood.png"              ),
    "object-dark_wood_box"          : pygame.image.load("Images/squarevival-object-dark_wood_box.png"          ),
    "object-dark_wood_door-closed"  : pygame.image.load("Images/squarevival-object-dark_wood_door-closed.png"  ),
    "object-dark_wood_door-open"    : pygame.image.load("Images/squarevival-object-dark_wood_door-open.png"    ),
    "object-diamond_ore"            : pygame.image.load("Images/squarevival-object-diamond_ore.png"            ),
    "object-iron_ore"               : pygame.image.load("Images/squarevival-object-iron_ore.png"               ),
    "object-sand_bricks"            : pygame.image.load("Images/squarevival-object-sand_bricks.png"            ),
    "object-stone"                  : pygame.image.load("Images/squarevival-object-stone.png"                  ),
    "object-stone_bricks"           : pygame.image.load("Images/squarevival-object-stone_bricks.png"           ),
    #User interface images
    "ui-menu"                       : pygame.image.load("Images/squarevival-ui-menu.png"                       ),
}
#Cooldown time lengths
Cooldowns_Length = {
    "cooldown-cactus": 0.5,
    "cooldown-entity": 0.1,
    "cooldown-health": 1,
}
Cooldowns_Time = {
    "cooldown-cactus": 0,
    "cooldown-entity": 0,
    "cooldown-health": 0,
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
    ""                              : ""                   ,
    #Entity names
    "entity-fake_stone"             : "Fake Stone"         ,
    "enitty-fish-red"               : "Fish"               ,
    "entity-fish-teal"              : "Fish"               ,
    "entity-item-apple"             : "Apple"              ,
    "entity-item-bright_wood"       : "Bright Wood"        ,
    "entity-item-cactus_spike"      : "Cactus Spike"       ,
    "entity-item-coal"              : "Coal"               ,
    "entity-item-dark_grass_seed"   : "Dark Grass Seed"    ,
    "entity-item-dark_wood"         : "Dark Wood"          ,
    "entity-item-diamond"           : "Diamond"            ,
    "entity-item-grass_seed"        : "Grass Seed"         ,
    "entity-item-ice"               : "Ice"                ,
    "entity-item-iron_bar"          : "Iron Bar"           ,
    "entity-item-leaf"              : "Leaf"               ,
    "entity-item-mud"               : "Mud"                ,
    "entity-item-sand"              : "Sand"               ,
    "entity-item-snow"              : "Snow"               ,
    "entity-sheep"                  : "Sheep"              ,
    "entity-spider"                 : "Spider"             ,
    "entity-u"                      : "U"                  ,
    "entity-villager"               : "Villager"           ,
    "entity-wolf"                   : "Wolf"               ,
    #Ground names
    "ground-bright_wood_floor"      : "Bright Wood Floor"  ,
    "ground-cold_water"             : "Cold Water"         ,
    "ground-dark_grass"             : "Dark Grass"         ,
    "ground-dark_wood_floor"        : "Dark Wood Floor"    ,
    "ground-dirt"                   : "Dirt"               ,
    "ground-grass"                  : "Grass"              ,
    "ground-ice"                    : "Ice"                ,
    "ground-lava"                   : "Lava"               ,
    "ground-mud"                    : "Mud"                ,
    "ground-sand"                   : "Sand"               ,
    "ground-sand_bricks_ground"     : "Sand Bricks Ground" ,
    "ground-snow"                   : "Snow"               ,
    "ground-stone_bricks_ground"    : "Stone Bricks Ground",
    "ground-stone_ground"           : "Stone Ground"       ,
    "ground-warm_water"             : "Warm Water"         ,
    "ground-water"                  : "Water"              ,
    #Item names
    "item-apple"                    : "Apple"              ,
    "item-bright_wood"              : "Bright Wood"        ,
    "item-cactus_spike"             : "Cactus Spike"       ,
    "item-coal"                     : "Coal"               ,
    "item-dark_grass_seed"          : "Dark Grass Seed"    ,
    "item-dark_wood"                : "Dark Wood"          ,
    "item-diamond"                  : "Diamond"            ,
    "item-grass_seed"               : "Grass Seed"         ,
    "item-ice"                      : "Ice"                ,
    "item-iron_bar"                 : "Iron Bar"           ,
    "item-leaf"                     : "Leaf"               ,
    "item-mud"                      : "Mud"                , 
    "item-sand"                     : "Sand"               ,
    "item-snow"                     : "Snow"               ,
    #Object names
    "object-apple_tree"             : "Apple Tree"         ,
    "object-bright_tree"            : "Bright Tree"        ,
    "object-bright_wood"            : "Bright Wood"        ,
    "object-bright_wood_box"        : "Bright Wood Box"    ,
    "object-bright_wood_door-closed": "Bright Wood Door"   ,
    "object-bright_wood_door-open"  : "Bright wood Door"   ,
    "object-cactus"                 : "Cactus"             ,
    "object-cave"                   : "Cave"               ,
    "object-christmas_tree"         : "Christmas Tree"     ,
    "object-coal_ore"               : "Coal Ore"           ,
    "object-dark_tree"              : "Dark Tree"          ,
    "object-dark_wood"              : "Dark Wood"          ,
    "object-dark_wood_box"          : "Dark Wood Box"      ,
    "object-dark_wood_door-closed"  : "Dark Wood Door"     ,
    "object-dark_wood_door-open"    : "Dark Wood Door"     ,
    "object-diamond_ore"            : "Diamond Ore"        ,
    "object-iron_ore"               : "Iron Ore"           ,
    "object-sand_bricks"            : "Sand Bricks"        ,
    "object-stone"                  : "Stone"              ,
    "object-stone_bricks"           : "Stone Bricks"       ,
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
    #Ground speeds
    "ground-bright_wood_floor"  : 1,
    "ground-cold_water"         : 0.4,
    "ground-dark_grass"         : 1,
    "ground-dark_wood_floor"    : 1,
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
    #Object speeds
    "object-apple_tree"         : 1,
    "object-bright_tree"        : 1,
    "object-bright_wood"        : 1,
    "object-bright_wood_box"    : 1,
    "object-bright_wood_door"   : 1,
    "object-cactus"             : 0.5,
    "object-cave"               : 1,
    "object-christmas_tree"     : 1,
    "object-coal_ore"           : 1,
    "object-dark_tree"          : 1,
    "object-dark_wood"          : 1,
    "object-dark_wood_box"      : 1,
    "object-dark_wood_door"     : 1,
    "object-diamond_ore"        : 1,
    "object-iron_ore"           : 1,
    "object-sand_bricks"        : 1,
    "object-stone"              : 1,
    "object-stone_bricks"       : 1,
}
#Number variables
Variables = {
    #Camera's horizontal and vertical position
    "camera_x"           : 0,
    "camera_y"           : 0,
    #How zoomed in the camera is
    "camera_z"           : Settings["GridW"] / 18,
    #Whether the player is in a world or not
    "game"               : False,
    #Whether the player is in a world unpaused or not
    "game_running"       : False,
    #Player's health points
    "health"             : 100,
    #Hotbar item selected
    "hotbar"             : 0,
    #Player's hunger points
    "hunger"             : 100,
    #Keys being pressed
    "key_a"              : False,
    "key_d"              : False,
    "key_s"              : False,
    "key_w"              : False,
    #Menus being shown
    "menu_debug"         : False,
    "menu_inventory"     : False,
    "menu_pause"         : False,
    "menu_settings"      : False,
    #Page numbers (0: Main menu, 1: World list, 2: World creation, 3: Credits, 4: Game)
    "page"               : 0,
    #Player horizontal and vertical position
    "player_posx"        : 0,
    "player_posy"        : 0,
    #Tile the player is standing on
    "player_tile"        : 0,
    "player_tileposx"    : 0,
    "player_tileposy"    : 0,
    #Player's moving speed
    "player_vel"         : 0,
    #Variable used for keeping track of the size of a structure
    "structure_depth"    : 0,
    #Tile's horizontal and vertical position
    "tile_posx"          : 0,
    "tile_posy"          : 0,
    #Length of a full day/night cycle (5 minutes)
    "time_day_length"    : 300,
    #Percentage through the full day/night cycle
    "time_day_percentage": 0,
    #Time since the code started running in frames and seconds
    "time_frames"        : 0,
    "time_seconds"       : 0,
}

#LISTS
#Tile list
#Grid[?][0]: Water level
#Grid[?][1]: Temperature
#Grid[?][2]: Humidity
#Grid[?][3]: Biome
#Grid[?][4]: Ground
#Grid[?][5]: Object
Grid = [[0, 0, 0, "Ocean", "ground-water", ""] for i in range(Settings["GridW"] * Settings["GridH"])]
#Images list
ImagesList = [i for i in Images]
#Inventory
Inventory = [["", 0] for i in range(32)]
#Inventory margins
InventoryMargins =  [[(i % 8) * 89 + 8, (i // 8) * -89 + Config["ScreenY"] - 89] for i in range(32)]
#Item being dragged in the inventory
Item_Dragging = ["", 0]
Item_Swap = ["", 0]
#Objects you can't walk through
ObjectsSolid = [
    "object-apple_tree"             ,
    "object-bright_tree"            ,
    "object-bright_wood"            ,
    "object-cave"                   ,
    "object-christmas_tree"         ,
    "object-coal_ore"               ,
    "object-dark_tree"              ,
    "object-dark_wood"              ,
    "object-diamond_ore"            ,
    "object-iron_ore"               ,
    "object-sand_bricks"            ,
    "object-stone"                  ,
    "object-stone_bricks"           ,
]
#World terrain points
Points = [[a, 1, random.randrange(0, Config["ScreenX"]), random.randrange(0, Config["ScreenY"])] for a in range(3) for b in range(int(Settings["Points"] / 2))] + [[a, -1, random.randrange(0, Config["ScreenX"]), random.randrange(0, Config["ScreenY"])] for a in range(3) for b in range(int(Settings["Points"] / 2))]
#Colors for lighting
Time_Colors = [[0, 0, 0, 0] for i in range(200)]
for i in range(len(Time_Colors)):
    percentage = i / (len(Time_Colors) / 100)
    if percentage <= 12.5:
        Time_Colors[i] = [255, 128, 0, percentage * (-128 / 25) + 64]
    elif percentage <= 37.5:
        Time_Colors[i] = [255, 128, 0, 0]
    elif percentage <= 50:
        Time_Colors[i] = [255, 128, 0, percentage * (128 / 25) - 192]
    elif percentage <= 62.5:
        Time_Colors[i] = [percentage * (-512 / 25) + 1280, percentage * (-256 / 25) + 640, percentage * (256 / 25) - 512, percentage * (128 / 25) - 192]
    elif percentage <= 87.5:
        Time_Colors[i] = [0, 0, 128, 128]
    else:
        Time_Colors[i] = [percentage * (512 / 25) - 1792, percentage * (256 / 25) - 896, percentage * (-256 / 25) + 1024, percentage * (-128 / 25) + 576]

#VARIABLES
structure_depth, sprites_group_entity, sprites_group_tile, sprites_group_ui_main, sprites_group_ui_pause = 0, pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()

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
        self.rect.center = ((self.posx - Variables["camera_x"]) * Variables["camera_z"] + Config["ScreenX"] / 2, (self.posy - Variables["camera_y"]) * Variables["camera_z"] + Config["ScreenY"] / 2)
    def update(self):
        if self.type.__contains__("entity-item"):
            #Collect items
            if math.sqrt((self.posx - Variables["player_posx"]) ** 2 + (self.posy - Variables["player_posy"]) ** 2) <= Settings["TileSize"]:
                item(self.type.replace("entity-", ""))
                self.kill()
        elif self.type == "entity-u":
            #Set player speed
            Variables["player_vel"] = (Settings["TileSize"] / 8) * Speeds[Grid[Variables["player_tile"]][4]] * Speeds[Grid[Variables["player_tile"]][5]]
            #Move player if the inventory is closed and in the opposite direction if the player walks into an object
            if not Variables["menu_inventory"]:
                if Keys["A"]:
                    self.posx -= Variables["player_vel"]
                    if Variables["player_tileposx"] % 1 > 0.5 and ObjectsSolid.__contains__(Grid[Variables["player_tile"] - 1][5]):
                        self.posx += Variables["player_vel"]
                if Keys["D"]:
                    self.posx += Variables["player_vel"]
                    if Variables["player_tileposx"] % 1 < 0.5 and ObjectsSolid.__contains__(Grid[Variables["player_tile"] + 1][5]):
                        self.posx -= Variables["player_vel"]
                if Keys["S"]:
                    self.posy += Variables["player_vel"]
                    if Variables["player_tileposy"] % 1 < 0.5 and ObjectsSolid.__contains__(Grid[Variables["player_tile"] + Settings["GridW"]][5]):
                        self.posy -= Variables["player_vel"]
                if Keys["W"]:
                    self.posy -= Variables["player_vel"]
                    if Variables["player_tileposy"] % 1 > 0.5 and ObjectsSolid.__contains__(Grid[Variables["player_tile"] - Settings["GridW"]][5]):
                        self.posy += Variables["player_vel"]
            Variables["player_tileposx"] = self.posx * (Settings["GridW"] / Config["ScreenX"]) - 0.5
            Variables["player_tileposy"] = self.posy * (Settings["GridH"] / Config["ScreenY"]) - 0.5
            #Keep player away from the edge of the world
            if Variables["player_tileposx"] <= 0:
                self.posx = 4
            elif Variables["player_tileposx"] >= Settings["GridW"] - 1:
                self.posx = Config["ScreenX"] - 4
            if Variables["player_tileposy"] <= 0:
                self.posy = 4
            elif Variables["player_tileposy"] >= Settings["GridH"] - 1:
                self.posy = Config["ScreenY"] - 4
            Variables["player_posx"] = self.posx
            Variables["player_posy"] = self.posy
            self.tile = round(self.posx / Settings["TileSize"] - 0.5) + round(self.posy / Settings["TileSize"] - 0.5) * Settings["GridH"]
            Variables["player_tile"] = self.tile
        self.rect.center = ((self.posx - Variables["camera_x"]) * Variables["camera_z"] + Config["ScreenX"] / 2, (self.posy - Variables["camera_y"]) * Variables["camera_z"] + Config["ScreenY"] / 2)
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
        self.rect.center = ((self.posx - Variables["camera_x"]) * Variables["camera_z"] + Config["ScreenX"] / 2, (self.posy - Variables["camera_y"]) * Variables["camera_z"] + Config["ScreenY"] / 2)
    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            #Destroying objects/tiles
            if pygame.mouse.get_pressed()[0] == 1 and not Variables["menu_inventory"]:
                if not Grid[self.id][4] in "ground-cold_water, ground-dirt, ground-stone_ground, ground-warm_water, ground-water":
                    if Grid[self.id][4] == "ground-dark_grass":
                        if random.randrange(0, 100) <= 10:
                            itementity("entity-item-dark_grass_seed", self.posx, self.posy)
                    if Grid[self.id][4] == "ground-grass":
                        if random.randrange(0, 100) <= 10:
                            itementity("entity-item-grass_seed", self.posx, self.posy)
                    if Grid[self.id][4] == "ground-ice":
                        itementity("entity-item-ice", self.posx, self.posy)
                    if Grid[self.id][4] == "ground-mud":
                        itementity("entity-item-mud", self.posx, self.posy)
                    if Grid[self.id][4] == "ground-sand":
                        itementity("entity-item-sand", self.posx, self.posy)
                    if Grid[self.id][4] == "ground-snow":
                        itementity("entity-item-snow", self.posx, self.posy)
                    Grid[self.id][4] = "ground-dirt"
                if not "object-cave".__contains__(Grid[self.id][5]):
                    if Grid[self.id][5] == "object-apple_tree":
                        itementity("entity-item-bright_wood", self.posx, self.posy)
                        if random.randrange(0, 100) <= 50:
                            itementity("entity-item-apple", self.posx, self.posy)
                    elif Grid[self.id][5] == "object-bright_tree":
                        itementity("entity-item-bright_wood", self.posx, self.posy)
                        if random.randrange(0, 100) <= 50:
                            itementity("entity-item-bright_wood", self.posx, self.posy)
                    elif Grid[self.id][5] == "object-bright_wood":
                        itementity("entity-item-bright_wood", self.posx, self.posy)
                    elif Grid[self.id][5] == "object-cactus":
                        if random.randrange(0, 100) <= 25:
                            itementity("entity-item-cactus_spike", self.posx, self.posy)
                    elif Grid[self.id][5] == "object-coal_ore":
                        itementity("entity-item-coal", self.posx, self.posy)
                        if random.randrange(0, 100) <= 20:
                            itementity("entity-item-coal", self.posx, self.posy)
                    elif Grid[self.id][5] == "object-dark_tree":
                        itementity("entity-item-dark_wood", self.posx, self.posy)
                        if random.randrange(0, 100) <= 50:
                            itementity("entity-item-dark_wood", self.posx, self.posy)
                    elif Grid[self.id][5] == "object-dark_wood":
                        itementity("entity-item-dark_wood", self.posx, self.posy)
                    elif Grid[self.id][5] == "object-diamond_ore":
                        itementity("entity-item-diamond", self.posx, self.posy)
                    elif Grid[self.id][5] == "object-iron_ore":
                        itementity("entity-item-iron_bar", self.posx, self.posy)
                        if random.randrange(0, 100) <= 10:
                            itementity("entity-item-iron_bar", self.posx, self.posy)
                    Grid[self.id][5] = ""
            #Placing items
            if pygame.mouse.get_pressed()[2] == 1 and Grid[self.id][5] == "" or Grid[self.id][5] == "object-cave" and not Variables["menu_inventory"]:
                if Inventory[Variables["hotbar"]][0] == "item-bright_wood":
                    Grid[self.id][5] = "object-bright_wood"
                    itemremove(Variables["hotbar"])
                if Inventory[Variables["hotbar"]][0] == "item-dark_grass_seed" and Grid[self.id][4] == "ground-dirt":
                    Grid[self.id][4] = "ground-dark_grass"
                    itemremove(Variables["hotbar"])
                if Inventory[Variables["hotbar"]][0] == "item-dark_wood":
                    Grid[self.id][5] = "object-dark_wood"
                    itemremove(Variables["hotbar"])
                if Inventory[Variables["hotbar"]][0] == "item-grass_seed" and Grid[self.id][4] == "ground-dirt":
                    Grid[self.id][4] = "ground-grass"
                    itemremove(Variables["hotbar"])
                if Inventory[Variables["hotbar"]][0] == "item-ice" and Grid[self.id][4] in "ground-cold_water ground-dark_grass, ground-dirt, ground-grass, ground-warm_water, ground-water":
                    Grid[self.id][4] = "ground-ice"
                    itemremove(Variables["hotbar"])
                if Inventory[Variables["hotbar"]][0] == "item-mud" and Grid[self.id][4] in "ground-cold_water ground-dark_grass, ground-dirt, ground-grass, ground-warm_water, ground-water":
                    Grid[self.id][4] = "ground-mud"
                    itemremove(Variables["hotbar"])
                if Inventory[Variables["hotbar"]][0] == "item-sand" and Grid[self.id][4] in "ground-cold_water ground-dark_grass, ground-dirt, ground-grass, ground-warm_water, ground-water":
                    Grid[self.id][4] = "ground-sand"
                    itemremove(Variables["hotbar"])
                if Inventory[Variables["hotbar"]][0] == "item-snow" and Grid[self.id][4] in "ground-cold_water ground-dark_grass, ground-dirt, ground-grass, ground-warm_water, ground-water":
                    Grid[self.id][4] = "ground-snow"
                    itemremove(Variables["hotbar"])
        if not Grid[self.id][4] == "":
            self.image = Images[Grid[self.id][4]]
        self.rect.center = ((self.posx - Variables["camera_x"]) * Variables["camera_z"] + Config["ScreenX"] / 2, (self.posy - Variables["camera_y"]) * Variables["camera_z"] + Config["ScreenY"] / 2)
#User interface buttons
class UI_Button(pygame.sprite.Sprite):
    def __init__(self, identity, pos_x, pos_y, size_x, size_y, color, text_color, text_font, text_size, text):
        pygame.sprite.Sprite.__init__(self)
        self.identity = identity
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y
        self.text_style = pygame.font.SysFont(text_font, text_size)
        self.text = self.text_style.render(text, 1, text_color)
        self.image = pygame.Surface((self.size_x, self.size_y))
        self.image.fill(color)
        self.image.blit(self.text, self.text.get_rect(center=(self.size_x / 2, self.size_y / 2)))
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos_x, self.pos_y)
    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == 1:
                if self.identity == 0 and Variables["page"] == 0:
                    Variables["page"] = 4
                    Variables["game"] = True
                    Variables["game_running"] = True
                elif self.identity == 1:
                    Variables["menu_settings"] = True
                elif self.identity == 2:
                    Variables["page"] = 3
                elif self.identity == 3:
                    Variables["menu_settings"] = True
                elif self.identity == 4:
                    Variables["game_running"] = True
                    Variables["menu_pause"] = False
                elif self.identity == 6:
                    Variables["page"] = 0
                    Variables["game"] = False
                    Variables["menu_pause"] = False
        self.rect.center = (self.pos_x, self.pos_y)

#FUNCTIONS
def find_item_from_pos(x, y):
    return int((x / (Config["ScreenX"] / 8)) // 1 + ((y * -1 + Config["ScreenY"]) / (Config["ScreenY"] / 8)) // 1 * 8)
#Find the X and Y position when given the tile #
def find_pos_from_tile(tile):
    Variables["tile_posx"] = (((tile + 0.5) % Settings["GridW"] * Settings["TileSize"] - Settings["TileSize"] / 2) - Variables["camera_x"]) * Variables["camera_z"] + Config["ScreenX"] / 2
    Variables["tile_posy"] = ((round((tile - ((Settings["GridW"] - 1) / 2)) / Settings["GridW"]) * Settings["TileSize"]) - Variables["camera_y"]) * Variables["camera_z"] + Config["ScreenY"] / 2
#Find the tile # when given the X and Y position
def find_tile_from_pos(x, y):
    pass
#Add an item to the inventory
def item(item):
    item_added = False
    for i in range(len(Inventory)):
        if Inventory[i][0] == item and Inventory[i][1] < 32:
            Inventory[i][1] += 1
            item_added = True
            break
    if not item_added:
        for i in range(len(Inventory)):
            if Inventory[i][0] == "":
                Inventory[i][0] = item
                Inventory[i][1] = 1
                break
#Create an item entity
def itementity(item, posx, posy):
    sprite = Entity(0, item, posx + random.randrange(-4, 4) * Settings["TileSize"] / 16, posy + random.randrange(-4, 4) * Settings["TileSize"] / 16, Settings["TileSize"] / 2, Settings["TileSize"] / 2)
    sprites_group_entity.add(sprite)
#Remove an item from the inventory
def itemremove(item_number):
    Inventory[item_number][1] -= 1
    if Inventory[item_number][1] == 0:
        Inventory[item_number][0] = ""
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
    if tile > Settings["GridW"] and "ground-cold_water, ground-warm_water, ground-water".__contains__(Grid[tile - Settings["GridW"]][4]):
            Grid[tile - Settings["GridW"]][4] = "ground-sand"
            Grid[tile - Settings["GridW"]][5] = ""
    if tile > 0 and "ground-cold_water, ground-warm_water, ground-water".__contains__(Grid[tile - 1][4]):
        Grid[tile - 1][4] = "ground-sand"
        Grid[tile - 1][5] = ""
    if tile < len(Grid) - 1 and "ground-cold_water, ground-warm_water, ground-water".__contains__(Grid[tile + 1][4]):
        Grid[tile + 1][4] = "ground-sand"
        Grid[tile + 1][5] = ""
    if tile < len(Grid) - Settings["GridW"] and "ground-cold_water, ground-warm_water, ground-water".__contains__(Grid[tile + Settings["GridW"]][4]):
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
    if tile > Settings["GridW"] and not "ground-cold_water, ground-warm_water, ground-water".__contains__(Grid[tile - Settings["GridW"]][4]):
        Grid[tile - Settings["GridW"]][4] = "ground-sand"
        Grid[tile - Settings["GridW"]][5] = ""
    if tile > 0 and not "ground-cold_water, ground-warm_water, ground-water".__contains__(Grid[tile - 1][4]):
        Grid[tile - 1][4] = "ground-sand"
        Grid[tile - 1][5] = ""
    if tile < len(Grid) - 1 and not "ground-cold_water, ground-warm_water, ground-water".__contains__(Grid[tile + 1][4]):
        Grid[tile + 1][4] = "ground-sand"
        Grid[tile + 1][5] = ""
    if tile < len(Grid) - Settings["GridW"] and not "ground-cold_water, ground-warm_water, ground-water".__contains__(Grid[tile + Settings["GridW"]][4]):
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
    if Variables["menu_settings"]:
        screen.fill((  0, 187,   0))
        font = pygame.font.SysFont("bahnschrift", 75)
        text = font.render("Settings", True, (255, 255, 255))
        text_rect = text.get_rect(center=(Config["ScreenX"] / 2, 50))
        screen.blit(text, text_rect)
    elif Variables["page"] == 0:
        screen.fill((  0, 255, 102))
        screen.blit(Images["ui-menu"], [0, 0])
        sprites_group_ui_main.draw(screen)
        font = pygame.font.SysFont("bahnschrift", 100)
        text = font.render("Squarevival", True, (  0,   0,   0))
        text_rect = text.get_rect(center=(Config["ScreenX"] / 2, 75))
        screen.blit(text, text_rect)
    elif Variables["page"] == 1:
        screen.fill((  0, 255, 102))
        font = pygame.font.SysFont("bahnschrift", 75)
        text = font.render("Worlds", True, (  0,   0,   0))
        text_rect = text.get_rect(center=(Config["ScreenX"] / 2, 50))
        screen.blit(text, text_rect)
    elif Variables["page"] == 2:
        screen.fill((  0, 255, 102))
        font = pygame.font.SysFont("bahnschrift", 75)
        text = font.render("Create World", True, (  0,   0,   0))
        text_rect = text.get_rect(center=(Config["ScreenX"] / 2, 50))
        screen.blit(text, text_rect)
    elif Variables["page"] == 3:
        screen.fill((  0,   0,   0))
    elif Variables["page"] == 4:
        screen.fill((  0,   0,   0))
        for i in range(int((Settings["GridW"] // Variables["camera_z"] + 2) ** 2)):
            x = (((i + 0.5) % 19) - 9.5)
            if Variables["player_tileposx"] < 8:
                x += Variables["player_tileposx"] * -1 + 9
            if Variables["player_tileposx"] > Settings["GridW"] - 8:
                x += Variables["player_tileposx"] * -1 + 80.5
            y = (((i + 0.5) / 19) // 1 - 9) * Settings["GridW"]
            if Variables["player_tileposy"] < 8:
                y += 0
            if Variables["player_tileposy"] > Settings["GridH"] - 8:
                y += 0
            tile = int(Variables["player_tile"] + x + y)
            find_pos_from_tile(tile)
            screen.blit(Images[Grid[tile][4]], [Variables["tile_posx"], Variables["tile_posy"]])
            if not Grid[tile][5] == "":
                screen.blit(Images[Grid[tile][5]], [Variables["tile_posx"], Variables["tile_posy"]])
        sprites_group_entity.draw(screen)
        screen.blit(screen_effect_time, (0, 0))
        #Draw the debug screen
        if Variables["menu_pause"]:
            screen_effect_pause.fill((  0,   0,   0, 128))
            sprites_group_ui_pause.draw(screen_effect_pause)
            pygame.draw.rect(screen_effect_pause, (  0,   0,   0), [Config["ScreenX"] / 2 - 160, Config["ScreenY"] / 2 - 166, 320, 60])
            font = pygame.font.SysFont("bahnschrift", 50)
            text = font.render("Game Paused", True, (255, 255, 255))
            text_rect = text.get_rect(center=(Config["ScreenX"] / 2, Config["ScreenY"] / 2 - 136))
            screen_effect_pause.blit(text, text_rect)
            screen.blit(screen_effect_pause, (0, 0))
        elif Variables["menu_debug"] and not Variables["menu_inventory"]:
            pygame.draw.rect(screen, (  0,   0,   0), [5, 5, Config["ScreenX"] - 10, 210])
            font = pygame.font.SysFont("bahnschrift", 20)
            text = font.render(Config["ScreenCaption"], True, (255, 255, 255))
            screen.blit(text, [10, 10])
            text = font.render("Position (X, Y): " + str(round(Variables["player_posx"] * (Settings["GridW"] / Config["ScreenX"]) - 0.5, 1)) + ", " + str(round(Variables["player_posy"] * (Settings["GridH"] / Config["ScreenY"]) - 0.5, 1)), True, (255, 255, 255))
            screen.blit(text, [10, 40])
            text = font.render("Tile (#, X, Y): " + str(Variables["player_tile"]) + ", " + str(round(Variables["player_posx"] / Settings["TileSize"] - 0.5)) + ", " + str(round(Variables["player_posy"] / Settings["TileSize"] - 0.5)), True, (255, 255, 255))
            screen.blit(text, [10, 70])
            text = font.render("Tile Features (Biome, Ground, Object):", True, (255, 255, 255))
            screen.blit(text, [10, 100])
            if Grid[Variables["player_tile"]][5] == "":
                text = font.render(str(Grid[Variables["player_tile"]][3]) + ", " + str(Names[Grid[Variables["player_tile"]][4]]), True, (255, 255, 255))
            else:
                text = font.render(str(Grid[Variables["player_tile"]][3]) + ", " + str(Names[Grid[Variables["player_tile"]][4]]) + ", " + str(Names[Grid[Variables["player_tile"]][5]]), True, (255, 255, 255))
            screen.blit(text, [10, 130])
            text = font.render("Biome Info (Water, Temperature, Humidity): " + str(round(Grid[Variables["player_tile"]][0], 3)) + ", " + str(round(Grid[Variables["player_tile"]][1], 3)) + ", " + str(round(Grid[Variables["player_tile"]][2], 3)), True, (255, 255, 255))
            screen.blit(text, [10, 160])
            text = font.render("Time (%, #): " + str(round(Variables["time_day_percentage"], 1)) + ", " + str(int(Variables["time_seconds"] // Variables["time_day_length"])), True, (255, 255, 255))
            screen.blit(text, [10, 190])
        #Draw the hotbar/inventory
        if Variables["game_running"]:
            if Variables["menu_inventory"]:
                screen_effect_inventory.fill((  0,   0,   0, 128))
            else:
                screen_effect_inventory.fill((  0,   0,   0,   0))
                pygame.draw.rect(screen_effect_inventory, (  0,   0,   0, 128), [0, Config["ScreenY"] - 97, Config["ScreenX"], 97])
            screen.blit(screen_effect_inventory, (0, 0))
            for i in range(32):
                if i >= 8 and not Variables["menu_inventory"]:
                    break
                if Variables["hotbar"] == i and not Variables["menu_inventory"]:
                    pygame.draw.rect(screen, (255, 255, 192), [InventoryMargins[i][0] - 8, InventoryMargins[i][1] - 8, 97, 97])
                pygame.draw.rect(screen, (192, 192, 192), [InventoryMargins[i][0], InventoryMargins[i][1], 81, 81])
                if not Inventory[i][0] == "":
                    screen.blit(Images[Inventory[i][0].replace(".png", "")], [InventoryMargins[i][0], InventoryMargins[i][1]])
                    font = pygame.font.SysFont("bahnschrift", 36)
                    text = font.render(str(Inventory[i][1]), True, (  0,   0,   0))
                    screen.blit(text, [InventoryMargins[i][0], InventoryMargins[i][1]])
            if Variables["menu_inventory"] and not Item_Dragging == ["", 0]:
                screen.blit(Images[Item_Dragging[0].replace(".png", "")], [mousex - 40.5, mousey - 40.5])
                font = pygame.font.SysFont("bahnschrift", 36)
                text = font.render(str(Item_Dragging[1]), True, (  0,   0,   0))
                screen.blit(text, [mousex - 40.5, mousey - 40.5])
        #Draw the health and hunger bars
        if Variables["game_running"] and not Variables["menu_inventory"]:
            pygame.draw.rect(screen, (255,  51,  51), [8, Config["ScreenY"] - 125, Variables["health"] * 2, 20])
            pygame.draw.rect(screen, (128,  51,  51), [Config["ScreenX"] - Variables["hunger"] * 2 - 8, Config["ScreenY"] - 125, Variables["hunger"] * 2, 20])
            font = pygame.font.SysFont("bahnschrift", 20)
            text = font.render(str(Variables["health"]), True, (255, 255, 255))
            text_rect = text.get_rect(center=(25, Config["ScreenY"] - 115))
            screen.blit(text, text_rect)
            text = font.render(str(Variables["hunger"]), True, (255, 255, 255))
            text_rect = text.get_rect(center=(Config["ScreenX"] - 25, Config["ScreenY"] - 115))
            screen.blit(text, text_rect)
    pygame.display.update()
def main():
    global Item_Dragging
    global Item_Swap
    global mousex
    global mousey
    global screen
    global screen_effect_inventory
    global screen_effect_pause
    global screen_effect_time
    clock = pygame.time.Clock()
    #Screen and screen effects
    screen = pygame.display.set_mode((Config["ScreenX"], Config["ScreenY"]))
    screen_effect_inventory = pygame.Surface((Config["ScreenX"], Config["ScreenY"]), pygame.SRCALPHA)
    screen_effect_pause = pygame.Surface((Config["ScreenX"], Config["ScreenY"]), pygame.SRCALPHA)
    screen_effect_time = pygame.Surface((Config["ScreenX"], Config["ScreenY"]))
    screen_effect_time.set_alpha(64)
    screen_effect_time.fill((255, 128,   0))
    pygame.display.set_caption(Config["ScreenCaption"])
    pygame.display.set_icon(Images["entity-u"])
    #Resize images
    for i in range(len(Images)):
        if ImagesList[i] == "ui-menu":
            scale = 720
        elif "entity-item" in ImagesList[i]:
            scale = Settings["TileSize"] * Variables["camera_z"] * 0.75
        elif "item" in ImagesList[i]:
            scale = 81
        else:
            scale = Settings["TileSize"] * Variables["camera_z"]
        Images[ImagesList[i]] = pygame.transform.scale(Images[ImagesList[i]], (scale, scale))
    #Make user interface
    sprite = UI_Button(0, Config["ScreenX"] / 2 - 200, 200, 160, 80, (255, 255, 255), (  0,   0,   0), "bahnschrift", 40, "Play")
    sprites_group_ui_main.add(sprite)
    sprite = UI_Button(1, Config["ScreenX"] / 2, 200, 160, 80, (255, 255, 255), (  0,   0,   0), "bahnschrift", 40, "Settings")
    sprites_group_ui_main.add(sprite)
    sprite = UI_Button(2, Config["ScreenX"] / 2 + 200, 200, 160, 80, (255, 255, 255), (  0,   0,   0), "bahnschrift", 40, "Credits")
    sprites_group_ui_main.add(sprite)
    sprite = UI_Button(3, Config["ScreenX"] / 2, Config["ScreenY"] / 2 - 68, 320, 60, (  0, 255, 102), (  0,   0,   0), "bahnschrift", 40, "Settings")
    sprites_group_ui_pause.add(sprite)
    sprite = UI_Button(4, Config["ScreenX"] / 2, Config["ScreenY"] / 2, 320, 60, (  0, 255, 102), (  0,   0,   0), "bahnschrift", 40, "Save World")
    sprites_group_ui_pause.add(sprite)
    sprite = UI_Button(5, Config["ScreenX"] / 2, Config["ScreenY"] / 2 + 68, 320, 60, (  0, 255, 102), (  0,   0,   0), "bahnschrift", 40, "Save World As")
    sprites_group_ui_pause.add(sprite)
    sprite = UI_Button(6, Config["ScreenX"] / 2, Config["ScreenY"] / 2 + 136, 320, 60, (  0, 255, 102), (  0,   0,   0), "bahnschrift", 40, "Save and Quit")
    sprites_group_ui_pause.add(sprite)
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
        #Ocean biomes
        elif Grid[a][0] <= 0.1:
            if Grid[a][1] <= -0.33:
                Grid[a][3] = "Cold Ocean"
                if random.randrange(0, 100) <= Grid[a][1] * -400 - 300:
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
            #Beach biome
            Grid[a][3] = "Beach"
            Grid[a][4] = "ground-sand"
        elif Grid[a][0] >= 0.2:
            if Grid[a][1] <= -0.33:
                if Grid[a][2] <= -0.33:
                    #Snow Plains biome
                    Grid[a][3] = "Snow Plains"
                    if random.randrange(0, 100) <= 10:
                        Grid[a][4] = "ground-ice"
                    else:
                        Grid[a][4] = "ground-snow"
                        if random.randrange(0, 100) <= 5:
                            Grid[a][5] = "object-dark_tree"
                elif Grid[a][2] >= -0.33 and Grid[a][2] <= 0.33:
                    #Snow Forest biome
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
                    #Plains biome
                    Grid[a][3] = "Plains"
                    Grid[a][4] = "ground-grass"
                    if random.randrange(0, 100) <= 5:
                        if random.randrange(0, 100) <= 5:
                            Grid[a][5] = "object-apple_tree"
                        else:
                            Grid[a][5] = "object-bright_tree"
                elif Grid[a][2] >= -0.33 and Grid[a][2] <= 0.33:
                    #Forest biome
                    Grid[a][3] = "Forest"
                    Grid[a][4] = "ground-grass"
                    if random.randrange(0, 100) <= 25:
                        if random.randrange(0, 100) <= 5:
                            Grid[a][5] = "object-apple_tree"
                        else:
                            Grid[a][5] = "object-bright_tree"
                elif Grid[a][2] >= 0.33:
                    #Swamp biome
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
                    #Desert biome
                    Grid[a][3] = "Desert"
                    Grid[a][4] = "ground-sand"
                    if random.randrange(0, 100) <= 5:
                        Grid[a][5] = "object-cactus"
                elif Grid[a][2] >= -0.33 and Grid[a][2] <= 0.33:
                    #Savanna biome
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
                    #Jungle biome
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
        if Grid[structure_tile][4] in "ground-warm_water, ground-water" and Grid[structure_tile][0] <= 0.1 and Grid[structure_tile][1] >= -0.1:
            structure_island(structure_tile)
    #Make lakes
    for a in range(round(len(Grid) / 800)):
        structure_tile = random.randint(0, len(Grid))
        if not Grid[structure_tile][4] in "ground-cold_water, ground-ice, ground-warm_water, ground-water":
            structure_lake(structure_tile)
    #Make caves
    for a in range(round(len(Grid) / 800)):
        structure_tile = random.randint(0, len(Grid))
        while not Grid[structure_tile][4] in "ground-dark_grass, ground-grass, ground-snow":
            structure_tile = random.randint(0, len(Grid))
        if Grid[structure_tile][4] in "ground-dark_grass, ground-grass, ground-snow":
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
            #Check for mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Drag items in the inventory
                if Variables["menu_inventory"] and mousey >= 356:
                    Item_Swap = Inventory[find_item_from_pos(mousex, mousey)]
                    Inventory[find_item_from_pos(mousex, mousey)] = Item_Dragging
                    Item_Dragging = Item_Swap
                    Item_Swap = ["", 0]
            #Check for key presses
            if event.type == pygame.KEYDOWN:
                if Variables["game_running"]:
                    if event.key == pygame.K_1:
                        if not Variables["menu_inventory"]:
                            Variables["hotbar"] = 0
                    if event.key == pygame.K_2:
                        if not Variables["menu_inventory"]:
                            Variables["hotbar"] = 1
                    if event.key == pygame.K_3:
                        if not Variables["menu_inventory"]:
                            Variables["hotbar"] = 2
                    if event.key == pygame.K_4:
                        if not Variables["menu_inventory"]:
                            Variables["hotbar"] = 3
                    if event.key == pygame.K_5:
                        if not Variables["menu_inventory"]:
                            Variables["hotbar"] = 4
                    if event.key == pygame.K_6:
                        if not Variables["menu_inventory"]:
                            Variables["hotbar"] = 5
                    if event.key == pygame.K_7:
                        if not Variables["menu_inventory"]:
                            Variables["hotbar"] = 6
                    if event.key == pygame.K_8:
                        if not Variables["menu_inventory"]:
                            Variables["hotbar"] = 7
                    if event.key == pygame.K_a:
                        Keys["A"] = True
                    if event.key == pygame.K_d:
                        Keys["D"] = True
                    #Open/Close inventory
                    if event.key == pygame.K_e:
                        if Variables["menu_inventory"]:
                            Variables["menu_inventory"] = False
                        else:
                            Variables["menu_inventory"] = True
                    #Open/Close debug screen
                    if event.key == pygame.K_q:
                        if Variables["menu_debug"]:
                            Variables["menu_debug"] = False
                        else:
                            Variables["menu_debug"] = True
                    if event.key == pygame.K_s:
                        Keys["S"] = True
                    if event.key == pygame.K_w:
                        Keys["W"] = True
                if event.key == pygame.K_ESCAPE:
                    if Variables["page"] == 1 or Variables["page"] == 3:
                        Variables["page"] = 0
                    if Variables["page"] == 2:
                        Variables["page"] = 1
                    if Variables["page"] == 4 and not Variables["menu_inventory"]:
                        if Variables["game_running"]:
                            Variables["game_running"] = False
                            Variables["menu_pause"] = True
                        else:
                            Variables["game_running"] = True
                            Variables["menu_pause"] = False
                    if Variables["menu_settings"]:
                        Variables["menu_settings"] = False
            if event.type == pygame.KEYUP and Variables["game_running"]:
                if event.key == pygame.K_a:
                    Keys["A"] = False
                if event.key == pygame.K_d:
                    Keys["D"] = False
                if event.key == pygame.K_s:
                    Keys["S"] = False
                if event.key == pygame.K_w:
                    Keys["W"] = False
        if Variables["game_running"]:
            #Destroying objects/tiles
            if pygame.mouse.get_pressed()[0] == 1 and not Variables["menu_inventory"]:
                find_tile_from_pos(mousex, mousey)
            #Health and hunger loss
            if Variables["health"] > 0:
                if Variables["hunger"] == 0 and random.randrange(0, 100) <= 1:
                    Variables["health"] -= 1
            if Variables["hunger"] > 0:
                if Keys["A"] or Keys["D"] or Keys["S"] or Keys["W"]:
                    if random.randrange(0, 100) <= 1:
                        Variables["hunger"] -= 1
                else:
                    if random.randrange(0, 100) <= 0.5:
                        Variables["hunger"] -= 1
                if Cooldowns_Time["cooldown-cactus"] <= Variables["time_seconds"] - Cooldowns_Length["cooldown-cactus"] and Grid[Variables["player_tile"]][5] == "object-cactus":
                    Cooldowns_Time["cooldown-cactus"] = Variables["time_seconds"]
                    Variables["health"] -= random.randint(5, 10)
                    if Variables["health"] < 0:
                        Variables["health"] = 0
            if Grid[Variables["player_tile"]][5] == "object-cactus":
                if Cooldowns_Time["cooldown-cactus"] <= Variables["time_seconds"] - Cooldowns_Length["cooldown-cactus"]:
                    if Variables["health"] > 0:
                        Cooldowns_Time["cooldown-cactus"] = Variables["time_seconds"]
                        Variables["health"] -= random.randint(5, 10)
                        if Variables["health"] < 0:
                            Variables["health"] = 0
            #Health gaining
            if Cooldowns_Time["cooldown-health"] <= Variables["time_seconds"] - Cooldowns_Length["cooldown-cactus"] and Variables["health"] < 100:
                Cooldowns_Time["cooldown-health"] = Variables["time_seconds"]
                Variables["health"] += 1
            #Food eating
            if pygame.mouse.get_pressed()[2] == 1 and Variables["menu_inventory"] == 0 and Variables["hunger"] < 100:
                if Inventory[Variables["hotbar"]][0] == "item-apple":
                    itemremove(Variables["hotbar"])
                    Variables["hunger"] += 10
                if Variables["hunger"] > 100:
                    Variables["hunger"] = 100
            #Grass spreading
            for i in range(int((Settings["GridW"] // Variables["camera_z"] + 2) ** 2)):
                tile = int(Variables["player_tile"] + (((i + 0.5) % 19) - 9.5) + (((i + 0.5) / 19) // 1 - 9) * Settings["GridW"])
                if Grid[tile][4] == "ground-dirt" and random.randint(0, 100) <= 0.0001:
                    if "ground-grass" in Grid[tile - Settings["GridW"]][4] + Grid[tile - 1][4] + Grid[tile + 1][4] + Grid[tile + Settings["GridW"]][4]:
                        if "ground-dark_grass" in Grid[tile - Settings["GridW"]][4] + Grid[tile - 1][4] + Grid[tile + 1][4] + Grid[tile + Settings["GridW"]][4]:
                            if random.randrange(0, 100) <= 50:
                                Grid[tile][4] = "ground-grass"
                            else:
                                Grid[tile][4] = "ground-dark_grass"
                        else:
                            Grid[tile][4] = "ground-grass"
                    else:
                        if "ground-dark_grass" in Grid[tile - Settings["GridW"]][4] + Grid[tile - 1][4] + Grid[tile + 1][4] + Grid[tile + Settings["GridW"]][4]:
                            Grid[tile][4] = "ground-dark_grass"
            #Set camera X and Y and change them if the player is near the edge of the world
            Variables["camera_x"] = Variables["player_posx"]
            if Variables["camera_x"] < Config["ScreenX"] / Variables["camera_z"] / 2:
                Variables["camera_x"] = Config["ScreenX"] / Variables["camera_z"] / 2
            if Variables["camera_x"] > Config["ScreenX"] - Config["ScreenX"] / Variables["camera_z"] / 2:
                Variables["camera_x"] = Config["ScreenX"] - Config["ScreenX"] / Variables["camera_z"] / 2
            Variables["camera_y"] = Variables["player_posy"]
            if Variables["camera_y"] < Config["ScreenY"] / Variables["camera_z"] / 2:
                Variables["camera_y"] = Config["ScreenY"] / Variables["camera_z"] / 2
            if Variables["camera_y"] > Config["ScreenY"] - Config["ScreenY"] / Variables["camera_z"] / 2:
                Variables["camera_y"] = Config["ScreenY"] - Config["ScreenY"] / Variables["camera_z"] / 2
            #Update sprites
            sprites_group_entity.update()
            sprites_group_tile.update()
            #Set time and change time lighting
            Variables["time_frames"] += 1
            Variables["time_seconds"] = Variables["time_frames"] / Config["Framerate"]
            Variables["time_day_percentage"] = (100 / Variables["time_day_length"]) * (Variables["time_seconds"] % Variables["time_day_length"])
            screen_effect_time.set_alpha(Time_Colors[int(Variables["time_day_percentage"] // (100 / len(Time_Colors)))][3])
            screen_effect_time.fill((Time_Colors[int(Variables["time_day_percentage"] // (100 / len(Time_Colors)))][0], Time_Colors[int(Variables["time_day_percentage"] // (100 / len(Time_Colors)))][1], Time_Colors[int(Variables["time_day_percentage"] // (100 / len(Time_Colors)))][2]))
        if Variables["page"] == 0:
            sprites_group_ui_main.update()
        if Variables["menu_pause"]:
            sprites_group_ui_pause.update()
        draw()
        clock.tick(Config["Framerate"])
if __name__ == "__main__":
    main()
