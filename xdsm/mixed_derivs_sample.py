from XDSM import XDSM

opt = 'Optimization'
dat = 'DataInter'

x = XDSM()

x.addComp('Optimizer', 'Analysis', 'Optimizer')
x.addComp('C1', opt, 'C1')
x.addComp('solver', 'MDA', 'Solver')
x.addComp('C3', opt, 'C3')
x.addComp('C4', opt, 'C4')
x.addComp('C5', opt, 'C5')

x.addDep('C4', 'C1', dat, "")

x.addDep('C4', 'C3', dat, "")
x.addDep('C3', 'solver', dat, "")
x.addDep('C4', 'C3', dat, "")
x.addDep('solver', 'C4', dat, "")
x.addDep('C5', 'C4', dat, "")


x.addDep('C1', 'Optimizer', dat, "")
x.addDep('C3', 'Optimizer', dat, "")
x.addDep('Optimizer', 'C5', dat, "")




x.write('mixed_derivs_sample_xdsm',True)