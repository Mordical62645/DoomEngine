from wad_reader import WADReader

class WADData:
    def __init__(self, engine, map_name):
        self.reader = WADReader(engine.wad_path)
        self.map_index = self.get_lump_index(lump_name=map_name)
        print(f'\n{map_name}_index = {self.map_index}')

        self.reader.close()

    def get_lump_index(self, lump_name):
        for index, lump_info in enumerate(self.reader.directory):
            if lump_name in lump_info.values():
                return index