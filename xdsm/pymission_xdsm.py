from XDSM import XDSM

opt = 'Optimization'
dat = 'DataInter'

x = XDSM()
x.addComp('opt', 'Analysis', 'Optimizer')
x.addComp('splines', opt, 'Control Splines')
x.addComp('atmo', opt, 'Atmostpherics')

x.addComp('solver', 'MDA', 'Solver')
x.addComp('aero', opt, 'Aerodynamics')

x.addComp('prop', opt, 'Propulsion')
x.addComp('perf', opt, '\TwolineComponent{2.1cm}{Mission}{Performance}')

x.addDep('splines', 'opt', dat, 'Alt, MN')

#x.addDep('prop', 'splines', dat, '')
x.addDep('aero', 'splines', dat, '')
x.addDep('atmo', 'splines', dat, '')
x.addDep('prop', 'splines', dat, '')

x.addDep('aero', 'atmo', dat, '')
x.addDep('prop', 'atmo', dat, '')

x.addDep('aero', 'solver', dat, '')
x.addDep('solver', 'aero', dat, '')

x.addDep('perf', 'prop', dat, '')
x.addDep('perf', 'aero', dat, '')
x.addDep('perf', 'atmo', dat, '')

x.addDep('prop', 'aero', dat, '')


x.addDep('opt', 'perf', dat, 'Fuel Burn')

x.write('pymission_xdsm',True)
