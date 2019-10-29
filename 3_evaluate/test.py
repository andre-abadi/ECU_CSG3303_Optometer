""" Remixed from https://github.com/xinntao/ESRGAN/blob/master/test.py """
import os.path as osp
import glob
import cv2
import numpy as np
import torch
import RRDBNet_arch as arch

MODEL_PATH = "models/latest_G.pth"
DEVICE = torch.device("cuda")
# DEVICE = torch.DEVICE('cpu')

TEST_IMG_FOLDER = "input/*"

MODEL = arch.RRDBNet(3, 3, 64, 23, gc=32)
MODEL.load_state_dict(torch.load(MODEL_PATH), strict=True)
MODEL.eval()
MODEL = MODEL.to(DEVICE)

print("Model path {:s}. \nTesting...".format(MODEL_PATH))

IDX = 0
for path in glob.glob(TEST_IMG_FOLDER):
    IDX += 1
    base = osp.splitext(osp.basename(path))[0]
    print(IDX, base)
    # read images
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    img = img * 1.0 / 255
    img = torch.from_numpy(
            np.transpose(img[:, :, [2, 1, 0]], (2, 0, 1))).float()
    img_LR = img.unsqueeze(0)
    img_LR = img_LR.to(DEVICE)

    with torch.no_grad():
        output = MODEL(
                img_LR).data.squeeze().float().cpu().clamp_(0, 1).numpy()
    output = np.transpose(output[[2, 1, 0], :, :], (1, 2, 0))
    output = (output * 255.0).round()
    cv2.imwrite("output/{:s}_rlt.png".format(base), output)
