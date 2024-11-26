import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os
from PIL import Image

img = Image.open("/home/petar/GitHub/Radar/radar.png")
img.save("/home/petar/GitHub/Radar/radar_fixed.png")

image_path = input("/home/petar/GitHub/Radar/radar_fixed.png")
image_path = os.path.abspath(image_path)
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)






