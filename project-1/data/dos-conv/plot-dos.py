'''
Plots DOS shifted Ef to 0
'''

import sys
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # I/O

    if len(sys.argv) != 2:
        print('Usage: file')
        quit()
    else:
        [prog, file] = sys.argv

    data = np.loadtxt(file)

    f = open(file)
    line = f.readline()
    parts = line.split()

    Ef = float(parts[len(parts)-2])

    print('Ef = '+str(Ef)+' eV')

    data[:,0] = data[:,0] - Ef

    plt.plot(data[:,0], data[:,1], 'b', label=r'$N_k=8$')
    plt.xlabel('State Energy (eV)')
    plt.ylabel('Density of States (States /eV)')

    plt.vlines(0, 0, max(data[:,1])+0.1*max(data[:,1]), 'r', label=r'$E_f$')

    plt.xlim([min(data[:,0]), max(data[:,0])])
    plt.ylim([0, max(data[:,1])+0.1*max(data[:,1])])

    plt.legend(loc='best')

    plt.show()
