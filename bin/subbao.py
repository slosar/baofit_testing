#!/usr/bin/env python
import sys, os
nproc=2
priority="high"
ini = sys.argv[1]
outroot = sys.argv[2]
if (len(sys.argv)>3):
    rlist=sys.argv[3]
    if '-' in rlist:
        beg,end=map(int,rlist.split('-'))
        rlist=range(beg,end+1)
    else:
        rlist=map(int,rlist.split(','))
else:
    rlist=[1]

os.system('mkdir '+outroot)
for r in rlist:
    eo=""
    if r==17:
        r="ALL"
        eo="--reuse-cov=1"
    elif r==18:
        r="ALL_ALT"
    else:
        r=str(r)
        eo="--reuse-cov=1"
    croot=outroot+'/'+r
    name = r+'.'+outroot
    sysline = "OMP_NUM_THREADS=%i baofit -i %s --platelist=lr%s %s --output-prefix=%s. >%s.log 2>%s.err" %(nproc,ini,r,eo,croot,croot,croot)
    exeline = 'nohup wq sub -r "N:%i; priority:%s; mode:bycore1; job_name:%s" -c "source ~/.bashrc; %s" & '%(nproc, priority,name,sysline)
    print exeline
    os.system(exeline)
    
    

