                     


# import pygame
# import random
# import sys
# import os

# # Initialize Pygame
# pygame.init()

# # Constants
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 400
# GROUND_HEIGHT = 300
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GRAY = (100, 100, 100)
# DARK_GRAY = (80, 80, 80)
# FPS = 60

# # Create the game window
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("T-Rex Runner")
# clock = pygame.time.Clock()

# # Create font for text
# font = pygame.font.SysFont('Arial', 20)
# game_over_font = pygame.font.SysFont('Arial', 40)

# # Pixel Art Sprites
# def create_trex_sprite():
#     # Create a surface for the T-Rex sprite based on pixel art
#     sprite = pygame.Surface((22, 24), pygame.SRCALPHA)
    
#     # Pixel art for T-Rex (similar to the image provided)
#     pixels = [
#         "    DDDDD            ",
#         "   DDDDDDDD          ",
#         "   DDDDDDWDD         ",
#         "   DDDDDDDDD         ",
#         "   DDDDD             ",
#         "   DDDDDDD           ",
#         "   DDDDDDDD          ",
#         "DDDDDDDDD            ",
#         "DDDDDDDDDD           ",
#         " DDDDDDDDD           ",
#         "  DDDDDDDDD          ",
#         "   DDDDDDDD          ",
#         "   DDDDDDD           ",
#         "   DDDDDD            ",
#         "   DDDDD             ",
#         "   DD DD             ",
#         "   DD DD             ",
#         "   DD DD             ",
#         "   DD DD             ",
#         "                     ",
#         "                     ",
#         "                     ",
#         "                     ",
#         "                     "
#     ]
    
#     # Draw pixels
#     for y, row in enumerate(pixels):
#         for x, pixel in enumerate(row):
#             if pixel == "D":
#                 sprite.set_at((x, y), DARK_GRAY)
#             elif pixel == "W":
#                 sprite.set_at((x, y), WHITE)
    
#     return sprite

# def create_trex_ducking_sprite():
#     # Create a surface for the ducking T-Rex sprite
#     sprite = pygame.Surface((30, 15), pygame.SRCALPHA)
    
#     # Pixel art for ducking T-Rex
#     pixels = [
#         "      DDDDD                 ",
#         "     DDDDDDDD               ",
#         "     DDDDDDWDD              ",
#         "     DDDDDDDDDDDDDDD        ",
#         "     DDDDDDDDDDDDDDDDD      ",
#         "     DDDDDDDDDDDDDDDDD      ",
#         "     DDDDDDDDDDDDDDD        ",
#         "     DDDDDDD                ",
#         "     DD DD                  ",
#         "     DD DD                  ",
#         "                            ",
#         "                            ",
#         "                            ",
#         "                            ",
#         "                            "
#     ]
    
#     # Draw pixels
#     for y, row in enumerate(pixels):
#         for x, pixel in enumerate(row):
#             if pixel == "D":
#                 sprite.set_at((x, y), DARK_GRAY)
#             elif pixel == "W":
#                 sprite.set_at((x, y), WHITE)
    
#     return sprite

# def create_cactus_sprite():
#     # Create a surface for the cactus sprite based on pixel art
#     sprite = pygame.Surface((14, 30), pygame.SRCALPHA)
    
#     # Pixel art for cactus (similar to the image provided)
#     pixels = [
#         "      DD      ",
#         "      DD      ",
#         "      DD      ",
#         "      DD      ",
#         "      DD      ",
#         "   DD DD      ",
#         "   DD DD      ",
#         "   DD DD      ",
#         "   DD DD DD   ",
#         "   DD DD DD   ",
#         "   DD DD DD   ",
#         "   DD DD DD   ",
#         "   DD DD DD   ",
#         "      DD      ",
#         "      DD      ",
#         "      DD      ",
#         "      DD      ",
#         "      DD      ",
#         "      DD      ",
#         "      DD      ",
#         "      DD      ",
#         "      DD      ",
#         "      DD      ",
#         "      DD      ",
#         "      DD      ",
#         "      DD      ",
#         "      DD      ",
#         "      DD      ",
#         "      DD      ",
#         "              "
#     ]
    
