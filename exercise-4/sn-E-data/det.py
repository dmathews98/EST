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

def shift_a(totale):
    for i in range(len(totale)):
        totale[i] = (totale[i] - totale[len(totale)-1])/8.0 # per atom in diamond UC

    return totale

def shift_b(totale):
    for i in range(len(totale)):
        totale[i] = (totale[i] - totale[len(totale)-1])/4.0 # per atom in beta body centred tetragonal UC

    return totale

def find_point(shifte, val):
    for i in range(len(shifte)):
        if shifte[i] <= val:
            return i

def diff(totale_a, totale_b):
    ediff = []
    for i in range(len(totale_a)):
        totale_a[i] = totale_a[i]/8.0
        totale_b[i] = totale_b[i]/4.0
        ediff.append(totale_b[i]-totale_a[i]) # b - a as beta a more stable (lower in e therefore makes diff positive)

    return ediff

def main():
    file = 'alpha-sn.txt'
    ecut_a, totale_a, time_a = read_in(file)
    file = 'beta-sn.txt'
    ecut_b, totale_b, time_b = read_in(file)

    # shift to change in energy per formula unit
    shifte_a = shift_a(totale_a)
    shifte_b = shift_b(totale_b)

    # cutoff values in Ry
    tenmev = 10e-3/13.6
    fivemev = tenmev/2.0
    onemev = tenmev/10.0

    # find cuttoff index
    fivecut_a = find_point(shifte_a, fivemev)
    fivecut_b = find_point(shifte_b, fivemev)

    print('5meV cut for alpha tin is ' + str(ecut_a[fivecut_a]))
    print('5meV cut for beta tin is ' + str(ecut_b[fivecut_b]))

    plt.figure(1)
    plt.plot(ecut_a, shifte_a, 'b')
    plt.hlines(0, ecut_a[0], ecut_a[len(ecut_a)-1], color='r')
    plt.vlines([ecut_a[fivecut_a]], shifte_a[0], -shifte_a[0], color='black', label='5meV cutoff')
    #plt.ylim([-0.005, 0.005])
    #plt.xlim([100,200])
    plt.title('Diff from GS energy vs plane wave cut off energy for alpha tin')
    plt.xlabel('Plane wave cut off energy /Ry')
    plt.ylabel('Difference in GS energy per atom from true value /Ry')
    plt.legend(loc='upper left')

    plt.figure(2)
    plt.plot(ecut_b, shifte_b, 'b')
    plt.hlines(0, ecut_b[0], ecut_b[len(ecut_b)-1], color='r')
    plt.vlines([ecut_b[fivecut_b]], shifte_b[0], -shifte_b[0], color='black', label='5meV cutoff')
    #plt.ylim([-0.005, 0.005])
    #plt.xlim([100,200])
    plt.title('Diff from GS energy vs plane wave cut off energy for beta tin')
    plt.xlabel('Plane wave cut off energy /Ry')
    plt.ylabel('Difference in GS energy per atom from true value /Ry')
    plt.legend(loc='upper left')

    ediff = diff(totale_a, totale_b)
    onecut_diff = find_point(ediff, onemev)

    print('1meV cut for the difference in alpha and beta tin is ' + str(ecut_a[onecut_diff]))

    plt.figure(3)
    plt.plot(ecut_a, ediff, 'b')
    plt.hlines(0, ecut_a[0], ecut_a[len(ecut_b)-1], color='r')
    plt.vlines([ecut_a[onecut_diff]], ediff[0], -ediff[0], color='black', label='1meV cutoff')
    #plt.ylim([-0.005, 0.005])
    #plt.xlim([100,200])
    plt.title('Diff in GS energy of beta minus alpha tin vs plane wave cut off energy')
    plt.xlabel('Plane wave cut off energy /Ry')
    plt.ylabel('Difference in GS energy of beta minus alpha tin per atom /Ry')
    plt.legend(loc='upper left')

    plt.show()

main()
