class tic_tac:
    def __init__(self, kind, pos):
        self.kind = kind
        
        self.pos = pos
        
    def draw(self, surface, font):
        color = (200, 50, 50) if self.kind == "x" else (50, 50, 200)
        text = font.render(self.kind, True, color)
        
        rect = text.get_rect(center=self.pos)
        surface.blit(text, rect)