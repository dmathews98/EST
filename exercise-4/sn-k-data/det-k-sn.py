'''
Determines cutoff points
'''

import numpy as np
import matplotlib.pyplot as plt

def read_in(file):
    k = []
    totale = []
    kused = []
    f = open(file)
    for line in f.readlines():
        vals = line.split()
        k.append(float(vals[0]))
        totale.append(float(vals[1]))
        kused.append(float(vals[2]))
    f.close()

    return k, totale, kused

def shift_a(totale):
    for i in range(len(totale)):
        totale[i] = (totale[i] - totale[len(totale)-1])/8.0 # per atom in diamond UC

    return totale

def shift_b(totale):
    for i in range(len(totale)):
        totale[i] = (totale[i] - totale[len(totale)-1])/2.0 # per atom in beta body centred tetragonal UC

    return totale

def find_point(shifte, val):
    for i in range(6, len(shifte)):
        if shifte[i] <= val:
            return i

def main():
    file = 'alpha-sn-k.txt'
    k_a, totale_a, kused_a = read_in(file)

    file = 'beta-sn-k.txt'
    k_b, totale_b, kused_b = read_in(file)

    # shift to change in energy per formula unit
    shifte_a = shift_a(totale_a)
    shifte_b = shift_b(totale_b)

    # cutoff values in Ry
    tenmev = 10e-3/13.6
    mev = tenmev/10.0

    # find cuttoff index
    onecut_a = find_point(shifte_a, mev)
    onecut_b = find_point(shifte_b, mev)

    print('1meV kpoint cut for alpha is at N = ' + str(k_a[onecut_a]))
    print('1meV kpoint cut for beta is at N = ' + str(k_b[onecut_b]))

    plt.figure(1)
    plt.plot(k_a, shifte_a, 'b')
    plt.hlines(0, k_a[0], k_a[len(k_a)-1], color='r')
    plt.vlines(k_a[onecut_a], shifte_a[0], -shifte_a[0], color='black', label='1meV cutoff')
    #plt.ylim([-0.0005, 0.005])
    #plt.xlim([40,200])
    plt.title('Diff from true GS energy vs kpoint grid N N N for alpha tin')
    plt.xlabel('N')
    plt.ylabel('Difference in GS energy per atom from true value /Ry')
    plt.legend(loc='upper left')

    plt.figure(2)
    plt.plot(k_b, shifte_b, 'b')
    plt.hlines(0, k_b[0], k_b[len(k_b)-1], color='r')
    plt.vlines(k_b[onecut_b], shifte_b[0], -shifte_b[0], color='black', label='1meV cutoff')
    #plt.ylim([-0.0005, 0.005])
    #plt.xlim([40,200])
    plt.title('Diff from true GS energy vs kpoint grid N N N for beta tin')
    plt.xlabel('N')
    plt.ylabel('Difference in GS energy per atom from true value /Ry')
    plt.legend(loc='upper left')

    plt.show()


main()
