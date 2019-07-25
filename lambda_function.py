import numpy as np
import tensorflow as tf
import PIL
import matplotlib
from distutils.version import StrictVersion
from PIL import Image
from utils import ops as utils_ops
from matplotlib import pyplot as plt

# Object detection imports
from utils import label_map_util
from utils import visualization_utils as vis_util


import json

def lambda_handler(event, context):
    
    tf_version = tf.__version__
    pil_version = PIL.__version__
    np_version = np.version.version
    matplotlib_version = matplotlib.__version__
    
    v_dict={} #initialize dicitionary 
    
    v_dict.update(tensorflow=tf_version)
    v_dict.update(pil=pil_version)
    v_dict.update(numpy=np_version)
    v_dict.update(matplotlib=matplotlib_version)
    
    return {
        'statusCode': 200,
        'Payload': json.dumps(v_dict)
    }