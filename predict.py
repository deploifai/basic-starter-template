import os
import json

# The path of the model in the current project
model_path = os.path.sep.join([os.path.dirname(os.path.realpath(__file__)), "weights.h5"]) 

"""
Put all the logic for prediction here
"""
def predict(input_args):
  output = {
    data: input_args
  }

  """
  The response must be JSON parsable
  This can be a common issue when working with some kinds of data, for example: numpy values or ndarrays
  """
  if not json.loads(output):
    return {}
  return output


if __name__ == "__main__":
  input_args = ["My sample data"]
  predict(input_args)