import pygame, sys  # Importerar pygame och sys-modulerna
from game import Game  # Importerar Game-klassen från game-modulen
from colors import Colors  # Importerar färger från colors-modulen

pygame.init()  # Initierar pygame-biblioteket

# Skapar ett fönster med bredd 500 och höjd 620
screen = pygame.display.set_mode((500, 620)) #x, y koordinater
# Sätter titeln på fönstret
pygame.display.set_caption("Huvudmeny")

# Skapar en fontobjekt med storlek 30 för titeln
text_styling = pygame.font.Font(None, 30)
# Skapar texten "poäng" med vit färg och ingen styling 
poang_knapp = text_styling.render("POÄNG", True, Colors.white)
# Renderar texten "Nästa" med den angivna fonten och färgen 
nasta_knapp = text_styling.render("NÄSTA", True, Colors.white)
# Renderar texten "ny omgång" med den angivna fonten och färgen 
game_over_text = text_styling.render("Ny omgång", True, Colors.white)
# Renderar restarttexten med den angivna fonten och färgen
restart_surface = text_styling.render("Restart", True, Colors.white)

# Skapar en rektangel för poängen (x, y, bredd, höjd)
score_rect = pygame.Rect(320, 55, 170, 60)
# Skapar en rektangel för nästa figur (x, y, bredd, höjd)
next_rect = pygame.Rect(320, 215, 170, 180)
# Skapar en rektangel för restarttexten (x, y, bredd, höjd)
restart_rect = pygame.Rect(100, 50, 170, 60)

# Skapar en klocka för att styra uppdateringshastigheten
clock = pygame.time.Clock()

# Skapar ett Game-objekt
game = Game()

# Skapar ett anpassat användarevenemang för att uppdatera spelet
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

# test kod
# Definiera konstanter
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 620
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
mainMenuState = True
def draw_menu():
	screen.fill(WHITE)
	font = pygame.font.SysFont(None, 36)
	text = font.render("Press SPACE to Start", True, BLACK)
	text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
	screen.blit(text, text_rect)
	pygame.display.flip()

# Huvudloop
while True:
	# Hanterar alla pygame-händelser
	for event in pygame.event.get():
		if event.type == pygame.QUIT:  # Om fönstret stängs av
			pygame.quit()  # Stänger pygame
			sys.exit()  # Avslutar programmet
		if event.type == pygame.KEYDOWN:  # Om en tangent trycks ned
			if game.game_over == True:  # Om spelet är över
				game.game_over = False  # Återställer spelet
				game.reset()

			if event.key == pygame.K_LEFT and game.game_over == False:  # Om vänsterpil trycks ned
				game.move_left()  # Flyttar blocket åt vänster
			if event.key == pygame.K_RIGHT and game.game_over == False:  # Om högerpil trycks ned
				game.move_right()  # Flyttar blocket åt höger
			if event.key == pygame.K_DOWN and game.game_over == False:  # Om nedåtpil trycks ned
				game.move_down()  # Flyttar blocket nedåt
				game.update_score(0, 1)  # Uppdaterar poängen
			if event.key == pygame.K_UP and game.game_over == False:  # Om uppåtpil trycks ned
				game.rotate()  # Roterar blocket
		if event.type == GAME_UPDATE and game.game_over == False:  # Om det anpassade uppdateringsevenemanget utlöses
			game.move_down()  # Flyttar blocket nedåt

	# Rendering
	score_value_surface = text_styling.render(str(game.score), True, Colors.white)  # Renderar poängen

	# Fyller skärmen med rosa färg
	screen.fill(Colors.pink)
	# Ritar poängytan på skärmen
	screen.blit(poang_knapp, (365, 20, 50, 50))
	# Ritar ytan för nästa figur på skärmen
	screen.blit(nasta_knapp, (375, 180, 50, 50))
	# Ritar restarttexten på skärmen
	screen.blit(restart_surface, (100, 50, 50, 50))

	# Om spelet är över, ritar "GAME OVER"-texten på skärmen
	if game.game_over == True:
		screen.blit(game_over_text, (320, 450, 50, 50))

	# Ritar en grå rektangel för poängen
	pygame.draw.rect(screen, Colors.grey, score_rect, 0, 10)
	# Ritar poängytan på skärmen centralt i rektangeln
	screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))
	# Ritar en grå rektangel för nästa figur
	pygame.draw.rect(screen, Colors.grey, next_rect, 0, 10)
	# Ritar spelet på skärmen
	game.draw(screen)
	# Uppdaterar skärmen
	pygame.display.update()
	# Ställer in uppdateringshastigheten till 60 fps
	clock.tick(60)

