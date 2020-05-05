'''
Plot phonon bands and dos in required format
'''

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import lmfit

def linear_fit(x, m, b):
    return (x*m + b)

def get_sound_speed(k, band, colour):
    k_near_0 = k[0:11]
    wavenum_near_0 = band[0:11]

    b0 = 0.0
    m0 = 1000.0

    model = lmfit.Model(linear_fit)
    parameters = model.make_params(m=m0, b=b0)

    result = model.fit(wavenum_near_0, x=k_near_0, params=parameters)

    a = 10.2 * 5.29177e-11   # m
    k_unit = (2.0*np.pi/a)
    omega_unit = 2.0*np.pi*0.02998e12

    c = result.params['m'].value * (omega_unit/k_unit)

    print('Speed of sound for ' + str(colour) + ' line is ' + str(c) + ' m/s\n')

def main():
    dosfile = 'si-ph-dos-test.dat'
    bandfile = 'si-ph-disp-test.gp'

    dos_data = np.loadtxt(dosfile)
    band_data = np.loadtxt(bandfile)

    '''
    Via Bilbao crystallography

    0.000  0.000  0.000  50   Gamma
    0.500  0.000  0.500  50   X
    0.500  0.250  0.750  50   W
    0.375  0.375  0.750  50   Sigma
    0.000  0.000  0.000  50   Gamma
    0.500  0.500  0.500  50   L
    '''

    get_sound_speed(band_data[:,0], band_data[:,1], 'red')
    get_sound_speed(band_data[:,0], band_data[:,2], 'blue')
    get_sound_speed(band_data[:,0], band_data[:,3], 'green')

    point_names = ['$\Gamma$', 'X', 'W', '$\Sigma$', '$\Gamma$', 'L']
    band_points = band_data[::50,0][:len(point_names)]

    f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
    f.suptitle('Si Phonon Band Structure and Density of States')
    ax1.set_ylim([0, 550])
    ax1.set_xlim([band_data[0][0], band_data[len(band_data)-1][0]])
    ax2.set_xlim([dos_data[0][0], max(dos_data[:,1])])

    ax1.plot(band_data[:,0], band_data[:,1], 'r')
    ax1.plot(band_data[:,0], band_data[:,2], 'b')
    ax1.plot(band_data[:,0], band_data[:,3], 'g')
    ax1.plot(band_data[:,0], band_data[:,4], 'y')
    ax1.plot(band_data[:,0], band_data[:,5], 'orange')
    ax1.plot(band_data[:,0], band_data[:,6], 'purple')
    ax2.plot(dos_data[:,1], dos_data[:,0], color='black', linewidth=1.0)
    #ax2.plot(dos_data[:,2], dos_data[:,0], linewidth=0.3, color='green', label='Integrated DOS')
    ax1.vlines(band_points,0,550,color='grey',linestyle='dotted')
    # ax1.hlines(EFermi, 0, 20, color='red', linestyle='solid', label='Fermi Level')
    # ax2.hlines(EFermi, 0, 40, color='red', linestyle='solid', label='Fermi Level')
    ax1.set_xticks(band_points)
    ax1.set_xticklabels(point_names)
    ax2.set_xticks([])
    ax1.set_ylabel(r'Wavenumber ($cm^{-1}$)')
    # ax1.set_xlabel(r'$|\vec{k}|$')
    ax2.set_xlabel('Density of States')
    # ax2.legend()

    plt.show()

main()
