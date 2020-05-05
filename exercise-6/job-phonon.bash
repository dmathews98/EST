#!/bin/bash --login
#
#PBS -N qe_job
#PBS -l select=1:ncpus=36
#PBS -l place=scatter:excl
#PBS -l walltime=00:20:00
#PBS -A dc114


# Set number of cores
NSLOTS=36

# Make sure any symbolic links are resolved to absolute path
export PBS_O_WORKDIR=$(readlink -f $PBS_O_WORKDIR)

# Change to the directory that the job was submitted from
cd $PBS_O_WORKDIR

# Load the Quantum Espresso module
module load qe
module load mpt

# SCF calculation on normal k-point mesh
mpiexec_mpt -ppn $NSLOTS -n $NSLOTS pw.x < si.scf.in > si.scf.out

# DFPT calculation on regular q-point mesh
mpiexec_mpt -ppn $NSLOTS -n $NSLOTS ph.x < si.ph.in > si.ph.out

# Postprocessing - all these steps can be done interactively, if needed.
# Convert dynamical matrix to real space force constants
mpiexec_mpt -ppn 1 -n 1 q2r.x < q2r.in > q2r.out

# Determine phonon dispersion curves along path Gamma-X-W-K-Gamma-L
mpiexec_mpt -ppn 1 -n 1 matdyn.x < si.ph-disp.in > si.ph-disp.out

# Determine phonon density of states on denser q-point grid
mpiexec_mpt -ppn 1 -n 1 matdyn.x < si.ph-dos.in > si.ph-dos.out
