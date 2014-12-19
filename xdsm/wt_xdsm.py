from XDSM import XDSM

opt = 'Optimization'
dat = 'DataInter'

Large="\Large "

x = XDSM()
x.addComp('Optimizer', 'Analysis', Large + 'Optimizer')

x.addComp('solver', 'MDA', Large + 'Solver')

x.addComp('rotor', opt, Large + 'Rotor')
x.addComp('hub', opt, Large + 'Hub')
x.addComp('nacelle', opt, Large + 'Nacelle')
x.addComp('tower', opt, Large + 'Tower')
x.addComp('deflection', opt, Large + 'Tower Strike')
x.addComp('aep_a', opt, Large + 'AEP')
x.addComp('opex_a', opt, Large + 'Op. Exp.')
x.addComp('tcc_a', opt, Large + 'Cap. Cost')
x.addComp('bos_a', opt, Large + 'BOS')
x.addComp('fin_a', opt, Large + 'Fin.')


x.addDep('rotor', 'solver', dat, "$L_{blade}, precurve$")
x.addDep('solver', 'rotor', dat, "$\Delta_{L}, \Delta_{precurve}$")

x.addDep('tcc_a', 'rotor', dat, '$m_{blade}$, $P_{rated}$')
x.addDep('tcc_a', 'hub', dat, '$m_{hub}$')
x.addDep('tcc_a', 'nacelle', dat, '$m_{nacelle}$')
x.addDep('tcc_a', 'tower', dat, '$m_{tower}$')

x.addDep('bos_a', 'rotor', dat, '\TwolineComponent{2.1cm}{$m_{blade}$, $P_{rated}$}{$d_{rotor}$}')
x.addDep('bos_a', 'tcc_a', dat, "$\$_{tcc}$")

x.addDep('opex_a', 'rotor', dat, '$P_{rated}$')
x.addDep('opex_a', 'aep_a', dat, '$AEP_{net}$')

x.addDep('aep_a', 'rotor', dat, '$AEP$')

x.addDep('hub', 'rotor', dat, '\TwolineComponent{2.2cm}{$m_{blade}$, $d_{rotor}$,}{$M_{root}$}')

x.addDep('nacelle', 'rotor', dat, '\ThreelineComponent{2.1cm}{$m_{blade}, P_{rated}}{d_{rotor}, Q_{rotor}$}{$T_{rotor}, \Omega_{rated}$}')

x.addDep('tower', 'rotor', dat, '\ThreelineComponent{2.9cm}{$V_{rated}, V_{extreme}$}{$H, tilt, m_{rotor}, $}{$I_{rotor}, Q_{rotor}, T_{rotor}$}')
x.addDep('tower', 'hub', dat, '$m_{hub}, I_{hub}$')

x.addDep('tower', 'nacelle', dat, '$m_{nacelle}, I_{nacelle}$')

x.addDep('deflection', 'rotor', dat, '$L_{blade}, precone, tilt$')
x.addDep('deflection', 'nacelle', dat, '$L_{nac}, H_{nac}$')
x.addDep('deflection', 'tower', dat, '$z_{waist}, d_{tower}$')

x.addDep('fin_a', 'tcc_a', dat, "$\$_{tcc}$")
x.addDep('fin_a', 'bos_a', dat, "$\$_{bos}$")
x.addDep('fin_a', 'opex_a', dat, "$\$_{opex}$")
x.addDep('fin_a', 'aep_a', dat, "$AEP$")



x.addDep('rotor', 'Optimizer', dat, "\TwolineComponent{2.1cm}{$c,\\theta, t_{sc}, t_{te}, \lambda_2$}{$\lambda_{max}, H$}")
x.addDep('nacelle', 'Optimizer', dat, "$L_{shaft}, h_{beam}$")
x.addDep('tower', 'Optimizer', dat, "$d, t, z_{waist}$")


x.addDep('Optimizer', 'rotor', dat, r"$\delta_{rotor}, \epsilon, \Omega, \epsilon^*_{rotor}$")
x.addDep('Optimizer', 'nacelle', dat, "$\\sigma_{nacelle}, \epsilon, \\theta_{lss}$")
x.addDep('Optimizer', 'deflection', dat, "$\\delta_{max}$")
x.addDep('Optimizer', 'tower', dat, "\TwolineComponent{1.9cm}{$d_{top}, d_{base}, $}{$ \sigma_{tower}, \sigma^*_{tower}$}")
x.addDep('Optimizer', 'fin_a', dat, "$COE$")


x.write('wt_xdsm',True)