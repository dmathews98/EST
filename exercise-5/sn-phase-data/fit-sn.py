'''
Fits alpha and beta tin data to Vinet EoS and finds common tangent for phase transition
'''

from __future__ import division
import numpy as np
import lmfit
import matplotlib.pyplot as plt
import math as m
from scipy import optimize

def VinetEoS(x, B, Bp, Eo, Vo):
    n = (x/Vo)**(1.0/3.0)
    t1 = 4.0*B*Vo/(Bp - 1.0)**(2.0)
    t2 = 2.0*B*Vo/(Bp - 1.0)**(2.0)
    t3 = np.exp((3.0/2.0)*(Bp - 1.0)*(1 - n))
    t4 = (3.0*(Bp - 1.0)*(1.0 - n) - 2.0)
    E = Eo + t1 + (t2 * t3 * t4)

    return E

def fit_method(method, xvals, yvals, B_g, Bp_g, Eo, Vo):
    model = lmfit.Model(method)

    parameters = model.make_params(B=B_g, Bp=Bp_g, Eo=Eo, Vo=Vo)
    #parameters['Eo'].vary = False
    #parameters['Vo'].vary = False
    #parameters['B'].min = 0
    #parameters['Bp'].min = 0

    result = model.fit(yvals, x=xvals, params=parameters)

    print(result.fit_report())
    print('\n')
    BPa = result.params['B'].value * (2.179872325e-18/((5.291771067e-11)**3))
    uncert = result.params['B'].stderr * (2.179872325e-18/((5.291771067e-11)**3))
    BGPa = BPa * 1e-9
    uncertGPa = uncert * 1e-9
    perc = uncertGPa/BGPa *100

    Bp = result.params['Bp'].value
    Bpuncert = result.params['Bp'].stderr
    Bpperc = Bpuncert/Bp *100

    Eof = result.params['Eo'].value / 13.6
    Eoun = result.params['Eo'].stderr / 13.6
    Eoperc = Eoun/Eof *100

    Vof = result.params['Vo'].value * 5.291771067e-1**3
    Voun = result.params['Vo'].stderr * 5.291771067e-1**3
    Voperc = Voun/Vof *100

    print(str(method))
    print('Fitted B in GPa = ' +str(BGPa) + ' +/- ' +str(uncertGPa) +' ('+str(perc)+' %)\n')

    print('Fitted B\' = ' +str(Bp) + ' +/- ' +str(Bpuncert) +' ('+str(Bpperc)+' %)\n')

    print('Fitted Eo in eV = ' +str(Eof) + ' +/- ' +str(Eoun) +' ('+str(Eoperc)+' %)\n')

    print(r'Fitted Vo in $\AA^3$ = ' +str(Vof) + ' +/- ' +str(Voun) +' ('+str(Voperc)+' %)\n')

    return model, result

def fit_tang(x, V_result_a, V_model_a, V_result_b, V_model_b):
    xa = x[0]
    xb = x[1]
    h=0.1
    # eqn 1
    dfa = (V_model_a.eval(V_result_a.params, x=xa) - V_model_a.eval(V_result_a.params, x=xa+h))/(xa -(xa+h))
    dfb = (V_model_b.eval(V_result_b.params, x=xb) - V_model_b.eval(V_result_b.params, x=xb+h))/(xb -(xb+h))
    diff = dfa-dfb

    # eqn 2
    eq2 = dfa*(xa-xb) - (V_model_a.eval(V_result_a.params, x=xa) - V_model_b.eval(V_result_b.params, x=xb))

    return [diff, eq2]

def linear(x, m, b):
    return (m*x + b)

