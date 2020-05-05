from __future__ import division
import sys
import numpy as np
import matplotlib.pyplot as plt

def get_band_diff(x, y):
    band_diff = abs(x[:,1] - y[:,1])
    band_diff += abs(x[:,2] - y[:,2])
    band_diff += abs(x[:,3] - y[:,3])
    band_diff += abs(x[:,4] - y[:,4])
    band_diff += abs(x[:,5] - y[:,5])

    return band_diff/6.0

if __name__ == "__main__":
    # I/O

    files = ['data/si.ph-disp-4-10-data.gp',
             'data/si.ph-disp-5-10-data.gp',
             'data/si.ph-disp-6-10-data.gp',
             'data/si.ph-disp-7-10-data.gp',
             'data/si.ph-disp-8-10-data.gp',
             'data/si.ph-disp-9-10-data.gp',
             'data/si.ph-disp-10-10-data.gp',
             'data/si.ph-disp-11-10-data.gp',
             'data/si.ph-disp-12-10-data.gp',
             'data/si.ph-disp-13-10-data.gp',
             'data/si.ph-disp-14-10-data.gp',
             'data/si.ph-disp-15-10-data.gp']

    band_data_1 = np.loadtxt(str(files[0]))
    for i in range(1,6):
        band_data_1[:,i] = band_data_1[:,i] * 0.02998

    band_data_2 = np.loadtxt(str(files[1]))
    for i in range(1,6):
        band_data_2[:,i] = band_data_2[:,i] * 0.02998

    band_data_3 = np.loadtxt(str(files[2]))
    for i in range(1,6):
        band_data_3[:,i] = band_data_3[:,i] * 0.02998

    band_data_4 = np.loadtxt(str(files[3]))
    for i in range(1,6):
        band_data_4[:,i] = band_data_4[:,i] * 0.02998

    band_data_5 = np.loadtxt(str(files[4]))
    for i in range(1,6):
        band_data_5[:,i] = band_data_5[:,i] * 0.02998

    band_data_6 = np.loadtxt(str(files[5]))
    for i in range(1,6):
        band_data_6[:,i] = band_data_6[:,i] * 0.02998

    band_data_7 = np.loadtxt(str(files[6]))
    for i in range(1,6):
        band_data_7[:,i] = band_data_7[:,i] * 0.02998

    band_data_8 = np.loadtxt(str(files[7]))
    for i in range(1,6):
        band_data_8[:,i] = band_data_8[:,i] * 0.02998

    band_data_9 = np.loadtxt(str(files[8]))
    for i in range(1,6):
        band_data_9[:,i] = band_data_9[:,i] * 0.02998

    band_data_10 = np.loadtxt(str(files[9]))
    for i in range(1,6):
        band_data_10[:,i] = band_data_10[:,i] * 0.02998

    band_data_11 = np.loadtxt(str(files[10]))
    for i in range(1,6):
        band_data_11[:,i] = band_data_11[:,i] * 0.02998

    # band_data_12 = np.loadtxt(str(files[11]))
    # for i in range(1,6):
    #     band_data_12[:,i] = band_data_12[:,i] * 0.02998

    band_diff_111 = get_band_diff(band_data_1, band_data_11)

    band_diff_211 = get_band_diff(band_data_2, band_data_11)

    band_diff_311 = get_band_diff(band_data_3, band_data_11)

    band_diff_411 = get_band_diff(band_data_4, band_data_11)

    band_diff_511 = get_band_diff(band_data_5, band_data_11)

    band_diff_611 = get_band_diff(band_data_6, band_data_11)

    band_diff_711 = get_band_diff(band_data_7, band_data_11)

    band_diff_811 = get_band_diff(band_data_8, band_data_11)

    band_diff_911 = get_band_diff(band_data_9, band_data_11)

    band_diff_1011 = get_band_diff(band_data_10, band_data_11)

    # band_diff_1112 = get_band_diff(band_data_11, band_data_12)

    point_names = ['$\Gamma$', 'X', 'W', 'K', '$\Gamma$', 'L']
    band_points = band_data_1[::50,0][:len(point_names)]

    f, ax1 = plt.subplots(1)
    f.suptitle('Average Absolute Difference per Band \nin Phonon Dispersion from NQ=14')
    # ax1.plot(band_data_1[:,0], band_diff_111, label='NQ=4', linewidth=0.8)
    # ax1.plot(band_data_1[:,0], band_diff_211, label='NQ=5', linewidth=0.8)
    # ax1.plot(band_data_1[:,0], band_diff_311, label='NQ=6', linewidth=0.8)
    # ax1.plot(band_data_1[:,0], band_diff_411, label='NQ=7', linewidth=0.8)
    # ax1.plot(band_data_1[:,0], band_diff_511, label='NQ=8', linewidth=0.8)
    # ax1.plot(band_data_1[:,0], band_diff_611, label='NQ=9', linewidth=0.8)
    # ax1.plot(band_data_1[:,0], band_diff_711, label='NQ=10', linewidth=0.8)
    # ax1.plot(band_data_1[:,0], band_diff_811, label='NQ=11', linewidth=0.8)
    # ax1.plot(band_data_1[:,0], band_diff_911, label='NQ=12', linewidth=0.8)
    # ax1.plot(band_data_1[:,0], band_diff_1011, label='NQ=13', linewidth=0.8)
    ax1.plot(band_data_1[:,0], band_diff_511, color='b', label='NQ=8', linewidth=0.8)
    ax1.plot(band_data_1[:,0], band_diff_511, color='b', linewidth=0.8)
    ax1.plot(band_data_1[:,0], band_diff_511, color='b', linewidth=0.8)
    ax1.plot(band_data_1[:,0], band_diff_511, color='b', linewidth=0.8)
    ax1.plot(band_data_1[:,0], band_diff_511, color='b', linewidth=0.8)
    ax1.plot(band_data_1[:,0], band_diff_511, color='b', linewidth=0.8)
    ax1.plot(band_data_1[:,0], band_diff_611, color='r', label='NQ=9', linewidth=0.8)
    ax1.plot(band_data_1[:,0], band_diff_611, color='r', linewidth=0.8)
    ax1.plot(band_data_1[:,0], band_diff_611, color='r', linewidth=0.8)
    ax1.plot(band_data_1[:,0], band_diff_611, color='r', linewidth=0.8)
    ax1.plot(band_data_1[:,0], band_diff_611, color='r', linewidth=0.8)
    ax1.plot(band_data_1[:,0], band_diff_611, color='r', linewidth=0.8)
    ax1.plot(band_data_1[:,0], band_diff_711, color='g', label='NQ=10', linewidth=0.8)
    ax1.plot(band_data_1[:,0], band_diff_711, color='g', linewidth=0.8)
    ax1.plot(band_data_1[:,0], band_diff_711, color='g', linewidth=0.8)
    ax1.plot(band_data_1[:,0], band_diff_711, color='g', linewidth=0.8)
    ax1.plot(band_data_1[:,0], band_diff_711, color='g', linewidth=0.8)
    ax1.plot(band_data_1[:,0], band_diff_711, color='g', linewidth=0.8)
    ax1.plot(band_data_1[:,0], band_diff_811, color='orange', label='NQ=11', linewidth=0.8)
    ax1.plot(band_data_1[:,0], band_diff_811, color='orange', linewidth=0.8)
    ax1.plot(band_data_1[:,0], band_diff_811, color='orange', linewidth=0.8)
    ax1.plot(band_data_1[:,0], band_diff_811, color='orange', linewidth=0.8)
    ax1.plot(band_data_1[:,0], band_diff_811, color='orange', linewidth=0.8)
    ax1.plot(band_data_1[:,0], band_diff_811, color='orange', linewidth=0.8)
    ax1.plot(band_data_1[:,0], band_diff_911, color='yellow', label='NQ=12', linewidth=0.8)
    ax1.plot(band_data_1[:,0], band_diff_911, color='yellow', linewidth=0.8)
    ax1.plot(band_data_1[:,0], band_diff_911, color='yellow', linewidth=0.8)
    ax1.plot(band_data_1[:,0], band_diff_911, color='yellow', linewidth=0.8)
    ax1.plot(band_data_1[:,0], band_diff_911, color='yellow', linewidth=0.8)
    ax1.plot(band_data_1[:,0], band_diff_911, color='yellow', linewidth=0.8)
    ax1.plot(band_data_1[:,0], band_diff_1011, color='cyan', label='NQ=13', linewidth=0.8)
    ax1.plot(band_data_1[:,0], band_diff_1011, color='cyan', linewidth=0.8)
    ax1.plot(band_data_1[:,0], band_diff_1011, color='cyan', linewidth=0.8)
    ax1.plot(band_data_1[:,0], band_diff_1011, color='cyan', linewidth=0.8)
    ax1.plot(band_data_1[:,0], band_diff_1011, color='cyan', linewidth=0.8)
    ax1.plot(band_data_1[:,0], band_diff_1011, color='cyan', linewidth=0.8)
    # ax1.plot(band_data_1[:,0][:10], band_diff_1112[:10], color='purple', label='NQ=14', linewidth=0.8)
    # ax1.plot(band_data_1[:,0][45:55], band_diff_1112[45:55], color='purple', linewidth=0.8)
    # ax1.plot(band_data_1[:,0][95:105], band_diff_1112[95:105], color='purple', linewidth=0.8)
    # ax1.plot(band_data_1[:,0][145:155], band_diff_1112[145:155], color='purple', linewidth=0.8)
    # ax1.plot(band_data_1[:,0][190:210], band_diff_1112[190:210], color='purple', linewidth=0.8)
    # ax1.plot(band_data_1[:,0][245:251], band_diff_1112[245:251], color='purple', linewidth=0.8)

    ax1.set_ylim(0,max(band_diff_511))
    ax1.vlines(band_points,0,max(band_diff_511),color='grey',linestyle='dotted')
    ax1.hlines(1.0, 0, max(band_data_1[:,0]), color='black', linestyle='solid')
    ax1.set_xticks(band_points)
    ax1.set_xticklabels(point_names)
    ax1.set_ylabel(r'Average Frequency Difference per Band (THZ)')

    plt.legend(loc='best')

    plt.show()
