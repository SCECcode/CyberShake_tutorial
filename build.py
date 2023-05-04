#!/usr/bin/env python3
# This script is used to update the inputs models and generate new docker build scripts for each configuration

import os
import datetime

# build date tag
dt=datetime.datetime.today()
month=dt.month
day=dt.day
mdate="%02d%02d"%(month,day)


cmd = "docker build --progress=plain --no-cache=false -f Dockerfile . -t cs_data_tutorial " \
"--build-arg APP_UNAME=cs_data_user --build-arg APP_GRPNAME=`id -g -nr` " \
"--build-arg APP_UID=`id -u` --build-arg APP_GID=`id -g` --build-arg BDATE=%s"%(mdate)

os.system(cmd)

cmd = "docker tag cs_data_tutorial sceccode/cs_data_tutorial"
print("Running: ",cmd)
os.system(cmd)
