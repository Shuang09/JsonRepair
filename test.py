import tensorflow as tf
print("GPUs: ", len(tf.config.experimental.list_physical_devices('GPU')))