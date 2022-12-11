import cv2
import csv
import numpy as np
import torch
import torchvision.transforms as transforms
import torchvision.io as io
import matplotlib.pyplot as plt
import matplotlib.cm as cm

videopath = 'Videos\HD_CCTV_retail_store.mp4'
labelpath = 'runs\detect\exp\HD_CCTV_retail_store.txt'

img = cv2.imread('background.png')
x, y, w, h = cv2.selectROI('location', img, False)
cv2.destroyAllWindows()
           

with open(labelpath, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    reader = list(reader)
    head_coord_rec = {i:[] for i in range(int(reader[-1][0]) + 1)}
    for row in reader:
        if int(row[1]) == 1:
            if not (((x / img.shape[1])  < float(row[2]) < ((x + w) / img.shape[1])) and (((x + w) / img.shape[1]) < float(row[3]) < ((y + h) / img.shape[0]))):
                head_coord_rec[int(row[0])].append((float(row[2]), float(row[3])))


video = cv2.VideoCapture(videopath)
a, image = video.read()
cv2.imwrite('background.png', image)

img = io.read_image('background.png')
H = img.shape[1]
W = img.shape[2]

heatmap = torch.zeros(1, H, W)
for k in head_coord_rec:
    for xy in head_coord_rec[k]:
        x, y = round(xy[0] * W), round(xy[1] * H)
        heatmap[0][y][x] += 1

heatmap = transforms.GaussianBlur(101, sigma=10)(heatmap)
heatmap = heatmap ** 0.4

heatmap = heatmap.permute(1, 2, 0)
heatmap /= heatmap.max()

heat_mag = torch.cat([heatmap], dim=2).numpy()
heat_mag = 1 / (1 +np.exp(-50*heat_mag+3.5))
heatmap = (heatmap * 255).to(torch.uint8)

jet = cm.get_cmap("jet")
jet_colors = jet(np.arange(256))[:, :3]
jet_heatmap = jet_colors[heatmap.reshape(H, W)]

img = img.permute(1, 2, 0).numpy()

alpha = 0.4

superimposed_img = jet_heatmap * 255 * alpha * heat_mag + img * (1-alpha * heat_mag)
superimposed_img = superimposed_img.astype(np.uint8)
superimposed_img = cv2.cvtColor(superimposed_img, cv2.COLOR_BGR2RGB)
cv2.imwrite('heatmap_remove.png', superimposed_img)
