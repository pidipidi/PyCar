from Startup import*
from Car import*
from Road import*
import pickle, os
import numpy as np
import random

vehicle  = Car(250, random.choice([height/2+40, height/2-20]))
road     = Road()
vehicle1 = Car(width/2+100, height/2+40)


def display_all(main_surface, display_list, text_list):
    main_surface.fill((0, 100, 100))
    for element in display_list:
        element.display(main_surface)
    for element_val in range(0, len(text_list)):
        main_surface.blit(font.render(str(text_list[element_val]), True, (0, 255, 0)), (10, 10 + (10 * element_val)))


def update_all(update_list):
    for element in update_list:
        element.update()


# make a plan
traj = np.array([np.random.normal(1,1.0,550),
                 np.random.normal(0,1.0,550)])
## traj = np.array([np.linspace(1.0, 1.0, 550),
##                  np.linspace(0, 0, 550)])

for i in xrange(len(traj[0])):
    clock.tick(60)

    ## to_update = [vehicle]
    to_display = [road, vehicle, vehicle1]
    to_text = [clock.get_fps(),
               vehicle.x,
               vehicle.y,
               vehicle.theta,
               vehicle.uv,
               vehicle.ua]

    vehicle.move(u=(traj[0][i], traj[1][i]))
    display_all(main_s, to_display, to_text)
    pygame.display.flip()
    print i

