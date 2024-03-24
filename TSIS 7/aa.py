import pygame
import os

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Music Player")

# Set up fonts
font = pygame.font.SysFont(None, 36)

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up music directory


# Set up current song index
current_song_index = 0

# Load the first song

# Function to play the current song
def play_song():
    pygame.mixer.music.play()

# Function to stop the current song
def stop_song():
    pygame.mixer.music.stop()

# Function to play the next song

# Function to play the previous song
 
# Main loop
running = True
while running:
    screen.fill(WHITE)
    text = font.render("Press SPACE to play, S to stop, N for next song, P for previous song", True, BLACK)
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play_song()
            elif event.key == pygame.K_s:
                stop_song()
            elif event.key == pygame.K_n:
                next_song()
            elif event.key == pygame.K_p:
                previous_song()

# Quit Pygame
pygame.quit()
