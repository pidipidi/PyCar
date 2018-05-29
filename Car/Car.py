from Startup import*


class Car:
    def __init__(self, x, y):
        self.body = pygame.image.load("Images//Body//Grey.png")
        self.wheels = pygame.image.load("Images//Wheels//Black.png")
        self.rect = self.body.get_rect()
        self.rect.x = x #200 #width/2
        self.rect.y = y #height/2
        self.rect.center = self.rect.x, self.rect.y
        self.coord_x = float(self.rect.x)
        self.coord_y = float(self.rect.y)

        # movement
        self.forward  = False
        self.backward = False
        self.left  = False
        self.right = False
        self.angle = 90.0

        self.turn_speed = 1.0 #0.5
        self.top_speed = 1.0 #6
        self.acceleration = 0.05 #0.2
        self.deceleration = 0.05 #0.1
        self.current_speed = 0
        self.move_x = 0
        self.move_y = 0

    def reset_data(self):
        self.left = False
        self.right = False
        self.forward = False
        self.backward = False

    def rotate(self):
        if self.angle > 360:
            self.angle = 0
        else:
            if self.angle < 0:
                self.angle = 360.0
        if self.left:
            self.angle += self.turn_speed * self.current_speed
        if self.right:
            self.angle -= self.turn_speed * self.current_speed

    def move(self):
        if self.forward:
            if self.current_speed < self.top_speed:
                self.current_speed += self.acceleration
        else:
            if self.current_speed > 0:
                self.current_speed -= self.deceleration
            else:
                self.current_speed = 0

        angle_rad = deg_to_rad(self.angle)
        self.move_x = -(float(self.current_speed * math.sin(angle_rad)))
        self.move_y = -(float(self.current_speed * math.cos(angle_rad)))
        self.coord_x -= self.move_x
        self.coord_y -= self.move_y
        self.rect.x = int(self.coord_x)
        self.rect.y = int(self.coord_y)
        

    def display(self, main_surface):
        temp_image = pygame.transform.rotate(self.body, self.angle)
        main_surface.blit(temp_image, (self.rect.x, self.rect.y))
        temp_image = pygame.transform.rotate(self.wheels, self.angle)
        main_surface.blit(temp_image, (self.rect.x, self.rect.y))

    def update(self):
        self.move_x = 0
        self.move_y = 0
        self.move()
        self.rotate()
        self.reset_data()
