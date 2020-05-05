'''
Determines cutoff points
'''

import sys
import numpy as np
import matplotlib.pyplot as plt

def shift_e(totale, numatoms):
    for i in range(len(totale)):
        totale[i] = (totale[i] - totale[len(totale)-1])/numatoms # E per atom

    return totale

def find_point(shifte, val):
    for i in range(len(shifte)):
        if abs(shifte[i]) <= val:
            return i

if __name__ == "__main__":
    # I/O

    if len(sys.argv) != 3:
        print('Usage: file numatoms_inUC')
        quit()
    else:
        [prog, file, numatoms] = sys.argv

    data = np.loadtxt(str(file))

    k_pts = data[:,0]

    # shift to change in energy per formula unit
    shifte = shift_e(data[:,1], float(numatoms)) *(13.6/1e-3)

    # cutoff values in Ry
    tenmev = 10e-3/13.6
    mev = tenmev/10.0

    # find cuttoff index
    tencut = find_point(shifte, 10)
    onecut = find_point(shifte, 1)

    print('10meV kpoint cut is at Nk = ' + str(k_pts[tencut]))
    print('1meV kpoint cut is at Nk = ' + str(k_pts[onecut]))

    plt.figure(1)
    plt.plot(k_pts, shifte, 'b')
    plt.hlines(0, k_pts[0], k_pts[len(k_pts)-1], color='r')
    plt.vlines(k_pts[tencut], shifte[0], -shifte[0], color='black', label='10meV cutoff')
    plt.vlines(k_pts[onecut], shifte[0], -shifte[0], color='grey', label='1meV cutoff')
    plt.ylim([-50, 50])
    plt.xlim([min(k_pts),max(k_pts)])
    # plt.title('Diff from true GS energy vs kpoint grid N N N for US')
    plt.xlabel(r'$N_k$')
    plt.ylabel('Difference in GS energy per atom from true value /meV')
    plt.legend(loc='best')

    plt.show()
