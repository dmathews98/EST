'''
Determine planewave cutoff energy
'''

import numpy as np
import matplotlib.pyplot as plt

def read_in(file):
    xvals = [] # ecut /Ry
    yvals = [] # E /Ry
    f = open(file, 'r')
    for line in f.readlines():
        vals  = line.split(' ')
        xvals.append(float(vals[0]))
        yvals.append(float(vals[1]))
    f.close()

    xvals = np.array(xvals)
    yvals = np.array(yvals)

    return xvals, yvals

def shift_en(totale):
    for i in range(len(totale)):
        totale[i] = (totale[i] - totale[len(totale)-1])/8.0 # per atom in diamond UC

    return totale

def find_point(shifte, val):
    for i in range(len(shifte)):
        if shifte[i] <= val:
            return i

def main():
    file = 'si-data-E.txt'
    ecut, totale = read_in(file)

    shifte = shift_en(totale)

    tenmev = 10e-3/13.6
    onemev = tenmev/10.0

    tencut = find_point(shifte, tenmev)
    onecut = find_point(shifte, onemev)

    print('10meV cut for Si is ' + str(ecut[tencut]))
    print('1meV cut for Si is ' + str(ecut[onecut]))

    plt.figure(1)
    plt.plot(ecut, shifte, 'b')
    plt.hlines(0, ecut[0], ecut[len(ecut)-1], color='r')
    plt.vlines([ecut[tencut], ecut[onecut]], shifte[0], -shifte[0], color='black', label='10meV and 1meV cutoffs (left to right)')
    #plt.ylim([-0.005, 0.005])
    #plt.xlim([100,200])
    plt.title('Diff from GS energy vs plane wave cut off energy for Si')
    plt.xlabel('Plane wave cut off energy /Ry')
    plt.ylabel('Difference in GS energy per atom from true value /Ry')
    plt.legend(loc='upper right')

    plt.show()

main()
