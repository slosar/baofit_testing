#!/usr/bin/env python

from inimaker import *
import os

os.system ('mkdir inis 2>/dev/null; rm inis/*.ini')
## by default we are trying to detect vanilla
vanilla=inimaker()
vanilla.write("bao_ampl")

## position detection, here we fix amplitude, and vary xibb.
## should be very similar

pos = inimaker()
pos.update("model-config","fix[BAO amplitude]=1.0;value[(1+beta)*bias]=-0.336")
pos.write("bao_pos")


# skip those for the time being
if False:
### rad tests
    rad = inimaker()
    rad.update("rmin","20")
    rad.update("rmax","150")
    rad.write("rad_20_150")
    rad.update("rmin","50")
    rad.update("rmax","190")
    rad.write("rad_50_190")

### zscale
zsc = inimaker()
zsc.update("model-config","value[alpha-scale]=0; release[alpha-scale]; gaussprior[alpha-scale]@(-0.5,0.5)")
zsc.write("zscale")

### anisotropic fit
ani = inimaker()
ani.update ("model-config","fix[BAO amplitude]=1.0; fix[BAO scale]=1.0;release[(1+beta)*bias]; ");
ani.update ("model-config", "release[BAO scale a]; gaussprior[BAO scale a]@(0.85,1.15)");
ani.update ("model-config", "release[BAO scale b]; gaussprior[BAO scale b]@(0.85,1.15)");
ani.update ("anisotropic","true");
ani.write("ani")

