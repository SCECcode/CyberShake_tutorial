# -it create interactive interface
# The username is coded in the build.py script
# The image name is coded in the build.py script
#
docker run -it --mount type=bind,source="$(pwd)"/target,destination=/home/cs_data_user/target sceccode/cs_data_tutorial
