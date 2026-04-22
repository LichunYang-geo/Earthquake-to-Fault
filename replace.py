# %%
import os
import shutil

current_path = os.getcwd()

h3d_road = f"{current_path}/hough-3d-lines"

fault_road = f"{current_path}/OutputFile"
os.makedirs(fault_road, exist_ok=True)
# %%
# origin file road
origin_h3d_main   = f"{h3d_road}/hough3dlines.cpp"
origin_pointcloud = f"{h3d_road}/pointcloud.cpp"
origin_vector3d   = f"{h3d_road}/vector3d.cpp"
origin_vector3d_h = f"{h3d_road}/vector3d.h"

# replace file road
replace_h3d_main   = f"{current_path}/replace_code/hough3dlines_replaced.cpp"
replace_pointcloud = f"{current_path}/replace_code/pointcloud_replaced.cpp"
replace_vector3d   = f"{current_path}/replace_code/vector3d_replaced.cpp"
replace_vector3d_h = f"{current_path}/replace_code/vector3d_replaced.h"

# %%
# replace file
shutil.copyfile(replace_h3d_main, origin_h3d_main)
shutil.copyfile(replace_pointcloud, origin_pointcloud)
shutil.copyfile(replace_vector3d, origin_vector3d)
shutil.copyfile(replace_vector3d_h, origin_vector3d_h)
# %%
