import pygame

width = 1024
height = 640
display_scale = 2
display_ratio = (16, 10)


class Display:
    def __init__(self):
        pygame.display.init()
        self.window = pygame.display.set_mode(
            (width * display_scale, height * display_scale))
        pygame.display.set_caption("Cool Guy")
        pygame.mouse.set_visible(False)
        pygame.display.set_icon(pygame.image.load("img/icon.png"))

    def refresh(self):
        pygame.display.flip()

    def handle_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()

        return True

    def fill_screen(self, color):
        self.window.fill(color)

    def blit(self, component, x, y, w, h):
        r = pygame.rect.Rect(x, y, w, h)
        component = pygame.transform.scale(component, (w, h))
        self.window.blit(component, r)
