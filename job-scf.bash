#!/bin/bash --login
#
#PBS -N qe_job
#PBS -l select=1:ncpus=36
#PBS -l place=scatter:excl
#PBS -l walltime=00:30:00
#PBS -A dc114

# Determine number of cores requested
NSLOTS=36

# Make sure any symbolic links are resolved to absolute path
export PBS_O_WORKDIR=$(readlink -f $PBS_O_WORKDIR)

# Change to the directory that the job was submitted from
cd $PBS_O_WORKDIR

# Load QE and MPI modules
module load qe
module load mpt

Ecut=($(seq 20 5 200))

for i in "${Ecut[@]}"
do
	sed -i "s/ecutwfc.*/ecutwfc = ${i}/g" quartz.scf-us.in
	sed -i "s/ecutwfc.*/ecutwfc = ${i}/g" quartz.scf-mt.in
	
	# Run the Quantum Espresso executable "pw.x"
	mpiexec_mpt -ppn $NSLOTS -n $NSLOTS pw.x < quartz.scf-us.in > quartz.scf-us.out
	mpiexec_mpt -ppn $NSLOTS -n $NSLOTS pw.x < quartz.scf-mt.in > quartz.scf-mt.out

	usE=$(sed -n -e 's/^.*!    total energy              =  //p' quartz.scf-us.out | sed "s/ Ry//g")
	mtE=$(sed -n -e 's/^.*!    total energy              =  //p' quartz.scf-mt.out | sed "s/ Ry//g")

	usT=$(sed -n -e 's/^.*PWSCF        :   //p' quartz.scf-us.out | awk '{print $1}' | sed "s/s//g")
	mtT=$(sed -n -e 's/^.*PWSCF        :   //p' quartz.scf-mt.out | awk '{print $1}' | sed "s/s//g")


	printf "%s %s %s\n" $i $usE $usT >> quartz-us.txt
	printf "%s %s %s\n" $i $mtE $mtT >> quartz-mt.txt
	
done
