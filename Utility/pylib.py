#---------------------------------------------------------------------
#import system lib
#---------------------------------------------------------------------
import os,sys

Libs=['pylib','mylib','schism_file']
if not set(Libs).issubset(set(sys.modules.keys())):
   #---------------------------------------------------------------------
   #spyder pylab library
   #C:/Program Files/Python/Python3[57]/Lib/site-packages/matplotlib/pylab.py
   #---------------------------------------------------------------------
   pversion=sys.version.split(' ')[0]
   #from pylab import *
   #print(pversion)

   #---------------------------------------------------------------------
   #libraries of packages
   #---------------------------------------------------------------------
   #matplotlib
   import matplotlib as mpl
   if os.getenv('HOSTNAME') is not None:
      if 'frontera' in os.getenv('HOSTNAME'): mpl.use('tkagg') 
   from matplotlib import pyplot as plt
   from matplotlib import cbook, mlab
   from matplotlib.dates import * 
   from matplotlib.pyplot import *

   #numpy
   import numpy as np
   from numpy import *
   from numpy.random import *
   from numpy.linalg import *
   import numpy.ma as ma
   #from numpy.fft import *

   #scipy
   import scipy as sp
   from scipy import (optimize,interpolate,signal)
   from scipy.fftpack import fft, ifft
   #from scipy import (optimize,interpolate,io,signal)

   #pandas
   import pandas as pd

   #misc
   import re
   import datetime
   #from io import StringIO
   #import imp
   #import importlib as imp

   #proj
   from pyproj import Transformer
   #from pyproj import Proj, transform

   #netcdf
   from netCDF4 import Dataset

   #excel
   try: 
      import xlsxwriter as xw
   except: 
      pass

   #mpi4py
   try:
      from mpi4py import MPI
   except:
       pass

   #url download
   try:
      import urllib
   except:
      pass

   #statistics
   # try:
   #    import skill_metrics as sm
   # except:
   #    pass

   #---------------------------------------------------------------------
   #libraries of self-defined modules
   #---------------------------------------------------------------------
   import mylib
   from mylib import (get_xtick,close_data_loop,datenum,
        loadz,npz_data,save_npz,find_continuous_sections,
        smooth,daytime_length,move_figure,lpfilt,mdivide,signa,
        inside_polygon,command_outputs,near_pts,proj,
        get_prj_file,mfft,read_shapefile_data,write_shapefile_data,
        ReadNC,WriteNC,harmonic_fit,harmonic_analysis,get_hycom,
        get_stat,get_subplot_position,load_bathymetry)
        #convert_matfile_format,

   import schism_file
   from schism_file import (read_schism_hgrid, read_schism_hgrid_ll,read_schism_bpfile,getglob,
        schism_grid,schism_bpfile,sms2gr3,read_schism_vgrid,read_schism_param,write_schism_param)

   if os.getenv('HOME')!=None:
       sys.path.append(os.getenv('HOME'))

   #sys.modules['loadz'] = mylib #in case oldmodule name used
   #sys.modules['read_schism_file'] = schism_file #in case oldmodule name used
   #import mpas_file
   #from mpas_file import (read_mpas_grid)


#------------------------------------------------------------------------------
#for python3.7.7
#pip install matplotlib scipy pyshp netcdf4 xlsxwriter mpi4py pyproj sympy math#skillmetrics
#pip install flake8==3.7.9 autopep8==1.5.2 spyder==4.1.3 (old version flake8 autopep8 may fails,but worked on Vortex)
#pip install skillmetrics

#---------------------------------------------------------------------------
#code discard
#---------------------------------------------------------------------------
#import warnings
#import matplotlib as mpl
#import numpy as np
#import datetime

#if pversion in ['3.5.3',]:
#   #from __future__ import (absolute_import, division, print_function, unicode_literals)
#   #from matplotlib.cbook import (flatten, exception_to_str, silent_list, iterable, dedent)
#   import six
#   from matplotlib.mlab import (
#        amap, base_repr, binary_repr, bivariate_normal, center_matrix, csv2rec,
#        demean, detrend, detrend_linear, detrend_mean, detrend_none, dist,
#        dist_point_to_segment, distances_along_curve, entropy, exp_safe,
#        fftsurr, find, frange, get_sparse_matrix, get_xyz_where, griddata,
#        identity, inside_poly, is_closed_polygon, ispower2, isvector, l1norm,
#        l2norm, log2, longest_contiguous_ones, longest_ones, movavg, norm_flat,
#        normpdf, path_length, poly_below, poly_between, prctile, prctile_rank,
#        rec2csv, rec_append_fields, rec_drop_fields, rec_join, rk4, rms_flat,
#        segments_intersect, slopes, stineman_interp, vector_lengths,
#        window_hanning, window_none)
#   bytes = six.moves.builtins.bytes
#elif pversion in ['3.7.7',]:
#   from matplotlib.cbook import (flatten, silent_list, iterable, dedent)
#   from matplotlib.mlab import (
#        demean, detrend, detrend_linear, detrend_mean, detrend_none,
#        window_hanning, window_none)
#   bytes = __import__("builtins").bytes

##matplotlib
#from matplotlib.dates import (
#    date2num, num2date, datestr2num, strpdate2num, drange, epoch2num,
#    num2epoch, mx2num, DateFormatter, IndexDateFormatter, DateLocator,
#    RRuleLocator, YearLocator, MonthLocator, WeekdayLocator, DayLocator,
#    HourLocator, MinuteLocator, SecondLocator, rrule, MO, TU, WE, TH, FR,
#    SA, SU, YEARLY, MONTHLY, WEEKLY, DAILY, HOURLY, MINUTELY, SECONDLY,
#    relativedelta)

#from matplotlib import cbook, mlab
#try:
#    from matplotlib import pyplot as plt
#    from matplotlib.pyplot import *
#except:
#    pass

##for numpy
#from numpy import *
#from numpy.fft import *
#from numpy.random import *
#from numpy.linalg import *
#import numpy.ma as ma

