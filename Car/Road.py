from Startup import*


class Road:
    def __init__(self, n_line=2):
        self.background = pygame.image.load("Images//Road//background.png")
        self.solid_line = pygame.image.load("Images//Road//solid_line.png")
        self.dash_line  = pygame.image.load("Images//Road//dash_line.png")
        
        self.rect   = self.background.get_rect()
        self.rect.x = width/2
        self.rect.y = height/2
        self.rect.center = self.rect.x, self.rect.y

        self.angle = 0

    def reset_data(self):
        print

    def relative_pose_from_solid_line(self, x, y, ang):
        d = []
        d.append([0, self.rect.y-y, 90.-ang])
        d.append([0, self.rect.y+130-y, 90.-ang])
        return d

    def relative_pose_from_dash_line(self, x, y, ang):
        return [0, self.rect.y+60-y, 90.-ang]
    

    def display(self, main_surface):
        temp_image = pygame.transform.rotate(self.background, self.angle)
        main_surface.blit(temp_image, (self.rect.x, self.rect.y))

        temp_image = pygame.transform.rotate(self.dash_line, self.angle)
        main_surface.blit(temp_image, (self.rect.x, self.rect.y+60))

        temp_image = pygame.transform.rotate(self.solid_line, self.angle)
        main_surface.blit(temp_image, (self.rect.x, self.rect.y))

        temp_image = pygame.transform.rotate(self.solid_line, self.angle)
        main_surface.blit(temp_image, (self.rect.x, self.rect.y+130))


    def update(self):
        self.reset_data()
