import pygame
from assets.scripts.characters.spaceship import spaceship

# Init
pygame.init()

SCREENWIDTH = 1000
SCREENHEIGHT = 700

surface = pygame.display.set_mode(((SCREENWIDTH, SCREENHEIGHT)))

pygame.display.set_caption('Red Planet')
player = spaceship(pygame.image.load(r'./assets/images/characters/player.png'), 50, 50, SCREENWIDTH, SCREENHEIGHT)

running = True

y1s1 = 0
y2s1 = -1*SCREENHEIGHT
y1s2 = 0
y2s2 = -1*SCREENHEIGHT
y1s3 = 0
y2s3 = -1*SCREENHEIGHT

def setBackground(width : int, height : int) -> None:
	# To set the background to a 'tiled' version of the background, also to make it move

	global y1s1
	global y2s1
	global y1s2
	global y2s2
	global y1s3
	global y2s3

	y1s1 += 5
	y2s1 += 5
	y1s2 += 3
	y2s2 += 3
	y1s3 += 1
	y2s3 += 1

	for x in range(0, width, 500):
		surface.blit(pygame.image.load(r'./assets/images/background/background.png'), (x,0))
		surface.blit(pygame.image.load(r'./assets/images/background/stars1.png'), (x,y1s1))
		surface.blit(pygame.image.load(r'./assets/images/background/stars1.png'), (x,y2s1))
		surface.blit(pygame.image.load(r'./assets/images/background/stars2.png'), (x,y1s2))
		surface.blit(pygame.image.load(r'./assets/images/background/stars2.png'), (x,y2s2))
		surface.blit(pygame.image.load(r'./assets/images/background/stars3.png'), (x,y1s3))
		surface.blit(pygame.image.load(r'./assets/images/background/stars3.png'), (x,y2s3))

	if y1s1 > height:
		y1s1 = -1*height
	if y2s1 > height:
		y2s1 = -1*height
	if y1s2 > height:
		y1s2 = -1*height
	if y2s2 > height:
		y2s2 = -1*height
	if y1s3 > height:
		y1s3 = -1*height
	if y2s3 > height:
		y2s3 = -1*height

# Init Variables
BLACK = (0, 0, 0)
FPS = 30
ACCELERATION = 12
ROTATION = 10
clock = pygame.time.Clock()

# All movestates
moveState = {
	'left' : False,
	'right' : False,
	'up' : False
}

# Game loop
while running:
	# Updating frames
	setBackground(SCREENWIDTH, SCREENHEIGHT)
	player.draw(surface)

	# Movements
	if moveState['left'] == True:
		player.rotate(ROTATION)
	if moveState['right'] == True:
		player.rotate(-1*ROTATION)
	if moveState['up'] == True:
		player.move(ACCELERATION)

	# Shooting
	if player.shootState == True:
		player.shoot(surface)

	# Check for keypress
	for event in pygame.event.get():
		# Check if user quit
		if event.type == pygame.QUIT:
			running = False

		# Check for user keypresses
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				moveState['up'] = True
			if event.key == pygame.K_RIGHT:
				moveState['right'] = True
			if event.key == pygame.K_LEFT:
				moveState['left'] = True

			if event.key == pygame.K_SPACE:
				player.shoot(surface)

		# Remove movements when key no longer pressed
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				moveState['up'] = False
			if event.key == pygame.K_LEFT:
				moveState['left'] = False
			if event.key == pygame.K_RIGHT:
				moveState['right'] = False

	# Updates
	pygame.display.flip()
	clock.tick(FPS)