from __future__ import division
import sys
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # I/O

    # q_range = np.arange(5, 15, 2)
    # k_range = np.arange(5, 15, 2)

    q_range = [5, 8, 9, 10, 11, 12, 14]
    k_range = [5, 8, 9, 10, 11, 12, 13, 14]

    colours = ['red', 'blue', 'green', 'yellow', 'orange', 'cyan', 'purple', 'maroon']


    plt.figure(1)
    for q in range(len(q_range)):
        data = np.loadtxt('mat-data/si.ph-dos-'+str(q_range[q])+'-13-data.dat')
        data[:,0] = data[:,0] * 0.02998
        labelq = 'Nq='+str(q_range[q])
        plt.plot(data[:,0], data[:,1], color=colours[q], label=labelq, linewidth=0.6)

    plt.legend(loc='best')
    plt.xlim([0, max(data[:,0])])
    plt.ylim([0, max(data[:,1])])
    plt.xlabel('Frequency (THZ)')
    plt.ylabel('DOS')
    plt.yticks([])
    plt.title('DOS for varying DFPT grid')

    plt.figure(2)
    for k in range(len(k_range)):
        data = np.loadtxt('mat-data/si.ph-dos-11-'+str(k_range[k])+'-data.dat')
        data[:,0] = data[:,0] * 0.02998
        labelk = 'Nk='+str(k_range[k])
        plt.plot(data[:,0], data[:,1], color=colours[k], label=labelk, linewidth=0.6)

    plt.legend(loc='best')
    plt.xlim([0, max(data[:,0])])
    plt.ylim([0, max(data[:,1])])
    plt.xlabel('Frequency (THZ)')
    plt.ylabel('DOS')
    plt.yticks([])
    plt.title('DOS for varying post-processing grid')

    plt.show()