#     # Draw pixels
#     for y, row in enumerate(pixels):
#         for x, pixel in enumerate(row):
#             if pixel == "D":
#                 sprite.set_at((x, y), DARK_GRAY)
    
#     return sprite

# def create_bird_sprite():
#     # Create a surface for the bird sprite based on pixel art
#     sprite = pygame.Surface((22, 16), pygame.SRCALPHA)
    
#     # Pixel art for bird (similar to the bird reference)
#     pixels = [
#         "                      ",
#         "                      ",
#         "                      ",
#         "     D                ",
#         "    DDD               ",
#         "DDDDDDDDD             ",
#         "DDDDDDDDDDD           ",
#         "DDDDD   DDD           ",
#         " D                    ",
#         "                      ",
#         "                      ",
#         "                      ",
#         "                      ",
#         "                      ",
#         "                      ",
#         "                      "
#     ]
    
#     # Draw pixels
#     for y, row in enumerate(pixels):
#         for x, pixel in enumerate(row):
#             if pixel == "D":
#                 sprite.set_at((x, y), DARK_GRAY)
    
#     return sprite

# def create_bird_flying_sprite():
#     # Create a surface for the bird sprite with wings up
#     sprite = pygame.Surface((22, 16), pygame.SRCALPHA)
    
#     # Pixel art for bird with wings up
#     pixels = [
#         "                      ",
#         "     D                ",
#         "    DDD               ",
#         "DDDDDDDDD             ",
#         "DDDDDDDDDDD           ",
#         "DDDDD   DDD           ",
#         " D      D D           ",
#         "        D D           ",
#         "        D             ",
#         "                      ",
#         "                      ",
#         "                      ",
#         "                      ",
#         "                      ",
#         "                      ",
#         "                      "
#     ]
    
#     # Draw pixels
#     for y, row in enumerate(pixels):
#         for x, pixel in enumerate(row):
#             if pixel == "D":
#                 sprite.set_at((x, y), DARK_GRAY)
    
#     return sprite

# # Create the sprites
# trex_sprite = create_trex_sprite()
# trex_ducking_sprite = create_trex_ducking_sprite()
# cactus_sprite = create_cactus_sprite()
# bird_sprite = create_bird_sprite()
# bird_flying_sprite = create_bird_flying_sprite()

# class TRex:
#     def __init__(self):
#         self.sprite = trex_sprite
#         self.ducking_sprite = trex_ducking_sprite
#         self.width = 22
#         self.height = 24
#         self.ducking_width = 30
#         self.ducking_height = 15
#         self.x = 50
#         self.y = GROUND_HEIGHT - self.height
#         self.jump_velocity = 15
#         self.velocity = 0
#         self.gravity = 0.8
#         self.jumping = False
#         self.ducking = False
        
#         # Create hitbox
#         self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
#     def jump(self):
#         if not self.jumping:
#             self.velocity = -self.jump_velocity
#             self.jumping = True
    
#     def duck(self):
#         if not self.jumping:
#             self.ducking = True
#             self.y = GROUND_HEIGHT - self.ducking_height
    
#     def stand(self):
#         if self.ducking:
#             self.ducking = False
#             self.y = GROUND_HEIGHT - self.height
    
#     def update(self):
#         # Apply gravity
#         if self.jumping:
#             self.velocity += self.gravity
#             self.y += self.velocity
            
#             # Check if landed
#             if self.y >= GROUND_HEIGHT - self.height:
#                 self.y = GROUND_HEIGHT - self.height
#                 self.jumping = False
#                 self.velocity = 0
        
#         # Update rect for collision detection
#         if self.ducking:
#             self.rect = pygame.Rect(self.x, self.y, self.ducking_width, self.ducking_height)
#         else:
#             self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
#     def draw(self):
#         if self.ducking:
#             screen.blit(self.ducking_sprite, (self.x, self.y))
#         else:
#             screen.blit(self.sprite, (self.x, self.y))

