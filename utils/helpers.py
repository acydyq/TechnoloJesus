import pygame
import os

def load_assets():
    assets = {}
    asset_folder = "assets/sprites"
    
    for file in os.listdir(asset_folder):
        if file.endswith(".png"):
            name = file.split(".")[0]
            assets[name] = pygame.image.load(os.path.join(asset_folder, file)).convert_alpha()
    
    return assets
"# Common Helper Functions" 
