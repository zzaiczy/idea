import tensorflow as tf


def generate_tfrecord(tfrecord_filename):
    sequences = [[1], [2, 2], [3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5, 5],
                 [1], [2, 2], [3, 3, 3], [4, 4, 4, 4]]
    labels = [1, 2, 3, 4, 5, 1, 2, 3, 4]
    others = labels[:]

    with tf.io.TFRecordWriter(tfrecord_filename) as f:
        for feature, label in zip(sequences, labels):
            frame_feature = list(map(lambda i: tf.train.Feature(int64_list=tf.train.Int64List(value=[i])), feature))

            example = tf.train.SequenceExample(
                context=tf.train.Features(feature={
                    'label': tf.train.Feature(int64_list=tf.train.Int64List(value=[label]))}),
                feature_lists=tf.train.FeatureLists(feature_list={
                    'sequence': tf.train.FeatureList(feature=frame_feature)
                })
            )
            f.write(example.SerializeToString())
    return 0
