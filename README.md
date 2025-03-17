# README

Generate the Apptainer image:

```bash
apptainer build ~/images/connectivity_measure.sif docker://ghcr.io/yanting-yang/connectivity_measure:latest
```

Submit sbatch job:

```bash
bash run.sh
```
