import tensorflow as tf

import numpy as np
import os
import time
import functools
import util


print("tf version is: ", tf.__version__)
print("is gpu available? ", "Yes" if tf.test.is_gpu_available() else "No")

# Dataset of thousands of Irish folk songs, represented in the ABC notation.
path_to_file = tf.keras.utils.get_file('irish.abc', 'https://raw.githubusercontent.com/aamini/introtodeeplearning_labs/2019/lab1/data/irish.abc')

# test: listen to get a better sense of the dataset
text = open(path_to_file).read()
# length of text is the number of characters in it
# Take a look at the first 250 characters in text
vocab = sorted(set(text))

# Creating a mapping from unique characters to indices
char2idx = {u:i for i, u in enumerate(vocab)}
text_as_int = np.array([char2idx[c] for c in text])

# Create a mapping from indices to characters
idx2char = np.array(vocab)
