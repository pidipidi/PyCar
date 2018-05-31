from Startup import*


class Car:
    def __init__(self, x, y):
        self.body = pygame.image.load("Images//Body//Grey.png")
        self.wheels = pygame.image.load("Images//Wheels//Black.png")
        self.rect = self.body.get_rect()
        self.rect.x = x #200 #width/2
        self.rect.y = y #height/2
        self.rect.center = self.rect.x, self.rect.y
        self.x     = float(self.rect.x)
        self.y     = float(self.rect.y)
        self.theta = 0.0
        self.uv = 0
        self.ua = 0

        # movement
        self.forward  = False
        self.backward = False
        self.left  = False
        self.right = False

        self.turn_speed = 1.0 #0.5
        self.top_speed = 1.0 #6
        self.acceleration = 0.05 #0.2
        self.deceleration = 0.05 #0.1
        self.current_speed = 0

    def reset_data(self):
        self.left = False
        self.right = False
        self.forward = False
        self.backward = False

    def move(self, u=None):
        if u is None:
            if self.forward:
                if self.current_speed < self.top_speed:
                    self.current_speed += self.acceleration
            else:
                if self.current_speed > 0:
                    self.current_speed -= self.deceleration
                else:
                    self.current_speed = 0

            if self.left:
                self.turn_speed = abs(self.turn_speed)
                self.ua = self.turn_speed * self.current_speed
            elif self.right:
                self.turn_speed = -abs(self.turn_speed)
                self.ua = self.turn_speed * self.current_speed
            else:
                self.ua = 0

            self.uv = self.current_speed
        else:
            self.uv = u[0]
            self.ua = u[1]

        angle_rad = deg_to_rad(self.theta)        
        self.dx     = float(self.uv * math.cos(angle_rad))
        self.dy     = -float(self.uv * math.sin(angle_rad))
        self.dTheta = float(self.ua)

        self.x     += self.dx
        self.y     += self.dy
        self.theta += self.dTheta

        if self.theta > 180:
            self.theta = -180
        else:
            if self.theta < -180:
                self.theta = 180.0


    def display(self, main_surface):
        temp_image = pygame.transform.rotate(self.body, self.theta+90)
        main_surface.blit(temp_image, (int(self.x), int(self.y)))
        temp_image = pygame.transform.rotate(self.wheels, self.theta+90)
        main_surface.blit(temp_image, (int(self.x), int(self.y)))


    def update(self):
        self.move()
        self.reset_data()
