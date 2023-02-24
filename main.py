from player import Player
from sprite_objects import *
from ray_casting import ray_casting_walls
from drawing import Drawing
from interaction import Interaction



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
    # print(interaction.check_win())
    if interaction.check_win() or interaction.check_lost():
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