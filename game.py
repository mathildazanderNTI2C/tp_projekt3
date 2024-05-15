#hanterar spelet (flytta rotera block)
from grid import Grid  # Importera Grid-klassen från filen grid.py
from blocks import *  # Importera alla blockklasser från filen blocks.py
import random

class Game:
	def __init__(self):
		self.grid = Grid()
		self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
		self.current_block = self.get_random_block()
		self.next_block = self.get_random_block()
		self.game_over = False
		self.score = 0

	def update_score(self, lines_cleared, move_down_points):
		# Metod för att uppdatera spelarens poäng baserat på antalet rader som raderats och poängen för att flytta ned blocket
		if lines_cleared == 1:
			self.score += 100
		elif lines_cleared == 2:
			self.score += 300
		elif lines_cleared == 3:
			self.score += 500
		# Lägg till poäng för att flytta ned blocket
		self.score += move_down_points

	def get_random_block(self):
		# Metod för att välja en slumpmässig blocktyp från listan och returnera den
		if len(self.blocks) == 0:
			self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
		block = random.choice(self.blocks)
		self.blocks.remove(block)
		return block

	def move_left(self):
		# Metod för att flytta det nuvarande blocket åt vänster
		self.current_block.move(0, -1)
		# Kontrollera om blocket är inom rutnätets gränser eller om det kolliderar med andra block
		if self.block_inside() == False or self.block_fits() == False:
			self.current_block.move(0, 1)  # Ångra föregående drag om blocket är utanför eller kolliderar

	def move_right(self):
		# Metod för att flytta det nuvarande blocket åt höger
		self.current_block.move(0, 1)
		# Kontrollera om blocket är inom rutnätets gränser eller om det kolliderar med andra block
		if self.block_inside() == False or self.block_fits() == False:
			self.current_block.move(0, -1)  # Ångra föregående drag om blocket är utanför eller kolliderar

	def move_down(self):
		# Metod för att flytta det nuvarande blocket nedåt
		self.current_block.move(1, 0)
		# Kontrollera om blocket är inom rutnätets gränser eller om det kolliderar med andra block
		if self.block_inside() == False or self.block_fits() == False:
			self.current_block.move(-1, 0)  # Ångra föregående drag om blocket är utanför eller kolliderar
			self.lock_block()  # Lås blocket om det inte längre kan flyttas nedåt

	def lock_block(self):
		# Metod för att låsa det nuvarande blocket på sin plats i rutnätet
		tiles = self.current_block.get_cell_positions()  # Hämta blockets cellpositioner
		for position in tiles:
			# Uppdatera rutnätet med blockets ID vid varje cellposition
			self.grid.grid[position.row][position.column] = self.current_block.id
		# Byt det nuvarande blocket mot nästa block och välj ett nytt nästa block
		self.current_block = self.next_block
		self.next_block = self.get_random_block()
		# Rensa fullständiga rader i rutnätet och uppdatera poängen
		rows_cleared = self.grid.clear_full_rows()
		if rows_cleared > 0:
			self.update_score(rows_cleared, 0)
			# Kontrollera om det nya blocket passar i rutnätet, annars är spelet över
		if self.block_fits() == False:
			self.game_over = True

	def reset(self):
		# Metod för att återställa spelet till dess ursprungliga tillstånd
		self.grid.reset()  # Återställ rutnätet
		self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]  # Återställ blocklistan
		self.current_block = self.get_random_block()  # Välj ett nytt nuvarande block
		self.next_block = self.get_random_block()  # Välj ett nytt nästa block
		self.score = 0  # Återställ poängen

	def block_fits(self):
		# Metod för att kontrollera om det nuvarande blocket passar i rutnätet utan att kollidera med andra block
		tiles = self.current_block.get_cell_positions()
		for tile in tiles:
			if self.grid.is_empty(tile.row, tile.column) == False:
				return False  # Returnera False om det finns en kollision
		return True  # Returnera True om blocket passar

	def rotate(self):
		# Metod för att rotera det nuvarande blocket
		self.current_block.rotate()
		# Kontrollera om det roterade blocket är inom rutnätets gränser eller om det kolliderar med andra block
		if self.block_inside() == False or self.block_fits() == False:
			self.current_block.undo_rotation()  # Ångra rotationen om blocket är utanför eller kolliderar

	def block_inside(self):
		# Metod för att kontrollera om det nuvarande blocket är inom rutnätets gränser
		tiles = self.current_block.get_cell_positions()
		for tile in tiles:
			if self.grid.is_inside(tile.row, tile.column) == False:
				return False  # Returnera False om en cell är utanför rutnätet
		return True  # Returnera True om alla celler är inom rutnätet

	def draw(self, screen):
		# Metod för att rita rutnätet och det nuvarande och nästa blocket på skärmen
		self.grid.draw(screen)  # Rita rutnätet
		self.current_block.draw(screen, 11, 11)  # Rita det nuvarande blocket

		# Rita nästa block på en specifik position beroende på dess typ
		if self.next_block.id == 3:
			self.next_block.draw(screen, 255, 290)
		elif self.next_block.id == 4:
			self.next_block.draw(screen, 255, 280)
		else:
			self.next_block.draw(screen, 270, 270)

	def check_collision(self, row_offset, col_offset):
		# Metod för att kontrollera kollision med andra block
		tiles = self.current_block.get_cell_positions(offset_row=row_offset, offset_col=col_offset)
		for tile in tiles:
			if not self.grid.is_empty(tile.row, tile.column) or not self.grid.is_inside(tile.row, tile.column):
				return True  # Returnera True om det finns en kollision eller om blocket är utanför rutnätet
		return False  # Returnera False om ingen kollision har upptäckts