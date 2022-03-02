import os

class Assets():
    def __init__(self) -> None:
        # assets folder
        self.assets_dir = os.path.join("assets")
        self.sprites_dir = os.path.join(self.assets_dir, "sprites")
        self.font_dir = os.path.join(self.assets_dir, "font")
        self.sounds_dir = os.path.join(self.assets_dir, "sounds")
        self.words_dir = os.path.join(self.assets_dir, 'words')