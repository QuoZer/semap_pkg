import numpy as np
import matplotlib.pyplot as plt
import open3d as o3d
from PIL import Image

from semap import Mapper

dataset_path = "./config/objects.yaml" 
pcd_path = "./clc12_ag112_tuned.pcd" 
esdf_path = "./vox_esdf_02m_clc12_ag112_tuned_new_rotated.pcd"

pcd = o3d.io.read_point_cloud(pcd_path)
esdf = o3d.t.io.read_point_cloud(esdf_path)
tf = [0, 5, 0]

mpr = Mapper(vis=False)
mpr.load_dataset(dataset_path) # 35 15
mpr.setup_point_clouds(pcd, "Map", 14, False)
mpr.setup_intensity_map(esdf, "ESDF", 1, False)
# viewer3d.load_trajectories(["traj1.pcd",
#                             "traj2.pcd"], -20)

mpr.m2d.set_resolution(0.2, 60, -2)
# mpr.m3d.explode_view()
# mpr.m3d.avg_nn_dist(50)
# segmented_img, _, esdf_grid = mpr.m2d.cluster_dbscan(True, 0.5, 0.8)
# matplotlib.image.imsave('seg_rooms_max.png', segmented_img)

# mpr.m2d.fuse_pointclouds(tf)
# mpr.m3d.show_esdf(-8, 8)
# mpr.m3d.show_esdf(-2, 0.496)
# mpr.m2d.draw_esdf_slice()
# mpr.m3d.rebuild_rooms_esdf()
# mpr.m3d.rebuild_rooms() 
# mpr.m3d.draw_class_distribution()

# mpr.draw_nn_perf()
# mpr.val_esdf()
# mpr.test_cluster_params()
# mpr.compare_esdf_compression()

try:
    while mpr.vis:        
        mpr.m3d.filter_point_clouds(voxel=True)
        #  Update the cloud and tick the GUI application
        mpr.viewer.update_o3d_scene()
        mpr.viewer.run_one_tick()
except Exception as e:
    print(e)
