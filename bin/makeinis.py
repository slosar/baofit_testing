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
pos.update("model-config","fix[BAO amplitude]=1.0;release[(1+beta)*bias];")
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
zsc.update("model-config","value[gamma-scale]=0; release[gamma-scale]; gaussprior[gamma-scale]@(-0.5,0.5)")
zsc.write("zscale")

### anisotropic fit
ani = inimaker()
ani.update ("model-config","fix[BAO amplitude]=1.0; fix[BAO alpha-iso]=1.0;release[(1+beta)*bias]; ");
ani.update ("model-config", "release[BAO alpha-perp]; gaussprior[BAO alpha-perp]@(0.85,1.15)");
ani.update ("model-config", "release[BAO alpha-parallel]; gaussprior[BAO alpha-parallel]@(0.85,1.15)");
ani.update ("anisotropic","true");
ani.write("ani")


### bias beta fit
bb = inimaker()
bb.update("model-config", "fix[BAO amplitude]; fix[BAO alpha-iso]; fix[gamma-bias]; noprior[beta]; release[(1+beta)*bias]")
bb.write("bb")
bb.update("model-config", "release[gamma-bias]; boxprior[gamma-bias]@(0,5); release[gamma-beta]; boxprior[gamma-beta]@(-1,1)")
bb.write("bbext")

