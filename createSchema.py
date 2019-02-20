import subprocess
import sys
import os

project = sys.argv[1]

cmd = "ls schema"
p = subprocess.Popen(cmd.strip().split(" "), stdout=subprocess.PIPE)
lines = p.communicate()[0].splitlines()
for line in lines:
    cmd = "bq mk --table {}:{} schema/{}".format(project, line, line)
    subprocess.check_call(cmd.strip().split(" "))
