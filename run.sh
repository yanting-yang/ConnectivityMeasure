#!/bin/bash
#SBATCH --time=1:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=8G
#SBATCH -o log/%j.out
#SBATCH -e log/%j.err

module load apptainer/1.3.5

apptainer run --cleanenv ~/images/connectivity_measure.sif --input_files ~/datasets/HCP-Aging_processed/*.npy
