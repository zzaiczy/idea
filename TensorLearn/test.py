import tensorflow as tf
feature = [1, 2, 3]
frame_feature = list(map(lambda i:
                         tf.train.Feature(
                             int64_list=tf.train.Int64List(value=[i])), feature))
print(frame_feature)
