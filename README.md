# ivul_cluster_introduction
This repo is intended to show examples on how to run massive parallel jobs in the ivul computing cluster

Extracting Improved Trajectories
================================
module load python/2.7.9 <br />
mkdir /vccscratch/$(id -u -n)/output_features <br />
cd /vccscratch/$(id -u -n)/ <br />
git clone https://github.com/cabaf/ivul_cluster_introduction.git <br />
cd ivul_cluster_introduction <br />
python generate_job.py video_list.json /vccscratch/cabafd/output_features/ feat_extract_$(id -u -n) <br />
sbatch feat_extract_$(id -u -n) <br />
