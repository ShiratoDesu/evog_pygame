import os
from assets.assets import Assets

class Sprites(Assets):
    def __init__(self) -> None:
        Assets.__init__(self)
        self.load_sprites()
    
    def load_sprites(self):
        self.mc_sprite = os.path.join(self.sprites_dir, "knight_design.png")