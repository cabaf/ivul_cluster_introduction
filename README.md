# ivul_cluster_introduction
This repo is intended to show examples on how to run massive parallel jobs in the ivul computing cluster

Extracting Improved Trajectories
================================
module load python/2.7.9
mkdir /vccscratch/`id -u -n`/output_features
cd /vccscratch/`id -u -n`/
git clone https://github.com/cabaf/ivul_cluster_introduction.git
cd ivul_cluster_introduction
python generate_job.py video_list.json /vccscratch/cabafd/output_features/ feat_extract_`id -u -n`
sbatch feat_extract_`id -u -n`
