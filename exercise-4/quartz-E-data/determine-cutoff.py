'''
Determines cutoff points
'''

import numpy as np
import matplotlib.pyplot as plt

def read_in(file):
    ecut = []
    totale = []
    time = []
    f = open(file)
    for line in f.readlines():
        vals = line.split()
        ecut.append(float(vals[0]))
        totale.append(float(vals[1]))
        time.append(float(vals[2]))
    f.close()

    return ecut, totale, time

def shift_e(totale):
    for i in range(len(totale)):
        totale[i] = (totale[i] - totale[len(totale)-1])/3.0 # per formula unit

    return totale

def find_point(shifte, val):
    for i in range(3,len(shifte)):
        if shifte[i] <= val:
            return i

def main():
    file = 'quartz-mt.txt'
    ecut_mt, totale_mt, time_mt = read_in(file)
    file = 'quartz-us.txt'
    ecut_us, totale_us, time_us = read_in(file)

    # shift to change in energy per formula unit
    shifte_mt = shift_e(totale_mt)
    shifte_us = shift_e(totale_us)

    # cutoff values in Ry
    tenmev = 10e-3/13.6
    mev = tenmev/10.0

    # find cuttoff index
    tencut_mt = find_point(shifte_mt, tenmev)
    onecut_mt = find_point(shifte_mt, mev)

    print('10meV cut for mt is ' + str(ecut_mt[tencut_mt]))
    print('1meV cut for mt is ' + str(ecut_mt[onecut_mt]))

    plt.figure(1)
    plt.plot(ecut_mt, shifte_mt, 'b')
    plt.hlines(0, ecut_mt[0], ecut_mt[len(ecut_mt)-1], color='r')
    plt.vlines([ecut_mt[tencut_mt], ecut_mt[onecut_mt]], shifte_mt[0], -shifte_mt[0], color='black', label='10meV and 1meV cutoffs (left to right)')
    #plt.ylim([-0.005, 0.005])
    #plt.xlim([100,200])
    plt.title('Diff from true GS energy vs plane wave cut off energy for MT')
    plt.xlabel('Plane wave cut off energy /Ry')
    plt.ylabel('Difference in GS energy per formula unit from true value /Ry')
    plt.legend(loc='upper left')

    tencut_us = find_point(shifte_us, tenmev)
    onecut_us = find_point(shifte_us, mev)

    print('10meV cut for us is ' + str(ecut_us[tencut_us]))
    print('1meV cut for us is ' + str(ecut_us[onecut_us]))

    plt.figure(2)
    plt.plot(ecut_us, shifte_us, 'b')
    plt.hlines(0, ecut_us[0], ecut_us[len(ecut_us)-1], color='r')
    plt.vlines([ecut_us[tencut_us], ecut_us[onecut_us]], shifte_us[0], -shifte_us[0], color='black', label='10meV and 1meV cutoffs (left to right)')
    #plt.ylim([-0.005, 0.005])
    #plt.xlim([40,200])
    plt.title('Diff from true GS energy vs plane wave cut off energy for US')
    plt.xlabel('Plane wave cut off energy /Ry')
    plt.ylabel('Difference in GS energy per formula unit from true value /Ry')
    plt.legend(loc='upper left')

    plt.figure(3)
    plt.plot(ecut_mt, time_mt, 'b')
    plt.plot(ecut_us, time_us, 'r')
    plt.vlines([ecut_mt[tencut_mt], ecut_mt[onecut_mt]], 15, 0, color='black', label='MT cutoffs')
    plt.vlines([ecut_us[tencut_us], ecut_us[onecut_us]], 15, 0, color='green', label='US cutoffs')
    plt.ylim([0,14])
    plt.title('CPU time vs cutoff energy')
    plt.xlabel('Plane wave cut off energy /Ry')
    plt.ylabel('CPU time for calculation /s')
    plt.legend(['MT time', 'US time', 'MT cutoffs', 'US cutoffs'], loc='upper left')

    plt.show()


main()
