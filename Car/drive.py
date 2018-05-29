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
traj = np.array([np.linspace(vehicle.rect.x, 750, 200),
                 np.linspace(vehicle.rect.y, vehicle.rect.y, 200),
                 np.linspace(vehicle.angle, vehicle.angle, 200)]).T
print np.shape(traj)

for i in xrange(len(traj)):
    clock.tick(60)

    vehicle.rect.x = traj[i][0]
    vehicle.rect.y = traj[i][1]
    vehicle.angle  = traj[i][2]

    ## to_update = [vehicle]
    to_display = [road, vehicle, vehicle1]
    to_text = [clock.get_fps(),
               vehicle.angle,
               vehicle.current_speed,
               vehicle.move_x,
               vehicle.move_y,
               vehicle.rect.x,
               vehicle.rect.y,
               "F " + str(vehicle.forward),
               "L " + str(vehicle.left),
               "R " + str(vehicle.right)]

    ## update_all(to_update)
    display_all(main_s, to_display, to_text)
    pygame.display.flip()

