#%%

from pykat import finesse        
from pykat.commands import *    
import numpy as np               
import matplotlib.pyplot as plt  



basekat = finesse.kat() 
basekat.verbose = False



basekat.parse("""
            l laser 1 0 n0
            s s0 0.1 n0 n1

                # the cavity:
            m1 M1 0.15 0 0 n1 n2
            s scav 0.2 n2 n3
            m1 M2 0.15 0 0 n3 n4
""")



kat = basekat.deepcopy()
kat.s0.remove()

###############Modulation and PDH######################
f_mod = 100e6
kat.parse("""
                # modulator
            
            s smod 0 n0 nmod1
            mod eom {f} 0.3 1 pm nmod1 nmod2
            s s0 0 nmod2 n1

                # photodiode and xaxis
            pd1 PDH {f} 0 n1
            xaxis M2 phi lin -150 150 400
""".format(f=f_mod))


for P in [0, 30, 60, 90, 120]:
    k = kat.deepcopy()
    k.PDH.phase1 = P
    out = k.run()
    plt.plot(out.x, out["PDH"], label='demod phase = {}$^\circ$'.format(P))
plt.xlabel('M2 tuning [deg]')
plt.ylabel('PDH Error Signal [W]')
plt.legend(loc=2, bbox_to_anchor=(1,1))
plt.show()




kat2 = kat.deepcopy()
kat2.parse("pd Pcirc n3")
out = kat2.run()

fig, ax = plt.subplots(2, 1, sharex=True)
ax[0].plot(out.x, out['Pcirc'], label="M1 phi = 0°")
ax[0].set_ylabel('[W]')
ax[1].plot(out.x, out['PDH'])
ax[1].set_ylabel('PDH Err Sig [W]')
ax[1].set_xlabel('M2 tuning [deg]')

kat3 = kat2.deepcopy()
kat3.M1.phi = 3
out = kat3.run()

ax[0].plot(out.x, out['Pcirc'], label="M1 phi = 3°")
ax[1].plot(out.x, out['PDH'])
ax[0].legend()
plt.show()

####################Lock###############################

kat4 = kat2.deepcopy()
kat4.verbose = True
kat4.parse("""
            xaxis M2 phi lin 0 100 200
            set err PDH re 
            lock z $err -1 1m

            put* M1 phi $z
""")
out = kat4.run()
out.plot()
