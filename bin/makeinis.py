#!/usr/bin/env python

from inimaker import *

## by default we are trying to detect vanilla
vanilla=inimaker(bootstrap=10000, mcmc=10000)
vanilla.write("bao_ampl")

## position detection, here we fix amplitude, and vary xibb.
## should be very similar

pos = inimaker()
pos.update("model-config","fix[BAO amplitude]=1.0;value[(1+beta)*bias]=-0.336")
pos.write("bao_pos")

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
zsc.update("model-config","value[alpha-scale]=0")
zsc.write("zscale")

### anisotropic fit
ani = inimaker(mcmc=10000)
ani.update ("model-config","fix[BAO scale]=1.0; value[BAO scale a]=0.0; value[BAO scale b]=0.0")
ani.write("ani")