# class Obstacle:
#     def __init__(self, x, speed, obstacle_type="cactus"):
#         self.type = obstacle_type
#         self.speed = speed
#         self.x = x
        
#         if obstacle_type == "cactus":
#             self.sprite = cactus_sprite
#             self.width = 14
#             self.height = 30
#             self.y = GROUND_HEIGHT - self.height
#         else:  # bird
#             self.sprite = bird_sprite
#             self.flying_sprite = bird_flying_sprite
#             self.width = 22
#             self.height = 16
#             self.y = GROUND_HEIGHT - random.randint(30, 80)
#             self.wing_up = False
#             self.wing_timer = 0
        
#         # Create hitbox (slightly smaller than visual sprite)
#         self.rect = pygame.Rect(self.x + 2, self.y + 2, self.width - 4, self.height - 4)
    
#     def update(self):
#         self.x -= self.speed
        
#         # Update hitbox
#         self.rect = pygame.Rect(self.x + 2, self.y + 2, self.width - 4, self.height - 4)
        
#         # Update bird animation
#         if self.type == "bird":
#             self.wing_timer += 1
#             if self.wing_timer > 15:
#                 self.wing_up = not self.wing_up
#                 self.wing_timer = 0
    
#     def draw(self):
#         if self.type == "cactus":
#             screen.blit(self.sprite, (self.x, self.y))
#         else:  # bird
#             if self.wing_up:
#                 screen.blit(self.flying_sprite, (self.x, self.y))
#             else:
#                 screen.blit(self.sprite, (self.x, self.y))

# class Cloud:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.width = random.randint(30, 60)
#         self.height = random.randint(15, 30)
#         self.speed = 1
        
#     def update(self):
#         self.x -= self.speed
        
#     def draw(self):
#         # Draw simple cloud
#         pygame.draw.ellipse(screen, WHITE, (self.x, self.y, self.width, self.height))
#         pygame.draw.ellipse(screen, WHITE, (self.x + self.width//4, self.y - self.height//4, self.width//2, self.height//2))
#         pygame.draw.ellipse(screen, WHITE, (self.x + self.width//2, self.y, self.width//2, self.height//1.5))

# class Game:
#     def __init__(self):
#         self.trex = TRex()
#         self.obstacles = []
#         self.clouds = []
#         self.score = 0
#         self.high_score = 0
#         self.speed = 5
#         self.obstacle_frequency = 1500  # ms
#         self.last_obstacle = pygame.time.get_ticks()
#         self.game_over = False
#         self.auto_mode = False
#         self.ground_offset = 0
        
#         # Add initial clouds
#         for _ in range(5):
#             self.clouds.append(Cloud(
#                 random.randint(0, SCREEN_WIDTH),
#                 random.randint(50, 200)
#             ))
    
#     def reset(self):
#         self.trex = TRex()
#         self.obstacles = []
#         self.score = 0
#         self.speed = 5
#         self.obstacle_frequency = 1500
#         self.last_obstacle = pygame.time.get_ticks()
#         self.game_over = False
        
#     def update(self):
#         if self.game_over:
#             return
            
#         # Update T-Rex
#         self.trex.update()
        
#         # Auto-mode logic
#         if self.auto_mode:
#             self.auto_play()
            
#         # Update obstacles
#         for obstacle in self.obstacles[:]:
#             obstacle.update()
            
#             # Check collision
#             if self.trex.rect.colliderect(obstacle.rect):
#                 self.game_over = True
#                 if self.score > self.high_score:
#                     self.high_score = self.score
            
#             # Remove obstacles that are off-screen
#             if obstacle.x + obstacle.width < 0:
#                 self.obstacles.remove(obstacle)
#                 self.score += 1
                
#                 # Increase speed every 5 points
#                 if self.score % 5 == 0:
#                     self.speed += 0.5
#                     self.obstacle_frequency = max(500, self.obstacle_frequency - 100)
        
