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

def shift_e(totale):
    for i in range(len(totale)):
        totale[i] = (totale[i] - totale[len(totale)-1])/9.0 # e per atom -3 fu and 3atom per fu

    return totale

def find_point(shifte, val):
    for i in range(len(shifte)):
        if shifte[i] <= val:
            return i

def main():
    file = 'quartz-us-k.txt'
    k_us, totale_us, kused_us = read_in(file)

    # shift to change in energy per formula unit
    shifte_us = shift_e(totale_us)

    # cutoff values in Ry
    tenmev = 10e-3/13.6
    mev = tenmev/10.0

    # find cuttoff index
    onecut_us = find_point(shifte_us, mev)

    print('1meV kpoint cut for us is at N = ' + str(k_us[onecut_us]))

    plt.figure(1)
    plt.plot(k_us, shifte_us, 'b')
    plt.hlines(0, k_us[0], k_us[len(k_us)-1], color='r')
    plt.vlines(k_us[onecut_us], shifte_us[0], -shifte_us[0], color='black', label='1meV cutoff')
    plt.ylim([-0.0005, 0.005])
    #plt.xlim([40,200])
    plt.title('Diff from true GS energy vs kpoint grid N N N for US')
    plt.xlabel('N')
    plt.ylabel('Difference in GS energy per atom from true value /Ry')
    plt.legend(loc='upper left')

    plt.show()


main()
