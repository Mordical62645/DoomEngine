import struct # so we can covert read bytes corresponding to the data of the C language data type necessary for Python
from pygame.math import Vector2 as vec2
from datatypes import *

class WADReader:
    def __init__(self, wad_path):
        self.wad_file = open(wad_path, 'rb')
        self.header = self.read_header()
        self.directory = self.read_directory()
        print(f"HEADER:\n{self.header}")
        # print("DIRECTORY:")
        # [print('\n', i) for i in self.directory]

    # linedef
    def read_linedef(self, offset):
        # 14 bytes  2H x 7
        read_2_bytes = self.read_2_bytes

        linedef = Linedef()
        linedef.start_vertex_id = read_2_bytes(offset, byte_format='H')
        linedef.end_vertex_id = read_2_bytes(offset + 2, byte_format='H')
        linedef.flags = read_2_bytes(offset + 4, byte_format='H')
        linedef.line_type = read_2_bytes(offset + 6, byte_format='H')
        linedef.sector_tag = read_2_bytes(offset + 8, byte_format='H')
        linedef.front_sidedef_id = read_2_bytes(offset + 10, byte_format='H')
        linedef.back_sidedef_id = read_2_bytes(offset + 12, byte_format='H')
        return linedef

    # vertex
    def read_vertex(self, offset):
        # 4 bytes = 2h + 2h
        x = self.read_2_bytes(offset, byte_format='h')
        y = self.read_2_bytes(offset + 2, byte_format='h')
        return vec2(x, y)

    # Directory
    def read_directory(self):
        directory = []
        for i in range(self.header['lump_count']):
            offset = self.header['init_offset'] + i * 16
            lump_info = {
                'lump_offset': self.read_4_bytes(offset),
                'lump_size': self.read_4_bytes(offset+4),
                'lump_name': self.read_string(offset + 8, num_bytes=8)
            }
            directory.append(lump_info)
        return directory

    # we can now read the header of the wad wile (12 bytes)
    def read_header(self):
        return {
            'wad_type': self.read_string(offset=0, num_bytes=4),
            'lump_count': self.read_4_bytes(offset=4), # lumps are the assets from the wad file
            'init_offset': self.read_4_bytes(offset=8) # where lumps begin
        }
    
    def read_1_bytes(self, offset, byte_format):
        # B - unsigned char, b - signed
        return self.read_bytes(offset=offset, num_bytes=1, byte_format=byte_format) [0]

    def read_2_bytes(self, offset, byte_format):
        # H - uint16, h - int16
        return self.read_bytes(offset=offset, num_bytes=2, byte_format=byte_format) [0]

    # method for reading 4 bytes (see notes.txt)
    def read_4_bytes(self, offset, byte_format='i'):
        # I - unit32, i - int32
        return self.read_bytes(offset=offset, num_bytes=4, byte_format=byte_format) [0]

    # using read_bytes() method, we can read strings from the wad file.
    def read_string(self, offset, num_bytes):
        # c - char
        return ''.join(b.decode('ascii') for b in self.read_bytes(offset, num_bytes, byte_format='c' * num_bytes) if ord(b) !=0).upper()

    # method for reading bytes
    def read_bytes(self, offset, num_bytes, byte_format):
        self.wad_file.seek(offset)
        buffer = self.wad_file.read(num_bytes)
        return struct.unpack(byte_format, buffer)
    
    def close(self):
        self.wad_file.close()