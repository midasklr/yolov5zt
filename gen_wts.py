import torch
import struct
import sys
from utils.torch_utils import select_device

# Initialize
device = select_device('cpu')
pt_file = "/home/hwits/Documents/CarVid/yolov5zt/weights/last.pt"
# Load model
model = torch.load(pt_file, map_location=device)['model'].float()  # load to FP32
model.to(device).eval()

with open('yolov5l.wts', 'w') as f:
    f.write('{}\n'.format(len(model.state_dict().keys())))
    for k, v in model.state_dict().items():
        vr = v.reshape(-1).cpu().numpy()
        f.write('{} {} '.format(k, len(vr)))
        for vv in vr:
            f.write(' ')
            f.write(struct.pack('>f',float(vv)).hex())
        f.write('\n')
