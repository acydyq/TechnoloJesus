import pygame
import pygame_gui
from game_logic.scene import IsometricScene
from utils.helpers import load_assets

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
FPS = 60

# Colors
WHITE = (255, 255, 255)

# Create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("TechnoloJesus")

# Pygame GUI Manager
ui_manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load assets
assets = load_assets()

# Main Menu UI
start_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((540, 300), (200, 50)),
    text="Start Game",
    manager=ui_manager
)
exit_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((540, 380), (200, 50)),
    text="Exit",
    manager=ui_manager
)

# Game State
running = True
scene = IsometricScene(assets)

# Main loop
clock = pygame.time.Clock()
while running:
    time_delta = clock.tick(FPS) / 1000.0

    screen.fill(WHITE)

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == start_button:
                print("Game Started!")
            elif event.ui_element == exit_button:
                running = False
        ui_manager.process_events(event)

    # Render Scene
    scene.render(screen)

    # Render UI
    ui_manager.update(time_delta)
    ui_manager.draw_ui(screen)

    pygame.display.update()

pygame.quit()
# Main Game Loop 
