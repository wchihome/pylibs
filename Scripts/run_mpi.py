#!/usr/bin/env python3
'''
Template for running MPI job on sciclone/ches @VIMS
Note: For MPI jobs demanding large memory, use small ppn
'''
from pylib import *
import time

#-----------------------------------------------------------------------------
#Input
#-----------------------------------------------------------------------------

#resource requst 
walltime=5 #hours
qnode='bora'; nnode=2; ppn=20      #bora, ppn=20
#qnode='vortex'; nnode=10; ppn=12   #vortex, ppn=12
#qnode='x5672'; nnode=2; ppn=8      #hurricane, ppn=8
#qnode='femto'; nnode=1; ppn=2      #femto,ppn=32, not working yet

#-----------------------------------------------------------------------------
#pre-processing
nproc=nnode*ppn
bdir=os.path.abspath(os.path.curdir)

#-----------------------------------------------------------------------------
#on front node; submit jobs in this section
#-----------------------------------------------------------------------------
if os.getenv('param')==None and os.getenv('job_on_node')==None:
    args=sys.argv
    param=[bdir,args[0]]
    
    #submit job on node
    if qnode=='femto': 
        scode='sbatch --export=param="{} {}" -J mpi4py -N {} -n {} -t {:02}:00:00 {}'.format(*param,nnode,nproc,walltime,args[0])
    else:
        scode='qsub {} -v param="{} {}", -N mpi4py -j oe -l nodes={}:{}:ppn={} -l walltime={:02}:00:00'.format(args[0],*param,nnode,qnode,ppn,walltime)
    print(scode); os.system(scode)
    os._exit(0)

#-----------------------------------------------------------------------------
#still on front node, but in batch mode; running jobs in this section
#-----------------------------------------------------------------------------
if os.getenv('param')!=None and os.getenv('job_on_node')==None:
    param=os.getenv('param').split();
    param=[int(i) if i.isdigit() else i for i in param]
    bdir=param[0]; code=param[1]
    os.chdir(bdir)

    if qnode=='x5672' or qnode=='vortex':
       rcode="mvp2run -v -e job_on_node=1 -e bdir='{}' {}>& screen.out".format(bdir,code)
    elif qnode=='bora':
       rcode="mpiexec -x job_on_node=1 -x bdir='{}' -n {} {}>& screen.out".format(bdir,nproc,code)
    elif qnode=='femto':
       pypath='/sciclone/home10/wangzg/bin/pylibs/Scripts/:/sciclone/home10/wangzg/bin/pylibs/Utility/'
       rcode="srun --export=job_on_node=1,bdir='{}',PYTHONPATH='{}' {}>& screen.out".format(bdir,pypath,code)
    print(rcode); os.system(rcode)
    os._exit(0)

#-----------------------------------------------------------------------------
#on computation node
#-----------------------------------------------------------------------------
#enter working dir
bdir=os.getenv('bdir'); os.chdir(bdir)

#get nproc and myrank
comm=MPI.COMM_WORLD
nproc=comm.Get_size()
myrank=comm.Get_rank()
if myrank==0: t0=time.time()

#do MPI work on each core
print('myrank={}, nproc={}, host={}'.format(myrank,nproc,os.getenv('HOST'))); sys.stdout.flush()

#finish MPI jobs
comm.Barrier()
if myrank==0: dt=time.time()-t0; print('total time used: {} s'.format(dt)); sys.stdout.flush()
if qnode=='vortex': 
   sys.exit(0)
elif qnode=='x5672':
   os._exit(0)