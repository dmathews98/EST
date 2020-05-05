'''
Plot phonon bands and dos in required format
'''

from __future__ import division
import sys
import numpy as np
import matplotlib.pyplot as plt
import lmfit

def linear_fit(x, m, b):
    return (x*m + b)

def get_sound_speed(k, band, colour):
    k_near_0 = k[0:9]
    wavenum_near_0 = band[0:9]

    b0 = 0.0
    m0 = 1000.0

    model = lmfit.Model(linear_fit)
    parameters = model.make_params(m=m0, b=b0)

    result = model.fit(wavenum_near_0, x=k_near_0, params=parameters)

    a = 10.2 * 5.29177e-11   # m
    k_unit = (1/a)
    omega_unit = 1e12

    c = result.params['m'].value * (omega_unit/k_unit)

    print('Speed of sound for ' + str(colour) + ' line is ' + str(c) + ' m/s\n')

if __name__ == "__main__":
    # I/O

    if len(sys.argv) != 3:
        print('Usage: dosfile bandfile')
        quit()
    else:
        [file, dosfile, bandfile] = sys.argv
    # dosfile = 'si-ph-dos-test.dat'
    # bandfile = 'si-ph-disp-test.gp'

    dos_data = np.loadtxt(str(dosfile))
    band_data = np.loadtxt(str(bandfile))

    # convert to THz
    band1 = band_data[:,1] * 0.02998
    band2 = band_data[:,2] * 0.02998
    band3 = band_data[:,3] * 0.02998
    band4 = band_data[:,4] * 0.02998
    band5 = band_data[:,5] * 0.02998
    band6 = band_data[:,6] * 0.02998

    dos_data[:,0] = dos_data[:,0] * 0.02998

    point_names = ['$\Gamma$', 'X', 'W', 'K', '$\Gamma$', 'L']
    band_points = band_data[::50,0][:len(point_names)]

    # Experimental data

    exp_e00_la_1 = np.loadtxt('exp-data/exp-e00-la-1.txt')
    # exp_e00_la_2 = np.loadtxt('exp-data/exp-e00-la-2.txt')
    exp_e00_lo = np.loadtxt('exp-data/exp-e00-lo.txt')
    exp_e00_to = np.loadtxt('exp-data/exp-e00-to.txt')

    exp_ee0_s1_1 = np.loadtxt('exp-data/exp-ee0-s1-1.txt')
    exp_ee0_s1_1[:,0] = band_points[len(band_points)-2] - exp_ee0_s1_1[:,0]*2**(1.0/2.0)
    exp_ee0_s1_2 = np.loadtxt('exp-data/exp-ee0-s1-2.txt')
    exp_ee0_s1_2[:,0] = band_points[len(band_points)-2] - exp_ee0_s1_2[:,0]*2**(1.0/2.0)
    exp_ee0_s3_1 = np.loadtxt('exp-data/exp-ee0-s3-1.txt')
    exp_ee0_s3_1[:,0] = band_points[len(band_points)-2] - exp_ee0_s3_1[:,0]*2**(1.0/2.0)
    exp_ee0_s3_2 = np.loadtxt('exp-data/exp-ee0-s3-2.txt')
    exp_ee0_s3_2[:,0] = band_points[len(band_points)-2] - exp_ee0_s3_2[:,0]*2**(1.0/2.0)

    exp_eee_la= np.loadtxt('exp-data/exp-eee-la.txt')
    exp_eee_la[:,0] = band_points[len(band_points)-2] + exp_eee_la[:,0]*3**(1.0/2.0)
    exp_eee_lo= np.loadtxt('exp-data/exp-eee-lo.txt')
    exp_eee_lo[:,0] = band_points[len(band_points)-2] + exp_eee_lo[:,0]*3**(1.0/2.0)
    exp_eee_to= np.loadtxt('exp-data/exp-eee-to.txt')
    exp_eee_to[:,0] = band_points[len(band_points)-2] + exp_eee_to[:,0]*3**(1.0/2.0)

    '''
    Via Bilbao crystallography

    0.000  0.000  0.000  50   Gamma
    0.500  0.000  0.500  50   X
    0.500  0.250  0.750  50   W
    0.375  0.375  0.750  50   K
    0.000  0.000  0.000  50   Gamma
    0.500  0.500  0.500  50   L
    '''

    get_sound_speed(band_data[:,0], band1, 'red')
    get_sound_speed(band_data[:,0], band2, 'blue')
    get_sound_speed(band_data[:,0], band3, 'green')

    f, (ax1, ax2) = plt.subplots(1, 2, sharey=True, gridspec_kw={'width_ratios': [3, 1]})
    f.suptitle('Si Phonon Dispersion and Density of States')
    ax1.set_ylim([0, max(band6)+3])
    ax1.set_xlim([band_data[0][0], band_data[len(band_data)-1][0]])
    ax2.set_xlim([dos_data[0][0], max(dos_data[:,1])])

    ax1.plot(band_data[:,0], band1, 'r', linewidth='0.8')
    ax1.plot(band_data[:,0], band2, 'b', linewidth='0.8')
    ax1.plot(band_data[:,0], band3, 'g', linewidth='0.8')
    ax1.plot(band_data[:,0], band4, 'y', linewidth='0.8')
    ax1.plot(band_data[:,0], band5, 'orange', linewidth='0.8')
    ax1.plot(band_data[:,0], band6, 'purple', linewidth='0.8')

    ax1.plot(exp_e00_la_1[:,0], exp_e00_la_1[:,1], '.', color='black', label='Kulda et al', markersize=4.0)
    # ax1.plot(exp_e00_la_2[:,0], exp_e00_la_2[:,1], '.', color='black')
    ax1.plot(exp_e00_lo[:,0], exp_e00_lo[:,1], '.', color='black', markersize=4.0)
    ax1.plot(exp_e00_to[:,0], exp_e00_to[:,1], '.', color='black', markersize=4.0)

    ax1.plot(exp_ee0_s1_1[:,0], exp_ee0_s1_1[:,1], '.', color='black', markersize=4.0)
    ax1.plot(exp_ee0_s1_2[:,0], exp_ee0_s1_2[:,1], '.', color='black', markersize=4.0)
    ax1.plot(exp_ee0_s3_1[:,0], exp_ee0_s3_1[:,1], '.', color='black', markersize=4.0)
    ax1.plot(exp_ee0_s3_2[:,0], exp_ee0_s3_2[:,1], '.', color='black', markersize=4.0)

    ax1.plot(exp_eee_la[:,0], exp_eee_la[:,1], '.', color='black', markersize=4.0)
    ax1.plot(exp_eee_lo[:,0], exp_eee_lo[:,1], '.', color='black', markersize=4.0)
    ax1.plot(exp_eee_to[:,0], exp_eee_to[:,1], '.', color='black', markersize=4.0)

    ax2.fill(dos_data[:,1], dos_data[:,0], color='black', linewidth=1.0)
    #ax2.plot(dos_data[:,2], dos_data[:,0], linewidth=0.3, color='green', label='Integrated DOS')
    ax1.vlines(band_points,0,550,color='grey',linestyle='dotted')
    # ax1.hlines(EFermi, 0, 20, color='red', linestyle='solid', label='Fermi Level')
    # ax2.hlines(EFermi, 0, 40, color='red', linestyle='solid', label='Fermi Level')
    ax1.set_xticks(band_points)
    ax1.set_xticklabels(point_names)
    ax2.set_xticks([])
    ax1.set_ylabel(r'Frequency (THz)')
    # ax1.set_xlabel(r'$|\vec{k}|$')
    ax2.set_xlabel('Density of States')
    ax1.legend(loc='best')

    plt.show()
