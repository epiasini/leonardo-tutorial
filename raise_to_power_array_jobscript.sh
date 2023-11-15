#!/bin/bash

#SBATCH --nodes=1
#SBATCH --time=00:05:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=2GB             # memory requested, per cpu
#SBATCH --account=Sis23_piasini       # account name
#SBATCH --partition=boost_usr_prod # partition name
#SBATCH --job-name=raise_to_power
#SBATCH --mail-type=ALL
#SBATCH --mail-user=epiasini@sissa.it
#SBATCH --output=/leonardo/home/userexternal/epiasini/sissa/lab_activities/lab_teachings/version_control/out/%x.%A.%3a.out
#SBATCH --error=/leonardo/home/userexternal/epiasini/sissa/lab_activities/lab_teachings/version_control/out/%x.%A.%3a.err
#SBATCH --array=0-20


source $HOME/virtualenvs/dl/bin/activate

cd $HOME/penn/projects/complexity/experiments/pavlovia_full/src/analysis/scripts/

srun --unbuffered time python raise_to_power_array.py ${SLURM_ARRAY_TASK_ID}

