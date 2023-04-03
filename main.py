from player import Player
from sprite_objects import *
from ray_casting import ray_casting_walls
from drawing import Drawing
from interaction import Interaction
from map import UPDATE_MAP, world_map, mini_map , collision_walls
from settings import MAP_LEVEL


pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
sc_map = pygame.Surface(MINIMAP_RES)
sprites = Sprites()
clock = pygame.time.Clock()
player = Player(sprites)
drawing = Drawing(sc, sc_map, player, clock)
interaction = Interaction(player, sprites, drawing)
drawing.menu()
pygame.mouse.set_visible(False)
interaction.play_music()
# return sc, sc_map, sprites, clock, player, drawing, interaction

while True:

    player.movement()
    drawing.background(player.angle)
    walls, wall_shot = ray_casting_walls(player, drawing.textures)
    drawing.world(walls + [obj.object_locate(player) for obj in sprites.list_of_objects])
    # print(walls + [obj.object_locate(player) for obj in sprites.list_of_objects if obj.flag == 'vaccine'])
    drawing.fps(clock)
    drawing.mini_map(player)
    drawing.player_weapon([wall_shot, sprites.sprite_shot])
    drawing.left_shot(player)

    interaction.interaction_objects()
    interaction.npc_action()
    interaction.clear_world()
    interaction.check_vaccination()


    status = interaction.check_win(MAP_LEVEL)
    if status and MAP_LEVEL==1: MAP_LEVEL = 2
    elif status and MAP_LEVEL==2: MAP_LEVEL = 1
   
    if status or interaction.check_lost():
        print(status,MAP_LEVEL)

     

        world_map, mini_map , collision_walls = UPDATE_MAP(MAP_LEVEL, world_map, mini_map , collision_walls ) 
        sc = pygame.display.set_mode((WIDTH, HEIGHT))
        sc_map = pygame.Surface(MINIMAP_RES)
        sprites = Sprites()
        clock = pygame.time.Clock()
        player = Player(sprites)
        drawing = Drawing(sc, sc_map, player, clock)
        interaction = Interaction(player, sprites, drawing)
        pygame.mouse.set_visible(False)
        interaction.play_music()
        pygame.display.flip()
        clock.tick()

    pygame.display.flip()
    clock.tick()