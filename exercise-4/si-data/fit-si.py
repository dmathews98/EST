'''
Fitting Silicon data to Murnaghan, 3rd O Burch-Murnaghan and Vinet EoS
'''

from __future__ import division
import numpy as np
import lmfit
import matplotlib.pyplot as plt
import math as m

def read_in(file):
    xvals = [] # a /Bohr
    yvals = [] # E /Ry
    f = open(file, 'r')
    for line in f.readlines():
        vals  = line.split(' ')
        xvals.append(float(vals[0]))
        yvals.append(float(vals[1]))
    f.close()

    xvals = np.array(xvals)
    yvals = np.array(yvals)

    return xvals, yvals

    # x = V
def MurnaghanEoS(x, B, Bp):
    n = (x/Vo)**(1.0/3.0)
    E = Eo + ((B*Vo)/Bp)*(n**3.0)*(((n**(-3.0*Bp))/(Bp - 1.0)) + 1.0) - ((B*Vo)/(Bp - 1.0))
    return E

def BirchEoS(x, B, Bp):
    n = (x/Vo)**(1.0/3.0)
    E = Eo + (9.0/16.0)*B*Vo*(((n**(-2.0) - 1.0)**(3.0))*Bp + ((n**(-2.0) - 1.0)**(2.0))*(6.0 - 4.0*(n**(-2.0))))
    return E

def VinetEoS(x, B, Bp):
    n = (x/Vo)**(1.0/3.0)
    t1 = 4.0*B*Vo/(Bp - 1.0)**(2.0)
    t2 = 2.0*B*Vo/(Bp - 1.0)**(2.0)
    t3 = np.exp((3.0/2.0)*(Bp - 1.0)*(1 - n))
    t4 = (3.0*(Bp - 1.0)*(1.0 - n) - 2.0)
    E = Eo + t1 + (t2 * t3 * t4)

    return E

def fit_method(method, xvals, yvals, B_g, Bp_g):
    model = lmfit.Model(method)

    parameters = model.make_params(B=B_g, Bp=Bp_g)
    #parameters['B'].min = 0
    #parameters['Bp'].min = 0

    result = model.fit(yvals, x=xvals, params=parameters)

    #print(result.fit_report())
    #print('\n')
    BPa = result.params['B'].value * (2.179872325e-18/((5.291771067e-11)**3))
    uncert = result.params['B'].stderr * (2.179872325e-18/((5.291771067e-11)**3))
    BGPa = BPa * 1e-9
    uncertGPa = uncert * 1e-9
    perc = uncertGPa/BGPa *100

    print(str(method))
    print('Fitted B in GPa = ' +str(BGPa) + ' +/- ' +str(uncertGPa) +' ('+str(perc)+' %)')

    #28.086 from input file
    Vo_m = Vo*((5.291771067e-11)**3)
    rho = 28.086*8*1.67377e-27/Vo_m   # mass density
    cl = np.sqrt((BPa/rho))   # longitudinal sound velocity
    print('From fitted B:\nLongitudinal sound velocity in ms^-1 = ' +str(cl))

    n = 2/(Vo_m)**(1/3)
    kd = n*np.power(((np.pi)**2)*6, 1/3)
    kb = 1.3807e-23
    hbar = 6.626e-34/(2*np.pi)
    thetad = hbar*cl*kd/kb
    print('Debye temeprature in K = ' +str(thetad)+'\n')

    return model, result

def main():
    file = 'si-data-a.txt'

    xvals, yvals = read_in(file)

    xvals = (xvals**3.0)/8
    yvals = yvals/2

    # 1 Ry = 2.179872325e-18 J
    # 1 Bohr = 5.2291771067e-11 m
    # B * (2.179872325e-18/(5.291771067e-11)**3)*1e-9 gives B in GPA

    global Eo
    global Vo
    Eo = min(yvals)
    Eo_ev = Eo / 13.6
    print('\nEo in eV = ' + str(Eo_ev))
    for i in range(len(yvals)):
        if yvals[i] == Eo:
            Vo = xvals[i] # Bohrs ^3
    voa_pera = Vo * ((0.52291771067)**3)
    print('Vo in Ang cubed per atom = ' +str(voa_pera) + '\n')

    # inital guesses
    B_g = 100.0 * 1e9 / (2.179872325e-18/(5.291771067e-11)**3)
    Bp_g = 5.0 * 1e9 / (2.179872e-18/(5.291771067e-11)**3)

    xplot = np.linspace(770/8, 1460/8, 1000)

    Method = MurnaghanEoS
    M_model, M_result = fit_method(Method, xvals, yvals, B_g, Bp_g)

    Method = BirchEoS
    B_model, B_result = fit_method(Method, xvals, yvals, B_g, Bp_g)

    Method = VinetEoS
    V_model, V_result = fit_method(Method, xvals, yvals, B_g, Bp_g)

    plt.figure(1)
    plt.plot(xvals, yvals, color='black', marker='.',linewidth=0, label='Data')
    plt.title('Energy of ground state Si for varying volume')
    plt.xlabel('Volume /Bohrs cubed')
    plt.ylabel('Energy /Ry')

    plt.plot(xplot, M_model.eval(M_result.params, x=xplot), 'r--', label = 'Murnaghan')
    plt.legend(loc='best')
    #plt.savefig('Murnaghan.pdf')

    plt.figure(2)
    plt.plot(xvals, yvals, color='black', marker='.',linewidth=0, label='Data')
    plt.title('Energy of ground state Si for varying volume')
    plt.xlabel('Volume /Bohrs cubed')
    plt.ylabel('Energy /Ry')

    plt.plot(xplot, B_model.eval(B_result.params, x=xplot), 'g--', label = 'Birch-Murnaghan 3rdO')
    plt.legend(loc='best')
    #plt.savefig('Birch.pdf')

    plt.figure(3)
    plt.plot(xvals, yvals, color='black', marker='.',linewidth=0, label='Data')
    plt.title('Energy of ground state Si for varying volume')
    plt.xlabel('Volume /Bohrs cubed')
    plt.ylabel('Energy /Ry')

    plt.plot(xplot, V_model.eval(V_result.params, x=xplot), 'b--', label = 'Vinet')

    plt.legend(loc='best')
    #plt.savefig('Vinet.pdf')
    plt.show()

main()