#         # Add new obstacles
#         current_time = pygame.time.get_ticks()
#         if current_time - self.last_obstacle > self.obstacle_frequency:
#             if random.random() < 0.7:
#                 self.obstacles.append(Obstacle(SCREEN_WIDTH, self.speed, "cactus"))
#             else:
#                 self.obstacles.append(Obstacle(SCREEN_WIDTH, self.speed, "bird"))
#             self.last_obstacle = current_time
            
#         # Update clouds
#         for cloud in self.clouds[:]:
#             cloud.update()
#             if cloud.x + cloud.width < 0:
#                 self.clouds.remove(cloud)
                
#         # Add new clouds randomly
#         if random.random() < 0.01:
#             self.clouds.append(Cloud(
#                 SCREEN_WIDTH,
#                 random.randint(50, 200)
#             ))
            
#         # Update ground offset (for scrolling effect)
#         self.ground_offset = (self.ground_offset + self.speed) % 40
    
#     def auto_play(self):
#         # Simple AI to play the game
#         # Look for the nearest obstacle
#         if self.obstacles:
#             nearest = self.obstacles[0]
#             distance = nearest.x - (self.trex.x + self.trex.width)
            
#             # Decide to jump or duck based on the obstacle type and distance
#             if distance < 120 and distance > 0:
#                 if nearest.type == "cactus":
#                     self.trex.jump()
#                 elif nearest.type == "bird":
#                     # If bird is flying low, jump
#                     if nearest.y > GROUND_HEIGHT - 70:
#                         self.trex.jump()
#                     # If bird is flying high, duck
#                     else:
#                         self.trex.duck()
#             elif distance > 120 and self.trex.ducking:
#                 self.trex.stand()
    
#     def draw(self):
#         # Clear screen
#         screen.fill((240, 240, 240))
        
#         # Draw clouds
#         for cloud in self.clouds:
#             cloud.draw()
        
#         # Draw ground
#         pygame.draw.line(screen, BLACK, (0, GROUND_HEIGHT), (SCREEN_WIDTH, GROUND_HEIGHT), 2)
        
#         # Draw ground texture (dots)
#         for i in range(40):
#             x_pos = (i * 20 - self.ground_offset) % SCREEN_WIDTH
#             y_pos = GROUND_HEIGHT + random.randint(5, 15)
#             size = random.randint(1, 2)
#             pygame.draw.circle(screen, GRAY, (x_pos, y_pos), size)
        
#         # Draw T-Rex
#         self.trex.draw()
        
#         # Draw obstacles
#         for obstacle in self.obstacles:
#             obstacle.draw()
        
#         # Draw score
#         score_text = font.render(f"Score: {self.score}   High Score: {self.high_score}", True, BLACK)
#         screen.blit(score_text, (20, 20))
        
#         # Draw auto mode status
#         auto_text = font.render(f"Auto Mode: {'ON' if self.auto_mode else 'OFF'} (Press 'A' to toggle)", True, BLACK)
#         screen.blit(auto_text, (20, 50))
        
#         # Draw speed
#         speed_text = font.render(f"Speed: {self.speed:.1f}", True, BLACK)
#         screen.blit(speed_text, (20, 80))
        
#         # Draw game over
#         if self.game_over:
#             over_text = game_over_font.render("GAME OVER", True, BLACK)
#             restart_text = font.render("Press SPACE to restart", True, BLACK)
#             screen.blit(over_text, (SCREEN_WIDTH//2 - over_text.get_width()//2, 150))
#             screen.blit(restart_text, (SCREEN_WIDTH//2 - restart_text.get_width()//2, 200))

# # Create the game
# game = Game()

# # Game loop
# running = True
# while running:
#     # Event handling
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
        
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE:
#                 if game.game_over:
#                     game.reset()
#                 else:
#                     game.trex.jump()
#             elif event.key == pygame.K_DOWN:
#                 game.trex.duck()
#             elif event.key == pygame.K_a:
#                 # Toggle auto mode
#                 game.auto_mode = not game.auto_mode
    
