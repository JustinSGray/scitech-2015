from XDSM import XDSM

opt = 'Optimization'
dat = 'DataInter'

x = XDSM()
x.addComp('Optimizer', 'Analysis', 'Optimizer')
x.addComp('Orbit', opt, 'Orbit Dynamics')
x.addComp('Attitude', opt, 'Attitude Dynamics')
x.addComp('Solar', opt, 'Cell Illumination')
x.addComp('Thermal', opt, 'Temperature')
x.addComp('Electrical', opt, 'Solar Power')
x.addComp('Battery', opt, 'Energy Storage')
x.addComp('Comm', opt, 'Communication')

x.addDep('Optimizer', 'Battery', dat, '')
x.addDep('Optimizer', 'Comm', dat, '')
x.addDep('Attitude', 'Optimizer', dat, '')
x.addDep('Solar', 'Attitude', dat, '')
x.addDep('Solar', 'Orbit', dat, '')
x.addDep('Thermal', 'Solar', dat, '')
x.addDep('Thermal', 'Optimizer', dat, '')
x.addDep('Electrical', 'Solar', dat, '')
x.addDep('Electrical', 'Optimizer', dat, '')
x.addDep('Electrical', 'Thermal', dat, '')
x.addDep('Battery', 'Electrical', dat, '')
x.addDep('Battery', 'Thermal', dat, '')
x.addDep('Battery', 'Attitude', dat, '')
x.addDep('Battery', 'Optimizer', dat, '')
x.addDep('Comm', 'Attitude', dat, '')
x.addDep('Comm', 'Orbit', dat, '')
x.addDep('Comm', 'Optimizer', dat, '')

x.write('cadre_xdsm',True)