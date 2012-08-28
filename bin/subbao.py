#!/usr/bin/env python
import sys, os, os.path
nproc=2
priority="high"
typ = sys.argv[1]

## type is delta/flux/data _ aln,xu
ty1,ty2=typ.split('_')
if (ty2=='xu'):
    xu=True
    xustr="Xu"
elif (ty2=='aln'):
    xu=False
    xustr="Aln2"
else:
    print "bad type 2"
    sys.exit(1)

if (ty1=="delta"):
    plateroot = 'delta_pk_'+xustr+'_d3d'
elif (ty1=="flux"):
    plateroot = 'flux_'+xustr+"_EM_d3d"
elif (ty1=="data"):
    plateroot = 'data_'+xustr+".SN"
else:
    print "bad type 1"
    sys.exit(1)


ini = sys.argv[2]
outrootdir = "outputs/"+(os.path.basename(ini)).replace('.ini','')

if (len(sys.argv)>3):
    rlist=sys.argv[3]
    if '-' in rlist:
        beg,end=map(int,rlist.split('-'))
        rlist=range(beg,end+1)
    else:
        rlist=map(int,rlist.split(','))
else:
    rlist=[1]


os.system('mkdir '+outrootdir)
os.system ('cp '+ini+" "+outrootdir)

for r in rlist:
    
    #special meaning for data. "realization" is now data type
    if (ty1=="data"):
        if r==1:
            plateroot="data_"+xustr+".SN"
        elif r==2:
            plateroot="data_"+xustr+".SN.3"
        elif r==3:
            plateroot="data_"+xustr+".SN.nolint"

    proot="data/"+plateroot
            
    eo=""
            
    if r==17:
        r="ALL"
        eo="--reuse-cov=1"
    elif r==18:
        r="ALL_ALT"
    else:
        r=str(r)
        eo="--reuse-cov=1"

    croot=outrootdir+'/'+typ+'.'+r

    if xu:
        eo += " --xi-format --xi-hexa"
    else:
        pass

            

    
    name = os.path.basename(croot)
    sysline = "OMP_NUM_THREADS=%i baofit -i %s --plateroot=%s/ "%(nproc,ini,proot)
    sysline += "--platelist=lr%s %s --output-prefix=%s. >%s.log 2>%s.err" %(r,eo,croot,croot,croot)

    astrobnl='astro0034' in os.getenv('HOSTNAME')
    ## Where are we?
    if (astrobnl):
        exeline = 'nohup wq sub -r "N:%i; priority:%s; mode:bycore1; job_name:%s" -c "source ~/.bashrc; %s" & '%(nproc, priority,name,sysline)
        print exeline
        os.system(exeline)
    
    

