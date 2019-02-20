import subprocess
import sys
import os
import argparse
import shutil

def extractSchema(project, dataset, table):
    cmd = "bq show --schema --format=prettyjson {}:{}.{}".format(project, dataset, table)
    p = subprocess.Popen(cmd.strip().split(" "), stdout=subprocess.PIPE)
    lines = p.communicate()[0].splitlines()

    path = "schema/" + dataset + "." + table + ".schema"
    with open(path, mode='w') as f:
        f.writelines(lines)

if os.path.exists("schema"):
    shutil.rmtree("schema")
os.mkdir("schema")

parser = argparse.ArgumentParser()
parser.add_argument("--project", type=str)
parser.add_argument("--dataset", type=str)
args = parser.parse_args()

cmd = "bq ls {}:{}".format(args.project, args.dataset)
p = subprocess.Popen(cmd.strip().split(" "), stdout=subprocess.PIPE)
lines = p.communicate()[0].splitlines()
for line in lines:
    s = line.strip().split(" ")
    if 'TABLE' in s:
        table = s[0]
        extractSchema(args.project, args.dataset, table)