#     # Check for key releases
#     keys = pygame.key.get_pressed()
#     if not keys[pygame.K_DOWN] and not game.auto_mode:
#         game.trex.stand()
    
#     # Update game state
#     game.update()
    
#     # Draw everything
#     game.draw()
    
#     # Update display
#     pygame.display.flip()
    
#     # Control game speed
#     clock.tick(FPS)

# # Quit the game
# pygame.quit()
# sys.exit()


import pygame
import random
import sys
import os
import asyncio  # Add this import for Pygbag compatibility

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
GROUND_HEIGHT = 300
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
DARK_GRAY = (80, 80, 80)
FPS = 60

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("T-Rex Runner")
clock = pygame.time.Clock()

# Create font for text
font = pygame.font.SysFont('Arial', 20)
game_over_font = pygame.font.SysFont('Arial', 40)

# Pixel Art Sprites
def create_trex_sprite():
    # Create a surface for the T-Rex sprite based on pixel art
    sprite = pygame.Surface((22, 24), pygame.SRCALPHA)
    
    # Pixel art for T-Rex (similar to the image provided)
    pixels = [
        "    DDDDD            ",
        "   DDDDDDDD          ",
        "   DDDDDDWDD         ",
        "   DDDDDDDDD         ",
        "   DDDDD             ",
        "   DDDDDDD           ",
        "   DDDDDDDD          ",
        "DDDDDDDDD            ",
        "DDDDDDDDDD           ",
        " DDDDDDDDD           ",
        "  DDDDDDDDD          ",
        "   DDDDDDDD          ",
        "   DDDDDDD           ",
        "   DDDDDD            ",
        "   DDDDD             ",
        "   DD DD             ",
        "   DD DD             ",
        "   DD DD             ",
        "   DD DD             ",
        "                     ",
        "                     ",
        "                     ",
        "                     ",
        "                     "
    ]
    
    # Draw pixels
    for y, row in enumerate(pixels):
        for x, pixel in enumerate(row):
            if pixel == "D":
                sprite.set_at((x, y), DARK_GRAY)
            elif pixel == "W":
                sprite.set_at((x, y), WHITE)
    
    return sprite

def create_trex_ducking_sprite():
    # Create a surface for the ducking T-Rex sprite
    sprite = pygame.Surface((30, 15), pygame.SRCALPHA)
    
    # Pixel art for ducking T-Rex
    pixels = [
        "      DDDDD                 ",
        "     DDDDDDDD               ",
        "     DDDDDDWDD              ",
        "     DDDDDDDDDDDDDDD        ",
        "     DDDDDDDDDDDDDDDDD      ",
        "     DDDDDDDDDDDDDDDDD      ",
        "     DDDDDDDDDDDDDDD        ",
        "     DDDDDDD                ",
        "     DD DD                  ",
        "     DD DD                  ",
        "                            ",
        "                            ",
        "                            ",
        "                            ",
        "                            "
    ]
    
    # Draw pixels
    for y, row in enumerate(pixels):
        for x, pixel in enumerate(row):
            if pixel == "D":
                sprite.set_at((x, y), DARK_GRAY)
            elif pixel == "W":
                sprite.set_at((x, y), WHITE)
    
    return sprite

