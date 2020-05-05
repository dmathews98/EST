'''
Determine planewave cutoff energy
'''

import sys
import numpy as np
import matplotlib.pyplot as plt

def shift_en(totale, numatoms):
    for i in range(len(totale)):
        totale[i] = (totale[i] - totale[len(totale)-1])/numatoms # per atom in UC

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

    ecut = data[:,0]

    shifte = shift_en(data[:,1], float(numatoms)) *(13.6/1e-3)

    tenmev = 10e-3/13.6
    onemev = tenmev/10.0

    tencut = find_point(shifte, 10)
    onecut = find_point(shifte, 1)

    print('10meV cut is ' + str(ecut[tencut]))
    print('1meV cut is ' + str(ecut[onecut]))

    plt.figure(1)
    plt.plot(ecut, shifte, 'b')
    plt.hlines(0, ecut[0], ecut[len(ecut)-1], color='r')
    plt.vlines([ecut[tencut]], shifte[0], -shifte[0], color='black', label='10meV cutoff')
    plt.vlines([ecut[onecut]], shifte[0], -shifte[0], color='grey', label='1meV cutoff')
    plt.ylim([min([0, min(shifte)]), max(shifte)])
    plt.xlim([min(ecut),max(ecut)])
    # plt.title('Diff from GS energy vs plane wave cut off energy')
    plt.xlabel('Plane wave cut off energy /Ry')
    plt.ylabel('Difference in GS energy per atom from true value /meV')
    plt.legend(loc='upper right')

    plt.show()
