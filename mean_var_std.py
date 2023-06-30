import numpy as np

def calculate(list):
  #raises exception if the list does not contain nine elements
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  else:
    #convert list into a 3x3 matrix
    matrix = np.array(list).reshape(3, 3)
    #computes all values using numpy functions and converts them to lists
    calculations = { 
      'mean' : [np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(),np.mean(matrix)],
      'variance': [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), np.var(matrix)],
  'standard deviation': [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), np.std(matrix)],
  'max': [np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), np.max(matrix)],
  'min': [np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), np.min(matrix)],
  'sum': [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), np.sum(matrix)]
  }

  return calculations