def create_cactus_sprite():
    # Create a surface for the cactus sprite based on pixel art
    sprite = pygame.Surface((14, 30), pygame.SRCALPHA)
    
    # Pixel art for cactus (similar to the image provided)
    pixels = [
        "      DD      ",
        "      DD      ",
        "      DD      ",
        "      DD      ",
        "      DD      ",
        "   DD DD      ",
        "   DD DD      ",
        "   DD DD      ",
        "   DD DD DD   ",
        "   DD DD DD   ",
        "   DD DD DD   ",
        "   DD DD DD   ",
        "   DD DD DD   ",
        "      DD      ",
        "      DD      ",
        "      DD      ",
        "      DD      ",
        "      DD      ",
        "      DD      ",
        "      DD      ",
        "      DD      ",
        "      DD      ",
        "      DD      ",
        "      DD      ",
        "      DD      ",
        "      DD      ",
        "      DD      ",
        "      DD      ",
        "      DD      ",
        "              "
    ]
    
    # Draw pixels
    for y, row in enumerate(pixels):
        for x, pixel in enumerate(row):
            if pixel == "D":
                sprite.set_at((x, y), DARK_GRAY)
    
    return sprite

def create_bird_sprite():
    # Create a surface for the bird sprite based on pixel art
    sprite = pygame.Surface((22, 16), pygame.SRCALPHA)
    
    # Pixel art for bird (similar to the bird reference)
    pixels = [
        "                      ",
        "                      ",
        "                      ",
        "     D                ",
        "    DDD               ",
        "DDDDDDDDD             ",
        "DDDDDDDDDDD           ",
        "DDDDD   DDD           ",
        " D                    ",
        "                      ",
        "                      ",
        "                      ",
        "                      ",
        "                      ",
        "                      ",
        "                      "
    ]
    
    # Draw pixels
    for y, row in enumerate(pixels):
        for x, pixel in enumerate(row):
            if pixel == "D":
                sprite.set_at((x, y), DARK_GRAY)
    
    return sprite

def create_bird_flying_sprite():
    # Create a surface for the bird sprite with wings up
    sprite = pygame.Surface((22, 16), pygame.SRCALPHA)
    
    # Pixel art for bird with wings up
    pixels = [
        "                      ",
        "     D                ",
        "    DDD               ",
        "DDDDDDDDD             ",
        "DDDDDDDDDDD           ",
        "DDDDD   DDD           ",
        " D      D D           ",
        "        D D           ",
        "        D             ",
        "                      ",
        "                      ",
        "                      ",
        "                      ",
        "                      ",
        "                      ",
        "                      "
    ]
    
    # Draw pixels
    for y, row in enumerate(pixels):
        for x, pixel in enumerate(row):
            if pixel == "D":
                sprite.set_at((x, y), DARK_GRAY)
    
    return sprite

# Create the sprites
trex_sprite = create_trex_sprite()
trex_ducking_sprite = create_trex_ducking_sprite()
cactus_sprite = create_cactus_sprite()
bird_sprite = create_bird_sprite()
bird_flying_sprite = create_bird_flying_sprite()

class TRex:
    def __init__(self):
        self.sprite = trex_sprite
        self.ducking_sprite = trex_ducking_sprite
        self.width = 22
        self.height = 24
        self.ducking_width = 30
        self.ducking_height = 15
        self.x = 50
        self.y = GROUND_HEIGHT - self.height
        self.jump_velocity = 15
        self.velocity = 0
        self.gravity = 0.8
        self.jumping = False
        self.ducking = False
        
        # Create hitbox
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def jump(self):
        if not self.jumping:
            self.velocity = -self.jump_velocity
            self.jumping = True
    
    def duck(self):
        if not self.jumping:
            self.ducking = True
            self.y = GROUND_HEIGHT - self.ducking_height
    
    def stand(self):
        if self.ducking:
            self.ducking = False
            self.y = GROUND_HEIGHT - self.height
    
    def update(self):
        # Apply gravity
        if self.jumping:
            self.velocity += self.gravity
            self.y += self.velocity
            
            # Check if landed
            if self.y >= GROUND_HEIGHT - self.height:
                self.y = GROUND_HEIGHT - self.height
                self.jumping = False
                self.velocity = 0
        
        # Update rect for collision detection
        if self.ducking:
            self.rect = pygame.Rect(self.x, self.y, self.ducking_width, self.ducking_height)
        else:
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def draw(self):
        if self.ducking:
            screen.blit(self.ducking_sprite, (self.x, self.y))
        else:
            screen.blit(self.sprite, (self.x, self.y))

