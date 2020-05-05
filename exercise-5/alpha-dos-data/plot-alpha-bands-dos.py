'''
Plot bands and dos in required format
'''

import numpy as np
import matplotlib.pyplot as plt

def main():
    dosfile = 'alpha_dos_tet_k15.dat'
    bandfile = 'alpha-sn-bands.dat.gnu'

    f = open(dosfile)
    line = f.readline()
    vals = line.split()
    EFermi = [float(vals[len(vals)-2])]

    dos_data = np.loadtxt(dosfile)
    band_data = np.loadtxt(bandfile)

    point_names = ['$\Gamma$', 'X', 'W', 'K', '$\Gamma$', 'L']
    band_points = band_data[::50,0][:len(point_names)]

    f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
    f.suptitle('Alpha Band Structure and Density of States')
    ax1.set_ylim([-4, 20])
    ax1.set_xlim([band_points[0],band_points[len(band_points)-1]])
    ax2.set_xlim(0,2.5)

    ax1.plot(band_data[:,0], band_data[:,1], '.', markersize=0.4)
    ax2.plot(dos_data[:,1], dos_data[:,0], color='green', linewidth=1.0)
    #ax2.plot(dos_data[:,2], dos_data[:,0], linewidth=0.3, color='green', label='Integrated DOS')
    ax1.vlines(band_points,-20,40,color='grey',linestyle='dotted')
    ax1.hlines(EFermi, 0, 20, color='red', linestyle='solid', label='Fermi Level')
    ax2.hlines(EFermi, 0, 40, color='red', linestyle='solid', label='Fermi Level')
    ax1.set_xticks(band_points)
    ax1.set_xticklabels(
    point_names)
    ax2.set_xticks([])
    ax1.set_ylabel('Energy (eV)')
    ax1.set_xlabel('Point in first Brillouin Zone')
    ax2.set_xlabel('Density of States')
    ax2.legend()

    plt.show()

main()
