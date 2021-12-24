from sklearn.preprocessing import StandardScaler
import time
from sklearn import decomposition

from sklearn.cluster import KMeans
import shutil
import math
import os
import argparse
from skimage.transform import resize
from skimage import img_as_bool
from natsort import 
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
