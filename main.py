import pygame
from constants import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	
	while True:
		pygame.Surface.fill(screen, (0, 0, 0, 1))
		pygame.display.flip()
		
		# check for window close, end process if closed
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
					return

if __name__ == "__main__":
	main()