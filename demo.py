from infer import InferenceHelper
from PIL import Image

infer_helper = InferenceHelper(dataset='kitti')

# # predict depth of a batched rgb tensor
# example_rgb_batch = ...  
# bin_centers, predicted_depth = infer_helper.predict(example_rgb_batch)

# predict depth of a single pillow image
# img = Image.open("test_imgs/classroom__rgb_00283.jpg")  # any rgb pillow image
# bin_centers, predicted_depth, viz = infer_helper.predict_pil(img, visualized=True)
# viz.show()
# predict depths of images stored in a directory and store the predictions in 16-bit format in a given separate dir
infer_helper.predict_dir("/home/khmt/DepthGuys/RTM3Dv2/kitti_format/data/kitti/image", "/home/khmt/DepthGuys/RTM3Dv2/kitti_format/data/kitti/depth_adabin")