def main():
    global tinmass
    tinmass = 118.71

    Method = VinetEoS

    # inital guesses
    B_g = 50.0 * 1e9 / (2.179872325e-18/(5.291771067e-11)**3)
    Bp_g = 4.0

    # ALPHA

    filea = 'alpha-sn.txt'
    alpha_data = np.transpose(np.loadtxt(filea))[:,::5]

    alpha_data[0] = (alpha_data[0]**3.0)/8.0 # vol per atom in bohr cubed
    alpha_data[1] = alpha_data[1]/2.0# energy per atom in Ry

    Eo_a = min(alpha_data[1])
    index = np.argmin(alpha_data[1])
    Vo_a = alpha_data[0][index]

    Eo_ev_a = Eo_a /13.6
    print('\nEo in eV = ' + str(Eo_ev_a))
    voa_pera_a = Vo_a * ((0.52291771067)**3)
    print('Vo in Ang cubed per atom = ' +str(voa_pera_a) + '\n')

    xplota = np.linspace(160, 310, 1000)

    V_model_a, V_result_a = fit_method(Method, alpha_data[0], alpha_data[1], B_g, Bp_g, Eo_a, Vo_a)

    # BETA

    fileb = 'beta-sn.txt'
    beta_data = np.transpose(np.loadtxt(fileb))[:,::5]

    beta_data[0] = (beta_data[0]**2)*(0.5456*beta_data[0])/4.0 # vol per atom in bohr cubed
    beta_data[1] = beta_data[1]/2.0 # energy per atom in Ry

    Eo_b = min(beta_data[1])
    index = np.argmin(beta_data[1])
    Vo_b = beta_data[0][index]

    Eo_ev_b = Eo_b /13.6
    print('\nEo in eV = ' + str(Eo_ev_b))
    voa_pera_b = Vo_b * ((0.52291771067)**3)
    print('Vo in Ang cubed per atom = ' +str(voa_pera_b) + '\n')

    xplotb = np.linspace(130, 250, 1000)

    V_model_b, V_result_b = fit_method(Method, beta_data[0], beta_data[1], B_g, Bp_g, Eo_b, Vo_b)

    # Common tangent

    x_test = [200, 350]
    com_x = optimize.fsolve(fit_tang, x_test, args=(V_result_a, V_model_a, V_result_b, V_model_b))

    com_y = [0, 0]
    com_y[0] = V_model_a.eval(V_result_a.params, x=com_x[0])
    com_y[1] = V_model_b.eval(V_result_b.params, x=com_x[1])

    linfit = lmfit.Model(linear)
    m_g = 60
    b_g = -300
    paramets = linfit.make_params(m=m_g, b=b_g)
    res = linfit.fit(com_y, x=com_x, params=paramets)

    p = -1 * res.params['m'].value * (2.179872325e-18/((5.291771067e-11)**3)) * 1e-9
    p_err = res.params['m'].stderr * (2.179872325e-18/((5.291771067e-11)**3)) * 1e-9
    p_perc = (p_err/p) * 100

    dv = (abs(com_x[1]-com_x[0]))/com_x[1] * 100

    print('Critical pressure in GPa = ' + str(p) + ' +/- ' + str(p_err) + ' ( ' + str(p_perc) + ' %)\n')
    print('Volume change at Critical pressure = ' + str(dv) + ' %\n')

    xplotcom = np.linspace(150, 240, 1000)

    plt.figure(1)
    plt.plot(alpha_data[0], alpha_data[1], color='black', marker='.',linewidth=0, label='Alpha data')
    plt.plot(beta_data[0], beta_data[1], color='red', marker='.',linewidth=0, label='Beta data')
    plt.plot(com_x, com_y, color='yellow', marker='.',linewidth=0, label='Common tangent points')
    plt.title(r'Energy of ground state tin types for varying volume')
    plt.xlabel('Volume per atom /Bohrs cubed')
    plt.ylabel('Energy per atom /Ry')

    plt.plot(xplota, V_model_a.eval(V_result_a.params, x=xplota), 'g--', label = 'Alpha Vinet fit')
    plt.plot(xplotb, V_model_b.eval(V_result_b.params, x=xplotb), 'b--', label = 'Beta Vinet fit')
    plt.plot(xplotcom, linfit.eval(res.params, x=xplotcom), 'y--', label='Common tangent fit')

    plt.legend(loc='best')
    #plt.savefig('sn-phase.pdf')
    plt.show()

main()
