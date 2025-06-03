from wad_data import WADData
from settings import *
import pygame as pg
import sys
from map_renderer import MapRenderer
from player import Player
from bsp import BSP
from seg_handler import SegHandler
from view_renderer import ViewRenderer


class DoomEngine:
    def __init__(self, wad_path='wad/DOOM1.WAD', player_speed=50, rotation_sensitivity=50):
        self.wad_path = wad_path
        self.screen = pg.display.set_mode(WIN_RES, pg.SCALED)
        self.framebuffer = pg.surfarray.array3d(self.screen)
        self.clock = pg.time.Clock()
        self.running = True
        self.dt = 1 / 60
        # Calculate the actual speed multiplier
        self.speed_multiplier = player_speed / 50.0
        self.rotation_multiplier = rotation_sensitivity / 50.0
        self.on_init()

    def on_init(self):
        self.wad_data = WADData(self, map_name='E1M1')
        self.map_renderer = MapRenderer(self)
        self.player = Player(self)
        self.bsp = BSP(self)
        self.seg_handler = SegHandler(self)
        self.view_renderer = ViewRenderer(self)

    def update(self):
        self.player.update()
        self.seg_handler.update()
        self.bsp.update()
        self.dt = self.clock.tick()
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        pg.surfarray.blit_array(self.screen, self.framebuffer)
        self.view_renderer.draw_sprite()
        pg.display.flip()

    def check_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.running = False
                pg.quit()
                sys.exit()

    def run(self):
        while self.running:
            self.check_events()
            self.update()
            self.draw()


def get_player_speed():
    while True:
        try:
            speed = float(input("Enter player speed (50 = normal): "))
            if speed <= 0:
                print("Speed must be greater than 0")
                continue
            return speed
        except ValueError:
            print("Please enter a valid number")


def get_rotation_sensitivity():
    while True:
        try:
            sensitivity = float(input("Enter rotation sensitivity (50 = normal): "))
            if sensitivity <= 0:
                print("Sensitivity must be greater than 0")
                continue
            return sensitivity
        except ValueError:
            print("Please enter a valid number")


if __name__ == '__main__':
    player_speed = get_player_speed()
    rotation_sensitivity = get_rotation_sensitivity()
    doom = DoomEngine(player_speed=player_speed, rotation_sensitivity=rotation_sensitivity)
    doom.run()
