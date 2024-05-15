import pygame
import sys
from colors import Colors

pygame.init()

class MainMenu:
    def __init__(self):
        pass
    
    def show(self):
        print("Huvudmenyn visas")  # Utskrift för att kontrollera om metoden anropas korrekt
        # Implementera kod för att visa huvudmenyn

class SettingsMenu:
    def __init__(self):
        pass
    
    def show(self):
        print("Inställningsmenyn visas")  # Utskrift för att kontrollera om metoden anropas korrekt
        # Implementera kod för att visa inställningsmenyn

# Skapa en klass för huvudmenyn
class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)

    def show(self):
        self.screen.fill(Colors.white)
        text = self.font.render("Main Menu - tryck på mellanslag", True, Colors.black)
        text_rect = text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()

# klass för inställningsmenyn
class SettingsMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)

    def show(self):
        self.screen.fill(Colors.white)
        text = self.font.render("Settings Menu - Press ESC to Go Back", True, Colors.black)
        text_rect = text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
