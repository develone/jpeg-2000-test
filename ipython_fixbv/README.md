# Introduction
This repository contains a of IPython notebooks
with MyHDL exercises.  These exercises can be used as a 
learning tool to learn hardware description and MyHDL.
It is also doing the JPEG 2000 for conversion from Python to HDL.


## Getting Started
Should be running IPython 2.1.0 or newer
Currently pip can not be used to install myhdl_tools or myhdl_09dev_fixbv.

    >> hg clone https://bitbucket.org/cfelton/myhdl_tools
    >> cd myhdl_tools
    >> As root or sudo 
    >> python setup.py install

    >> hg clone https://bitbucket.org/cfelton/myhdl_09dev_fixbv
    >> cd myhdl_09dev_fixbv
    >> hg checkout 0.9-dev
    >> As root or sudo 
    >> python setup.py install

First, clone the repository and run the ipython notebook in the 
cloned workspace:

    >> git clone https://github.com/develone/jpeg-2000-test.git
    >> cd ipython_fixbv  
    >> ipython notebook --pylab=inline

