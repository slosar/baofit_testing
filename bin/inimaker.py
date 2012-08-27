##
## inimaker module
##i


class inimaker:

    def __init__ (self, bootstrap=None,mcmc=None):
        self.cont="""
# Tabulated models to use
modelroot = ../models/
fiducial =  DR9LyaMocks
nowiggles = DR9LyaMocksSB
broadband = DR9LyaMocksBBand

model-config = fix[alpha-bias]=3.8; fix[alpha-beta]=0; fix[beta]=1.4; fix[(1+beta)*bias]=-0.336;
model-config = fix[BBand1*]; fix[BAO scale *]; fix[alpha-scale];

nz = 3
minz = 1.75
dz = 0.5

rmin = 50
rmax = 150

""".split('\n')
        self.cont=[x+"\n" for x in self.cont]
        if (not bootstrap==None):
            self.cont.append("bootstrap-trials = %i\n"%(bootstrap))
        if (not mcmc==None):
            self.cont.append("mcmc-save = %i\n"%(mcmc))


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
