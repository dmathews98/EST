from __future__ import division
import sys
import numpy as np
import matplotlib.pyplot as plt

def get_dos_diff(x,y):
    dos_diff = abs(x[:,1]- y[:,1])

    return dos_diff

if __name__ == "__main__":
    # I/O

    data_q14k14 = np.loadtxt('mat-data/si.ph-dos-14-14-data.dat')
    data_q14k14 = data_q14k14[:,1]

    q_range = np.arange(5, 15, 1)
    k_range = np.arange(5, 15, 1)

    difference_data = np.empty((len(q_range), len(k_range)))

    for q in range(len(q_range)):
        for k in range(len(k_range)):
            data = np.loadtxt('mat-data/si.ph-dos-'+str(q_range[q])+'-'+str(k_range[k])+'-data.dat')
            difference = data_q14k14 - data[:,1]#[0:len(data_q14k14)]
            difference_data[q][k] = np.linalg.norm(difference)

    f, ax = plt.subplots(1,1)
    img = ax.imshow(difference_data[::-1,:])
    f.suptitle('Difference in DOS (States /Energy /Unit Cell)\nfrom Nq and Nk = 14 for varing Nq and Nk')
    ax.set_xlabel('Nk')
    ax.set_xticks(np.arange(0, 10, 1))
    ax.set_xticklabels(['5', '6', '7', '8', '9', '10', '11', '12', '13', '14'])
    ax.set_ylabel('Nq')
    ax.set_yticks(np.arange(0, 10, 1))
    ax.set_yticklabels(['14', '13', '12', '11', '10', '9', '8', '7', '6', '5'])
    f.colorbar(img)
    plt.show()
