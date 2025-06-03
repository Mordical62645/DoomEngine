import pygame as pg
from settings import *

class MapRenderer:
    def __init__(self, engine):
        self.engine = engine
        self.wad_data = engine.wad_data
        self.vertexes = self.wad_data.vertexes
        self.linedefs = self.wad_data.linedefs
        self.x_min, self.x_max, self.y_min, self.y_max = self.get_map_bounds()

        # Padding in pixels
        self.padding = 30

        # Map width/height
        map_width = self.x_max - self.x_min
        map_height = self.y_max - self.y_min

        # Available width/height for map (window size minus padding)
        avail_w = WIDTH - 2 * self.padding
        avail_h = HEIGHT - 2 * self.padding

        # Scale to fit both dimensions
        self.scale = min(avail_w / map_width, avail_h / map_height)

        # Offset to center the map
        self.offset_x = (WIDTH - map_width * self.scale) / 2
        self.offset_y = (HEIGHT - map_height * self.scale) / 2

        # remapping (do this last!)
        self.vertexes = [pg.math.Vector2(self.remap_x(v.x), self.remap_y(v.y)) for v in self.vertexes]

    def draw(self):
        self.draw_vertexes()
    
    def draw(self):
        for line in self.linedefs:
            p1 = self.vertexes[line.start_vertex_id]
            p2 = self.vertexes[line.end_vertex_id]
            pg.draw.line(self.engine.screen, 'orange', p1, p2, 3)
    
    def remap_x(self, n):
        return (n - self.x_min) * self.scale + self.offset_x

    def remap_y(self, n):
        # Flip y to match screen coordinates
        return HEIGHT - ((n - self.y_min) * self.scale + self.offset_y)
    

    def get_map_bounds(self):
        x_sorted = sorted(self.vertexes, key=lambda v: v.x)
        x_min, x_max = x_sorted[0].x, x_sorted[-1].x

        y_sorted = sorted(self.vertexes, key=lambda v: v.y)
        y_min, y_max = y_sorted[0].y, y_sorted[-1].y

        return x_min, x_max, y_min, y_max

    def draw_vertexes(self):
        for v in self.vertexes:
            pg.draw.circle(self.engine.screen, 'white', (v.x, v.y), 4)