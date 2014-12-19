from XDSM import XDSM

opt = 'Optimization'
dat = 'DataInter'

x = XDSM()

x.addComp('Optimizer', 'Analysis', 'Optimizer')
x.addComp('solver', 'MDA', 'Solver')
x.addComp('C1', opt, 'C1')
x.addComp('C2', opt, 'C2')
x.addComp('C3', opt, 'C3')


x.addDep('C1', 'solver', dat, "$y_1$")
x.addDep('C2', 'C1', dat, "$y_2$")
x.addDep('solver', 'C2', dat, "$y_1$")
x.addDep('C3', 'C2', dat, "$y_1$")


x.addDep('C1', 'Optimizer', dat, "$x_1$")
x.addDep('C3', 'Optimizer', dat, "$x_2$")
x.addDep('Optimizer', 'C3', dat, "$f$")

x.write('total_v_partial', True)
