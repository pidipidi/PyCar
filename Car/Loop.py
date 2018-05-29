from Startup import*
from Car import*
from Road import*
import pickle, os
import numpy as np
import random

vehicle  = Car(250, random.choice([height/2+40, height/2-20]))
road     = Road()
vehicle1 = Car(width/2+100, height/2+40)
#obstacle2 = Car(width/2-100, height/2-20)


def display_all(main_surface, display_list, text_list):
    main_surface.fill((0, 100, 100))
    for element in display_list:
        element.display(main_surface)
    for element_val in range(0, len(text_list)):
        main_surface.blit(font.render(str(text_list[element_val]), True, (0, 255, 0)), (10, 10 + (10 * element_val)))


def update_all(update_list):
    for element in update_list:
        element.update()


data = {'pose':[], 'vehicle':[], 'solid_line':[], 'dash_line':[]}

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            None

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        vehicle.left = True
    if key[pygame.K_RIGHT]:
        vehicle.right = True
    if key[pygame.K_UP]:
        vehicle.forward = True
    if key[pygame.K_DOWN]:
        vehicle.backward = True
    if key[pygame.K_r]:
        if len(data['pose'])>10:
            mypath = './'
            onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
            max_count = 0
            for f in onlyfiles:
                if 'pkl' not in f: continue
                count = int(f.split("_")[1].split(".")[0])
                if max_count < count: max_count = count
            pickle.dump( data, open( "save_"+str(max_count+1)+".pkl", "wb" ) )
            data = {'pose':[], 'vehicle':[], 'solid_line':[], 'dash_line':[]}
            print "Saved a pickle: save_"+str(max_count+1)+".pkl"

        vehicle  = Car(250, random.choice([height/2+40, height/2-20]))
        vehicle1 = Car(width/2+random.randint(-100,100), random.choice([height/2+40, height/2-20]))


    to_update = [vehicle]
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

    update_all(to_update)
    display_all(main_s, to_display, to_text)
    pygame.display.flip()


    data['pose'].append([vehicle.rect.x, vehicle.rect.y, vehicle.angle])
    data['vehicle'].append([vehicle1.rect.x-vehicle.rect.x,
                            vehicle1.rect.y-vehicle.rect.y,
                            vehicle1.angle-vehicle.angle])
    data['solid_line'] += road.relative_pose_from_solid_line(vehicle.rect.x, vehicle.rect.y, vehicle.angle)
    data['dash_line'].append(road.relative_pose_from_dash_line(vehicle.rect.x, vehicle.rect.y, vehicle.angle))
    
    ## data.append([vehicle.rect.x, vehicle.rect.y, vehicle.angle])
