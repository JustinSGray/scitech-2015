from XDSM import XDSM

opt = 'Optimization'
anl = 'Analysis'
dat = 'DataInter'
proc = 'DataIO'

x = XDSM()
x.addComp('opt', opt, 'Optimizer')
x.addComp('mda', 'MDA', 'Solver')
x.addComp('f', anl, '$F(x,y)$')
x.addComp('fp', anl, "$F^\prime(x,y)$")


x.addDep('f', 'opt', dat, '$x$')

x.addDep('f', 'mda', dat, '$y$')
x.addDep('fp', 'mda', dat, '$y$')
x.addDep('mda', 'f', dat, '$h$')
x.addDep('mda', 'fp', dat, r'$\frac{dh}{dy}$')

x.addDep('fp', 'opt', dat, '$x$')
x.addDep('opt', 'f', dat, '$f, g$')
x.addDep('opt', 'fp', dat, r'$\frac{df}{dx}, \frac{dh}{dy}, \frac{dg}{dx}$')


x.write('mda',True)
