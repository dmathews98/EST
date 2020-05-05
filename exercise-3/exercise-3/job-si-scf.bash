#!/bin/bash --login
#
#PBS -N qe_job
#PBS -l select=1:ncpus=36
#PBS -l place=scatter:excl
#PBS -l walltime=0:20:00
#PBS -A dc114

NSLOTS=36

# Make sure any symbolic links are resolved to absolute path
export PBS_O_WORKDIR=$(readlink -f $PBS_O_WORKDIR)

# Change to the directory that the job was submitted from
cd $PBS_O_WORKDIR

# Load QE and MPI modules
module load qe
module load mpt


# Run the Quantum Espresso executable "pw.x"
mpiexec_mpt -ppn $NSLOTS -n $NSLOTS pw.x < si-fcc.scf.in > si-fcc.scf.out