class Obstacle:
    def __init__(self, x, speed, obstacle_type="cactus"):
        self.type = obstacle_type
        self.speed = speed
        self.x = x
        
        if obstacle_type == "cactus":
            self.sprite = cactus_sprite
            self.width = 14
            self.height = 30
            self.y = GROUND_HEIGHT - self.height
        else:  # bird
            self.sprite = bird_sprite
            self.flying_sprite = bird_flying_sprite
            self.width = 22
            self.height = 16
            self.y = GROUND_HEIGHT - random.randint(30, 80)
            self.wing_up = False
            self.wing_timer = 0
        
        # Create hitbox (slightly smaller than visual sprite)
        self.rect = pygame.Rect(self.x + 2, self.y + 2, self.width - 4, self.height - 4)
    
    def update(self):
        self.x -= self.speed
        
        # Update hitbox
        self.rect = pygame.Rect(self.x + 2, self.y + 2, self.width - 4, self.height - 4)
        
        # Update bird animation
        if self.type == "bird":
            self.wing_timer += 1
            if self.wing_timer > 15:
                self.wing_up = not self.wing_up
                self.wing_timer = 0
    
    def draw(self):
        if self.type == "cactus":
            screen.blit(self.sprite, (self.x, self.y))
        else:  # bird
            if self.wing_up:
                screen.blit(self.flying_sprite, (self.x, self.y))
            else:
                screen.blit(self.sprite, (self.x, self.y))

