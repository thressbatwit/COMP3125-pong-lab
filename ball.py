import pygame

class Ball:
    #pass
    radius = 10

    def __init__(self, x, y, vx, vy, screen, fgcolor, bgcolor):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.screen = screen
        self.fgcolor = fgcolor
        self.bgcolor = bgcolor
    
    def show(self, color):
        pygame.draw.circle(self.screen, color, (self.x, self.y), self.radius)
    
    def update(self):
        self.show(self.bgcolor)

        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.show(self.fgcolor)

        if(self.x < 30):
            self.vx = self.vx * -1
        
        if(self.y < 30):
            self.vy = self.vy * -1

        if(self.y > 420):
            self.vy = self.vy * -1