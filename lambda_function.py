import numpy as np
import tensorflow as tf
import urllib.request 
from distutils.version import StrictVersion
from PIL import Image
from utils import ops as utils_ops
from matplotlib import pyplot as plt

# Object detection imports
from utils import label_map_util
from utils import visualization_utils as vis_util


import json

def lambda_handler(event, context):
    
    res = tf.__version__
    return {
        'statusCode': 200,
        'Payload': json.dumps(res)
    }