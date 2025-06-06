from wad_data import WADData
from settings import *
import pygame as pg
import sys
import argparse
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
        self.current_map = 'E1M1'  # Track current map
        self.on_init()

    def on_init(self):
        self.wad_data = WADData(self, map_name=self.current_map)
        self.map_renderer = MapRenderer(self)
        self.player = Player(self)
        self.bsp = BSP(self)
        self.seg_handler = SegHandler(self)
        self.view_renderer = ViewRenderer(self)

    def change_map(self, map_name):
        """Change to a different map in the WAD file."""
        self.current_map = map_name
        # Reinitialize WAD data with new map
        self.wad_data = WADData(self, map_name=map_name)
        # Reset player position and angle
        self.player = Player(self)
        # Reinitialize other components
        self.map_renderer = MapRenderer(self)
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
            elif e.type == pg.KEYDOWN:
                # Map switching with number keys 1-9
                if pg.K_1 <= e.key <= pg.K_9:
                    map_num = e.key - pg.K_1 + 1
                    new_map = f'E1M{map_num}'
                    print(f"Switching to map: {new_map}")
                    self.change_map(new_map)

                elif e.key == pg.K_ESCAPE:
                    sys.exit()
                    pg.quit()

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
    try:
        # Initialize Pygame
        pg.init()
        
        # Set up argument parser
        parser = argparse.ArgumentParser(description='Doom Engine Launcher')
        parser.add_argument('--player-speed', type=float, default=50.0,
                          help='Player speed (50 = normal)')
        parser.add_argument('--rotation-speed', type=float, default=50.0,
                          help='Rotation sensitivity (50 = normal)')
        
        # Parse arguments
        args = parser.parse_args()
        
        # Create and run the game with the provided parameters
        doom = DoomEngine(player_speed=args.player_speed, 
                         rotation_sensitivity=args.rotation_speed)
        doom.run()
    except Exception as e:
        print(f"Error: {str(e)}")
        input("Press Enter to exit...")
    finally:
        pg.quit()
        sys.exit()
