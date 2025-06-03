from wad_reader import WADReader

class WADData:
    def __init__(self, engine):
        self.reader = WADReader(engine.wad_path)
        self.reader.close()