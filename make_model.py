
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

import numpy as np
import tensorflow as tf

def main():
  training_set = tf.contrib.learn.datasets.base.load_csv_with_header(
      filename="random_subset_of_cases.csv",
      target_dtype=np.int,
      features_dtype=np.float32)
  test_set = tf.contrib.learn.datasets.base.load_csv_with_header(
      filename="all_possible_cases.csv",
      target_dtype=np.int,
      features_dtype=np.float32)

  feature_columns = [tf.feature_column.numeric_column("x", shape=[training_set.data.shape[1]])]

  classifier = tf.estimator.DNNClassifier(feature_columns=feature_columns,
                                          hidden_units=[10,10],
                                          model_dir="./tensorflow_model"
                                          )

  train_input_fn = tf.estimator.inputs.numpy_input_fn(
      x={"x": np.array(training_set.data)},
      y=np.array(training_set.target),
      num_epochs=None,
      shuffle=True)

  # Train model.
  classifier.train(input_fn=train_input_fn, steps=6000)

  # Define the test inputs
  test_input_fn = tf.estimator.inputs.numpy_input_fn(
      x={"x": np.array(test_set.data)},
      y=np.array(test_set.target),
      num_epochs=1,
      shuffle=False)

  # Evaluate accuracy.
  accuracy_score = classifier.evaluate(input_fn=test_input_fn)["accuracy"]
  print("\nTest Accuracy: {0:f}\n".format(accuracy_score))

  new_samples = np.array(
      [[1,0,0,0,1,1,0,0,1]], dtype=np.float32)
  predict_input_fn = tf.estimator.inputs.numpy_input_fn(
      x={"x": new_samples},
      num_epochs=1,
      shuffle=False)
  predictions = list(classifier.predict(input_fn=predict_input_fn))
  print(predictions)
  predicted_classes = [p["classes"] for p in predictions]
  print(
      "New Samples, Class Predictions:    {}\n"
      .format(predicted_classes))

if __name__ == "__main__":
    main()