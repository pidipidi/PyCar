import numpy as np
import os, sys
import pickle
import matplotlib
import matplotlib.pyplot as plt

poses            = []
vehicle_poses    = []
solid_line_poses = []
dash_line_poses  = []

def plot(data):
    fig = plt.figure(figsize=(6,6))
    for i in xrange(3):
        fig.add_subplot(3,1,i+1)
        for j in xrange(len(data)):
            length = len(data[j])
            plt.plot(np.array(data[j])[int(0.03*length):,i])
            ## plt.plot(np.array(data[j])[int(0.05*length):int(0.95*length),i])
    plt.show()

mypath = './'
onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
for f in onlyfiles:
    if 'pkl' not in f: continue
    d = pickle.load( open(f, "rb"))
    if 'pose' not in d.keys(): continue
    poses.append(d['pose'])
    vehicle_poses.append(d['vehicle'])
    solid_line_poses.append(d['solid_line'])
    dash_line_poses.append(d['dash_line'])
    
plot(vehicle_poses)
    
