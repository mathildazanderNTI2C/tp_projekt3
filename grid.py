#kod för att skapa rutnätet med cellerna

import pygame
from colors import Colors  # Importera Colors-klassen från filen colors.py

class Grid:
    def __init__(self):
        # Konstruktor för Grid-klassen.
        # Sätter upp standardvärden för rutnätet.
        self.num_rows = 20  # Antal rader i rutnätet
        self.num_cols = 10  # Antal kolumner i rutnätet
        self.cell_size = 30  # Storleken på varje rutcell
        # Skapa ett rutnät som är en tvådimensionell lista med 0 som standardvärde för varje cell
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        # Hämta färgerna för rutcellerna från Colors-klassen
        self.colors = Colors.get_cell_colors()

    def print_grid(self):
        # Metod för att skriva ut rutnätet till konsolen
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end=" ")  # Skriv ut värdet för varje cell
            print()

    def is_inside(self, row, column):
        # Metod för att kontrollera om en position är inom rutnätets gränser
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        return False

    def is_empty(self, row, column):
        # Metod för att kontrollera om en cell är tom (har värdet 0)
        if self.grid[row][column] == 0:
            return True
        return False

    def is_row_full(self, row):
        # Metod för att kontrollera om en hel rad är full (alla celler är fyllda)
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True

    def clear_row(self, row):
        # Metod för att rensa en hel rad (sätta alla cellers värde till 0)
        for column in range(self.num_cols):
            self.grid[row][column] = 0

    def move_row_down(self, row, num_rows):
        # Metod för att flytta en rad nedåt i rutnätet
        for column in range(self.num_cols):
            self.grid[row + num_rows][column] = self.grid[row][column]  # Flytta cellerna nedåt
            self.grid[row][column] = 0  # Töm de ursprungliga cellerna

    def clear_full_rows(self):
        # Metod för att rensa alla fulla rader i rutnätet
        completed = 0  # Räknare för antalet rensade rader
        for row in range(self.num_rows - 1, 0, -1):  # Loopa genom rutnätet från botten till toppen
            if self.is_row_full(row):  # Om en rad är full
                self.clear_row(row)  # Rensa raden
                completed += 1  # Öka räknaren för rensade rader
            elif completed > 0:  # Om några rader har rensats tidigare
                self.move_row_down(row, completed)  # Flytta ned övre rader
        return completed  # Returnera antalet rensade rader

    def reset(self):
        # Metod för att återställa rutnätet till sitt ursprungliga tillstånd (alla celler har värdet 0)
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0

    def draw(self, screen):
        # Metod för att rita rutnätet på skärmen med hjälp av Pygame
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]  # Hämta värdet för cellen
                # Skapa en rektangel för cellen baserat på dess position och storlek
                cell_rect = pygame.Rect(column * self.cell_size + 11, row * self.cell_size + 11,
                                         self.cell_size - 1, self.cell_size - 1)
                # Rita en fylld rektangel för cellen med den motsvarande färgen från Colors-klassen
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
