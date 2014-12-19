from XDSM import XDSM

opt = 'Optimization'
anl = 'Analysis'
dat = 'DataInter'

x = XDSM()
x.addComp('opt', opt, 'Optimizer')
#x.addComp('Solver', 'MDA', 'Solver')
x.addComp('f', anl, '$F(x,y)$')
x.addComp('fp', anl, "$F^\prime(x,y)$")


x.addDep('f', 'opt', dat, '$x, y$')
x.addDep('fp', 'opt', dat, '$x, y$')
x.addDep('opt', 'f', dat, '$f(x,y), g(x), h(y)$')
x.addDep('opt', 'fp', dat, r'$\frac{df}{dx}, \frac{df}{dy}, \frac{dg}{dx}, \frac{dh}{dy}$')


x.write('basic_opt',True)
