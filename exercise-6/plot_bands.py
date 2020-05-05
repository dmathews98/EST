from __future__ import division
import sys
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # I/O

    file14 = 'mat-data/si.ph-disp-14-13-data.gp'
    file4 = 'mat-data/si.ph-disp-5-13-data.gp'

    band_data_14 = np.loadtxt(file14)
    band_data_5 = np.loadtxt(file4)

    point_names = ['$\Gamma$', 'X', 'W', 'K', '$\Gamma$', 'L']
    band_points = band_data_14[::50,0][:len(point_names)]

    for i in range(1, 6):
        band_data_5[:,i] = band_data_5[:,i] * 0.02998
        band_data_14[:,i] = band_data_14[:,i] * 0.02998

    fig, ax = plt.subplots(1)
    fig.suptitle('Phonon Dispersion for different DFPT grid sizes')
    ax.plot(band_data_14[:,0], band_data_14[:,1], 'r', label='Nq=14', linewidth=0.7)
    ax.plot(band_data_5[:,0], band_data_5[:,1], 'b', label='Nq=5', linewidth=0.7)
    for i in range(2, 6):
        ax.plot(band_data_14[:,0], band_data_14[:,i], 'r', linewidth=0.7)
        ax.plot(band_data_5[:,0], band_data_5[:,i], 'b', linewidth=0.7)

    ax.set_ylim([0, max(band_data_14[:,5])+3])
    ax.set_xlim([band_data_14[0][0], band_data_14[len(band_data_14)-1][0]])
    ax.set_xticks(band_points)
    ax.set_xticklabels(point_names)
    ax.set_ylabel(r'Frequency (THz)')
    ax.legend(loc='best')

    plt.show()
