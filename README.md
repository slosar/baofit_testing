baofit_testing
==============

A system to test the baofit package in a controlled fashion

Workflow
--------

There are two programs:

  *  bin/makeinis.py
  *  bin/subbao.py

The first one creates ini files in the inis directory. These are flux/delta/data and xu/aln agnostic. One
ini file per "testing unit".

The second one actually submits jobs for analysis. It takes three arguments:
first argument is what to do delta/flux/data_xu/aln.  For example flux_xu means flux with the xu parametrization.
second argument is the ini file to use
third argument is which realizations, e.g. 1-15 (17 = ALL, 18 ALL_ALT).

For example

bin/subbao.py flux_xu inis/bao_ampl.ini 18

will submit one job to analyze flux mocks, ALL_ALT with inis/bao_ampl.ini.
It will create a set of files in outputs/bao_ampl/flux_xu.ALL_ALT.*



To start
---------
Try this:

   mkdir inis
   bin/makeinis.py 
   ln -s ~/work/kirkby/baofit/models models
   ln -s ../BOSS_3D/output data
   mkdir output
   bin/subbao.py flux_xu inis/bao_ampl.inii 18
