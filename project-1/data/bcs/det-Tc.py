'''
Plots Tc reuslts
'''

import sys
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # I/O

    if len(sys.argv) != 1:
        print('Usage:')
        quit()
    else:
        [prog] = sys.argv

    mu_vals = [10, 13, 20]
    k_vals = [6, 7, 8, 9]

    degauss = np.arange(0.020, 0.601, 0.020)

    Tc_data = []

    for i in range(len(mu_vals)):
        for j in range(len(k_vals)):
            file = 'Tc-data/Tc-mu'+str(mu_vals[i])+'-k'+str(k_vals[j])+'.txt'
            Tc = np.loadtxt(file)
            Tc_data.append(Tc)

    Tc_data = np.transpose(Tc_data)

    f, (ax1, ax2, ax3) = plt.subplots(1,3, sharey=True)

    ax1.plot(degauss, Tc_data[:,0], 'r', label=r'$N_q=6$')
    ax1.plot(degauss, Tc_data[:,1], 'b', label=r'$N_q=7$')
    ax1.plot(degauss, Tc_data[:,2], 'g', label=r'$N_q=8$')
    ax1.plot(degauss, Tc_data[:,3], 'y', label=r'$N_q=9$')

    ax1.set_title(r'$\mu^*=0.10$')

    ax2.plot(degauss, Tc_data[:,4], 'r', label=r'$N_q=6$')
    ax2.plot(degauss, Tc_data[:,5], 'b', label=r'$N_q=7$')
    ax2.plot(degauss, Tc_data[:,6], 'g', label=r'$N_q=8$')
    ax2.plot(degauss, Tc_data[:,7], 'y', label=r'$N_q=9$')

    ax2.set_title(r'$\mu^*=0.13$')

    ax3.plot(degauss, Tc_data[:,8], 'r', label=r'$N_q=6$')
    ax3.plot(degauss, Tc_data[:,9], 'b', label=r'$N_q=7$')
    ax3.plot(degauss, Tc_data[:,10], 'g', label=r'$N_q=8$')
    ax3.plot(degauss, Tc_data[:,11], 'y', label=r'$N_q=9$')

    ax3.set_title(r'$\mu^*=0.20$')

    ax2.set_xlabel('Degauss (Ry)')
    ax1.set_ylabel('Tc (K)')
    ax3.legend(loc='best')

    plt.show()
