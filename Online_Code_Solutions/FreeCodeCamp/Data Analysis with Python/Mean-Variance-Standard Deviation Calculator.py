import numpy as np

def calculate(list):
  # check for 9 digits
  if len(list) != 9:
     raise ValueError("List must contain nine numbers.")
  
  # covert to array
  ls = np.array(list)
  # mean for columns(axis1), rows(axis2), all nums
  mean_rows = [ls[[0,1,2]].mean(), ls[[3,4,5]].mean(), ls[[6,7,8]].mean()]
  mean_cols = [ls[[0,3,6]].mean(), ls[[1,4,7]].mean(), ls[[2,5,8]].mean()]

  # variance for columns(axis1), rows(axis2), all nums
  var_rows = [ls[[0,1,2]].var(), ls[[3,4,5]].var(), ls[[6,7,8]].var()]
  var_cols = [ls[[0,3,6]].var(), ls[[1,4,7]].var(), ls[[2,5,8]].var()]  

  # standard deviation for columns(axis1), rows(axis2), all nums
  std_rows = [ls[[0,1,2]].std(), ls[[3,4,5]].std(), ls[[6,7,8]].std()]
  std_cols = [ls[[0,3,6]].std(), ls[[1,4,7]].std(), ls[[2,5,8]].std()]  

  # max for columns(axis1), rows(axis2), all nums
  max_rows = [ls[[0,1,2]].max(), ls[[3,4,5]].max(), ls[[6,7,8]].max()]
  max_cols = [ls[[0,3,6]].max(), ls[[1,4,7]].max(), ls[[2,5,8]].max()]

  # min for columns(axis1), rows(axis2), all nums
  min_rows = [ls[[0,1,2]].min(), ls[[3,4,5]].min(), ls[[6,7,8]].min()]
  min_cols = [ls[[0,3,6]].min(), ls[[1,4,7]].min(), ls[[2,5,8]].min()]

  # sum for columns(axis1), rows(axis2), all nums
  sum_rows = [ls[[0,1,2]].sum(), ls[[3,4,5]].sum(), ls[[6,7,8]].sum()]
  sum_cols = [ls[[0,3,6]].sum(), ls[[1,4,7]].sum(), ls[[2,5,8]].sum()]
  
  return {
  'mean': [mean_cols, mean_rows, ls.mean()],
  'variance': [var_cols, var_rows, ls.var()],
  'standard deviation': [std_cols, std_rows, ls.std()],
  'max': [max_cols, max_rows, ls.max()],
  'min': [min_cols, min_rows, ls.min()],
  'sum': [sum_cols, sum_rows, ls.sum()]
}