class Cloud:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = random.randint(30, 60)
        self.height = random.randint(15, 30)
        self.speed = 1
        
    def update(self):
        self.x -= self.speed
        
    def draw(self):
        # Draw simple cloud
        pygame.draw.ellipse(screen, WHITE, (self.x, self.y, self.width, self.height))
        pygame.draw.ellipse(screen, WHITE, (self.x + self.width//4, self.y - self.height//4, self.width//2, self.height//2))
        pygame.draw.ellipse(screen, WHITE, (self.x + self.width//2, self.y, self.width//2, self.height//1.5))

class Game:
    def __init__(self):
        self.trex = TRex()
        self.obstacles = []
        self.clouds = []
        self.score = 0
        self.high_score = 0
        self.speed = 5
        self.obstacle_frequency = 1500  # ms
        self.last_obstacle = pygame.time.get_ticks()
        self.game_over = False
        self.auto_mode = False
        self.ground_offset = 0
        
        # Add initial clouds
        for _ in range(5):
            self.clouds.append(Cloud(
                random.randint(0, SCREEN_WIDTH),
                random.randint(50, 200)
            ))
    
    def reset(self):
        self.trex = TRex()
        self.obstacles = []
        self.score = 0
        self.speed = 5
        self.obstacle_frequency = 1500
        self.last_obstacle = pygame.time.get_ticks()
        self.game_over = False
        
    def update(self):
        if self.game_over:
            return
            
        # Update T-Rex
        self.trex.update()
        
        # Auto-mode logic
        if self.auto_mode:
            self.auto_play()
            
        # Update obstacles
        for obstacle in self.obstacles[:]:
            obstacle.update()
            
            # Check collision
            if self.trex.rect.colliderect(obstacle.rect):
                self.game_over = True
                if self.score > self.high_score:
                    self.high_score = self.score
            
            # Remove obstacles that are off-screen
            if obstacle.x + obstacle.width < 0:
                self.obstacles.remove(obstacle)
                self.score += 1
                
                # Increase speed every 5 points
                if self.score % 5 == 0:
                    self.speed += 0.5
                    self.obstacle_frequency = max(500, self.obstacle_frequency - 100)
        
        # Add new obstacles
        current_time = pygame.time.get_ticks()
        if current_time - self.last_obstacle > self.obstacle_frequency:
            if random.random() < 0.7:
                self.obstacles.append(Obstacle(SCREEN_WIDTH, self.speed, "cactus"))
            else:
                self.obstacles.append(Obstacle(SCREEN_WIDTH, self.speed, "bird"))
            self.last_obstacle = current_time
            
        # Update clouds
        for cloud in self.clouds[:]:
            cloud.update()
            if cloud.x + cloud.width < 0:
                self.clouds.remove(cloud)
                
        # Add new clouds randomly
        if random.random() < 0.01:
            self.clouds.append(Cloud(
                SCREEN_WIDTH,
                random.randint(50, 200)
            ))
            
        # Update ground offset (for scrolling effect)
        self.ground_offset = (self.ground_offset + self.speed) % 40
    
    def auto_play(self):
        # Simple AI to play the game
        # Look for the nearest obstacle
        if self.obstacles:
            nearest = self.obstacles[0]
            distance = nearest.x - (self.trex.x + self.trex.width)
            
            # Decide to jump or duck based on the obstacle type and distance
            if distance < 120 and distance > 0:
                if nearest.type == "cactus":
                    self.trex.jump()
                elif nearest.type == "bird":
                    # If bird is flying low, jump
                    if nearest.y > GROUND_HEIGHT - 70:
                        self.trex.jump()
                    # If bird is flying high, duck
                    else:
                        self.trex.duck()
            elif distance > 120 and self.trex.ducking:
                self.trex.stand()
    
    def draw(self):
        # Clear screen
        screen.fill((240, 240, 240))
        
        # Draw clouds
        for cloud in self.clouds:
            cloud.draw()
        
        # Draw ground
        pygame.draw.line(screen, BLACK, (0, GROUND_HEIGHT), (SCREEN_WIDTH, GROUND_HEIGHT), 2)
        
        # Draw ground texture (dots)
        for i in range(40):
            x_pos = (i * 20 - self.ground_offset) % SCREEN_WIDTH
            y_pos = GROUND_HEIGHT + random.randint(5, 15)
            size = random.randint(1, 2)
            pygame.draw.circle(screen, GRAY, (x_pos, y_pos), size)
        
        # Draw T-Rex
        self.trex.draw()
        
        # Draw obstacles
        for obstacle in self.obstacles:
            obstacle.draw()
        
        # Draw score
        score_text = font.render(f"Score: {self.score}   High Score: {self.high_score}", True, BLACK)
        screen.blit(score_text, (20, 20))
        
        # Draw auto mode status
        auto_text = font.render(f"Auto Mode: {'ON' if self.auto_mode else 'OFF'} (Press 'A' to toggle)", True, BLACK)
        screen.blit(auto_text, (20, 50))
        
        # Draw speed
        speed_text = font.render(f"Speed: {self.speed:.1f}", True, BLACK)
        screen.blit(speed_text, (20, 80))
        
        # Draw game over
        if self.game_over:
            over_text = game_over_font.render("GAME OVER", True, BLACK)
            restart_text = font.render("Press SPACE to restart", True, BLACK)
            screen.blit(over_text, (SCREEN_WIDTH//2 - over_text.get_width()//2, 150))
            screen.blit(restart_text, (SCREEN_WIDTH//2 - restart_text.get_width()//2, 200))

# Create the game
game = Game()

# Modified game loop for Pygbag compatibility
async def main():
    # Game loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if game.game_over:
                        game.reset()
                    else:
                        game.trex.jump()
                elif event.key == pygame.K_DOWN:
                    game.trex.duck()
                elif event.key == pygame.K_a:
                    # Toggle auto mode
                    game.auto_mode = not game.auto_mode
        
        # Check for key releases
        keys = pygame.key.get_pressed()
        if not keys[pygame.K_DOWN] and not game.auto_mode:
            game.trex.stand()
        
        # Update game state
        game.update()
        
        # Draw everything
        game.draw()
        
        # Update display
        pygame.display.flip()
        
        # Control game speed
        clock.tick(FPS)
        
        # Required for pygbag
        await asyncio.sleep(0)

# Run the game
if __name__ == "__main__":
    asyncio.run(main())