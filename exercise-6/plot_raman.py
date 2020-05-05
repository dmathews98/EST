from __future__ import division
import sys
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # I/O

    file11 = 'mat-data/si.ph-disp-11-13-data.gp'
    file_r = 'mat-data/raman_data.txt'

    disp = np.loadtxt(file11)
    raman = np.loadtxt(file_r)

    point_names = ['$\Gamma$', 'X', 'W', 'K', '$\Gamma$', 'L']
    band_points = disp[::50,0][:len(point_names)]

    for i in range(1, 6):
        disp[:,i] = disp[:,i] * 0.02998
    raman[:,0] = raman[:,0] * 0.02998

    f, (ax1, ax2) = plt.subplots(1, 2, sharey=True, gridspec_kw={'width_ratios': [3, 1]})
    f.suptitle('Si Phonon Dispersion and Raman Spectroscopy Experimental Data')
    ax1.set_ylim([0, max(disp[:,5])+3])
    ax1.set_xlim([disp[0][0], disp[len(disp)-1][0]])
    ax2.set_xlim([raman[0][0], 5000])

    for i in range(1,6):
        ax1.plot(disp[:,0], disp[:,i], 'b', linewidth=0.8)

    ax2.plot(raman[:,1], raman[:,0], 'r', linewidth=0.8)

    ax1.vlines(band_points,0,550,color='grey',linestyle='dotted')
    ax1.set_xticks(band_points)
    ax1.set_xticklabels(point_names)
    ax1.set_ylabel(r'Frequency (THz)')
    ax2.set_xlabel('Intensity')

    plt.show()
