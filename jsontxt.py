import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
from PIL import Image

with open('../../akimoto/5beff081cf683c10dd21db1d613be0da-asset.json') as f:
    result = json.load(f)

height = result["regions"][0]['boundingBox']['height']
#height
width = result["regions"][0]['boundingBox']['width']

x1 = result["regions"][0]['points'][0]['x']
x2 = result["regions"][0]['points'][1]['x']
x3 = (x1 + x2)/2

y1 = result["regions"][0]['points'][0]['y']
y2 = result["regions"][0]['points'][2]['y']
y3 = (y1+y2)/2

name = result['asset']['name']
name = result['asset']['name']

save_path = './labels/' + name.replace
('jpg', 'txt')

_class = 0

with open(f"{save_path}", "w") as f:
        
            f.write("%d %.06f %.06f %.06f %.06f\n" % (_class, x3, y3, width, height))
