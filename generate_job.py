import os
import json
from argparse import ArgumentParser
import numpy as np

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

def slurm_job_template(jobid, nr_jobs, cmd):
    tt = """#!/bin/bash -l
#SBATCH --array=0-%d 
#SBATCH --time=0-72:00
#SBATCH --job-name=%s
#SBATCH --error=job.%%J.err
#SBATCH --output=job.%%J.out
module load python/2.7.9
%s""" % (nr_jobs-1, jobid, cmd)
    return tt

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("video_list")
    parser.add_argument("outputdir")
    parser.add_argument("job_filename")
    parser.add_argument("--nr_jobs", default=200, type=int)
    parser.add_argument("--jobid", default="activitynet_idt_extract")
    args = parser.parse_args()
    
    # Load list of videos
    with open(args.video_list, "r") as fobj:
        data = json.load(fobj)
    v = []
    for f in data:
        f_base = os.path.basename(f)
        v.append({"video_filename": f, 
                  "feature_filename": os.path.join(args.outputdir, 
                                                   "%s.feature.gz" % f_base)})

    # Split into chunks according to number of jobs
    v_processed = list(chunks(v, int(np.ceil((len(v)*1.0)/(args.nr_jobs*1.0)))))

    # Save splitted list
    output_list_filename = "array_%s" % args.video_list
    with open(output_list_filename, "w") as fobj:
        fobj.write(json.dumps(v_processed))

    # Creates slurm job file
    cmd = "python extract_idt.py $SLURM_ARRAY_TASK_ID %s" % output_list_filename
    template_job = slurm_job_template(args.jobid, args.nr_jobs, cmd)
    with open(args.job_filename, "w") as fobj:
        fobj.write(template_job)
