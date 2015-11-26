import json
import os
from argparse import ArgumentParser

if __name__ == "__main__":
    """
        Extract Improved Dense Trajectories from a chunked batch of files.
          Args:
            - id: chunk identifier.
            - task_array: json file containing the chunked list.
    """
    parser = ArgumentParser()
    parser.add_argument("id", type=int)
    parser.add_argument("task_array")
    args = parser.parse_args()
    with open(args.task_array, "r") as fobj:
        data = json.load(fobj)["%d" % args.id]
    for x in data:
        cmd = "./extract_idt.sh %s %s" % (x["video_filename"], x["feature_filename"])
        print cmd
        os.system(cmd)
