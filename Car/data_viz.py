import numpy as np
import os, sys
import pickle
import matplotlib
import matplotlib.pyplot as plt

us            = []
xs            = []
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

def plot_ind(data):
    fig = plt.figure(figsize=(6,6))
    for i in xrange(3):
        fig.add_subplot(3,1,i+1)
        length = len(data)
        plt.plot(np.array(data)[int(0.03*length):,i])
    plt.show()
    

mypath = './'
onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
for f in onlyfiles:
    if 'pkl' not in f: continue
    d = pickle.load( open(f, "rb"))
    if 'x' not in d.keys(): continue
    us.append(d['u'])
    xs.append(d['x'])
    vehicle_poses.append(d['vehicle'])
    solid_line_poses.append(d['solid_line'])
    dash_line_poses.append(d['dash_line'])
    
## plot(xs)

#sys.exit()
new_xs = []
from pydtw import dtw1d
for i in xrange(1,len(xs)):
    x_ref = np.array(xs[0])
    x     = np.array(xs[i])
    _, idx1, idx2 = dtw1d(x_ref[:,0].copy(order='C'),
                          x[:,0].copy(order='C'))
    
    l = []
    for j in xrange(len(xs[0][-1])):
        l.append(x[idx2,j])
    new_xs.append(l)

## x1 = []
## x2 = []
## for i,j in zip(alignmend_a, alignmend_b):
##     x1.append(a[i])
##     x2.append(b[j])
print np.shape(new_xs)


# Get 3D covariance figures
fig = plt.figure(figsize=(6,6))
fig.add_subplot(1,1,1)
plt.plot(new_xs[:,:,0], 'k-')
#plt.plot(new_xs[:,:,0], 'r-')
## plt.plot(x1, 'k--')
## plt.plot(x2, 'r--')
plt.show()





## idx = np.linspace(0,np.pi*2,100)
## a = np.cos(idx)
## b = np.concatenate((np.sin(idx), np.random.uniform(0,0.1,100)))
## cost_matrix, alignmend_a, alignmend_b = dtw1d(a, b)

## import rpy2.robjects as robjects
## r = robjects.r
## r('library("dtw")')
## idx = r.seq(0,6.28,len=100)
## template = r.cos(idx)
## query = r.sin(idx)+r('runif(100)/10')
## alignment=r.dtw(query,template,keep=r('TRUE'))
## robjects.globalenv["alignment"] =  alignment
## dist = r('alignment$distance')
## print(dist)

## index1 = r('alignment$index1')
## index2 = r('alignment$index2')

## import rpy2.robjects.numpy2ri as rpyn
## template=np.asarray(template)
## query=np.asarray(query)
## print np.shape(template), np.shape(query)
## print np.shape(index1), np.shape(index2)

