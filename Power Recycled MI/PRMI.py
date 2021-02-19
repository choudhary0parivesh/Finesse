from pykat import finesse        
from pykat.commands import *    
import numpy as np               
import matplotlib.pyplot as plt  

base = finesse.kat()
base.verbose = False

################ core optics#######################

basecode = """
                    l laser1 1.0 0 n1    #laser 1 watt
                    s s1 0 n1 n2         #cavity between laser and modulator
                    s s_mod n2 n3        # change modulator parameters
                    
                    m PRM 1 0 0 n3 n4    #recycling mirror
                    
                    bs bs1 0.5 0.5 0 0 n4 n5 n6 n7      #beam spplitter
                    
                    ##########y arm########
                    s s2 1 n5 n6         #cavity between BS and input RM
                    m ITMy 1 0 0 n6 n7   #input mirror
                    s scy 1 n7 n8        #cavity between mirror and end mirror
                    m ETMy 1 0 n8 n9     #end mirror
                    
                    
                    ##########x arm########
                    s s3 n6 n10          #cavity between BS and input RM
                    m ITMx 1 0 n11 n12   #input mirror
                    s scx 1 n13 n14      #cavity between mirror and end mirror
                    m ETMx 1 0 0 n15 n16 #end mirror

                    pd pow_out n7        #photo detector            


"""

base.parse(basecode)



