##
## inimaker module
##i


class inimaker:

    def __init__ (self, bootstrap=5000,mcmc=10000):
        self.cont="""
# Tabulated models to use
modelroot = models/
fiducial =  DR9LyaMocks
nowiggles = DR9LyaMocksSB
broadband = DR9LyaMocksBBand

model-config = value[gamma-bias]=3.8; gaussprior[gamma-bias]@(2.8,4.8)
model-config = fix[gamma-beta]=0;
model-config = value[beta]=1.4; gaussprior[beta]@(1.0,1.8)
model-config = fix[(1+beta)*bias]=-0.336; 
model-config = value[BAO alpha-iso]=1.0; boxprior[BAO alpha-iso]@(0.85,1.15)
model-config = fix[BBand1*]; fix[BAO alpha-p*]; fix[gamma-scale];

fix-aln-cov = true

#redshift dependence - this is constant
nz = 3
minz = 1.75
dz = 0.5

#separation for aln
nsep = 18
minsep = 0
dsep = 10

# ...ll=abs(log(lam2/lam1))

minll = 0.05 # cosmolib's xi3d_llstart
maxll = 0.27 # cosmolib's xi3d_llend
dll = 0.02   # cosmolib's xi3d_llstep
dll2 = 0.002 # cosmolib's Delta_pix_3D (uses two_step if this is non-zero)

rmin = 50
rmax = 170

weighted=true

""".split('\n')
        self.cont=[x+"\n" for x in self.cont]
        if (not bootstrap==None):
            self.cont.append("bootstrap-trials = %i\n"%(bootstrap))
        if (not mcmc==None):
            self.cont.append("mcmc-save = %i\n"%(mcmc))
            self.cont.append("mcmc-interval = 50\n")


    def update (self, field, value):
        ## model configs add
        ## otherwise we need to look if we need to add it
        if (field=='model-config'):
            self.cont.append(field+" = "+value+"\n")
        else:
            for i,line in enumerate(self.cont):
                if "=" in line:
                    #first,second = line.split('=')
                    qu = line.find("=")
                    first=line[:qu]
                    second=line[qu+1:]
                    first=first.replace(' ','')
                    #print '|'+first+'|'+field+'|',first==field
                    if first==field:
                        self.cont[i]=first+" = "+value+'\n'
                        return
            # if not found, just add
            self.cont.append(field+" = "+value+"\n")
                
                    
    def write(self,name):
        f=open ("inis/"+name+".ini",'w').writelines(self.cont)
