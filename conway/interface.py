import pygame

class Button:
    def __init__(self, x, y, width, height, text, font, color, text_color, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.color = color
        self.text_color = text_color
        self.action = action  # Fonction à appeler lorsque le bouton est cliqué

    def draw(self, screen):
        # Dessiner le bouton
        pygame.draw.rect(screen, self.color, self.rect)
        # Dessiner le texte
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.action:
                    self.action()  # Appeler l'action associée

class Slider:
    def __init__(self, x, y, width, min_val, max_val, start_val, label, font, handle_color=(100, 100, 100), line_color=(200, 200, 200)):
        self.rect = pygame.Rect(x, y, width, 20)
        self.min_val = min_val
        self.max_val = max_val
        self.value = start_val
        self.label = label
        self.font = font
        self.handle_color = handle_color
        self.line_color = line_color

        # Position du handle
        self.handle_radius = 10
        self.handle_x = self.get_handle_pos()
        self.handle_y = y + self.rect.height // 2

        self.dragging = False

    def get_handle_pos(self):
        # Calculer la position du handle en fonction de la valeur
        ratio = (self.value - self.min_val) / (self.max_val - self.min_val)
        return self.rect.x + int(ratio * self.rect.width)

    def draw(self, screen):
        # Dessiner la ligne du slider
        pygame.draw.line(screen, self.line_color, (self.rect.x, self.handle_y), (self.rect.x + self.rect.width, self.handle_y), 4)
        # Dessiner le handle
        pygame.draw.circle(screen, self.handle_color, (self.handle_x, self.handle_y), self.handle_radius)
        # Dessiner le label et la valeur
        label_surface = self.font.render(f"{self.label}: {self.value}", True, (255, 255, 255))
        screen.blit(label_surface, (self.rect.x, self.rect.y - 25))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_over_handle(event.pos):
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                self.update_value(event.pos[0])

    def is_over_handle(self, pos):
        dx = pos[0] - self.handle_x
        dy = pos[1] - self.handle_y
        return dx * dx + dy * dy <= self.handle_radius * self.handle_radius

    def update_value(self, mouse_x):
        # Limiter la position du handle à la ligne du slider
        mouse_x = max(self.rect.x, min(mouse_x, self.rect.x + self.rect.width))
        self.handle_x = mouse_x
        # Calculer la valeur en fonction de la position du handle
        ratio = (self.handle_x - self.rect.x) / self.rect.width
        self.value = int(self.min_val + ratio * (self.max_val - self.min_val))

    def get_value(self):
        return self.value