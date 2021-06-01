import os
import tensorflow as tf
os.environ["CUDA_VISIBLE_DEVICES"] = '0'
gpus = tf.config.list_physical_devices('GPU')
selected = gpus[0]
tf.config.set_visible_devices(selected, 'GPU')
tf.config.experimental.set_memory_growth(selected, True)
memory_limit = 10000
tf.config.experimental.set_virtual_device_configuration( selected, [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=memory_limit)])
