

## Necessary Packages
import numpy as np


def MinMaxScaler(data):
  """Min Max normalizer.
  
  Args:
    - data: original data
  
  Returns:
    - norm_data: normalized data
  """
  numerator = data - np.min(data, 0)
  denominator = np.max(data, 0) - np.min(data, 0)
  norm_data = numerator / (denominator + 1e-7)
  return norm_data
   
def MinMaxScaler2(data):
  """Min Max normalizer.
  
  Args:
    - data: original data
  
  Returns:
    - norm_data: normalized data
  """
  numerator = data - np.min(data, 0)
  denominator = np.max(data, 0) - np.min(data, 0)
  norm_data = numerator / (denominator + 1e-7)
  return norm_data


def real_data_loading (seq_len):
  """Load and preprocess real-world datasets.
  
  Args:
    - data_name: stock or energy
    - seq_len: sequence length
    
  Returns:
    - data: preprocessed data.
  """  

  #ori_data_f = np.loadtxt('data/sin_clear_20Hz_10Hz.txt', delimiter = "\t")
  #ori_data_a = np.loadtxt('data/sin_noise_20Hz_10Hz.txt', delimiter = "\t")

  #ori_data_f = np.loadtxt('data/EEG_filtered_clear_10Hz.txt', delimiter = "\t")
  #ori_data_a = np.loadtxt('data/EEG_artifacted_clear_10Hz.txt', delimiter = "\t")

  #ori_data_f = np.loadtxt('data/real_EEG_clear.txt', delimiter = "\t")
  #ori_data_f = np.loadtxt('data/1_in2.txt', delimiter = "\t")
  #ori_data_f = np.loadtxt('data/4_in.txt', delimiter = "\t")
  ori_data_f = np.loadtxt('data/2-CoStim_Result_Subjectjtb3_Sess3_Stim2000mA.txt', delimiter = "\t")
  #ori_data_f = np.loadtxt('data/3-CoStim_Result_Subjectlad2_Sess2_Stim2000mA.txt', delimiter = "\t")
  #ori_data_f = np.loadtxt('data/4-CoStim_Result_Subjectlad3_Sess3_Stim2000mA.txt', delimiter = "\t")
  #ori_data_f = np.loadtxt('data/5-CoStim_Result_Subjectlla2_Sess2_Stim2000mA.txt', delimiter = "\t")
  #ori_data_f = np.loadtxt('data/sham.txt', delimiter = "\t")
  #ori_data_f = np.loadtxt('data/sin_f.txt', delimiter = "\t")
  #ori_data_a = np.loadtxt('data/real_EEG_in_clear.txt', delimiter = "\t")
  #ori_data_a = np.loadtxt('data/real_EEG_clear.txt', delimiter = "\t")
  ori_data_a = np.loadtxt('data/2-CoStim_Result_Subjectjtb3_Sess3_Stim2000mA.txt', delimiter = "\t")
  #ori_data_a = np.loadtxt('data/3-CoStim_Result_Subjectlad2_Sess2_Stim2000mA.txt', delimiter = "\t")
  #ori_data_a = np.loadtxt('data/4-CoStim_Result_Subjectlad3_Sess3_Stim2000mA.txt', delimiter = "\t")
  #ori_data_a = np.loadtxt('data/5-CoStim_Result_Subjectlla2_Sess2_Stim2000mA.txt', delimiter = "\t")
  #ori_data_a = np.loadtxt('data/sin_a.txt', delimiter = "\t")
  # Flip the data to make chronological data
  # Normalize the data
  #max = np.max(ori_data_f, 0)
  #min = np.min(ori_data_f, 0)
  min1 = np.min(ori_data_f, 0)
  max1 = np.max(ori_data_f, 0)
  ori_data_f = MinMaxScaler(ori_data_f)
  ori_data_a = MinMaxScaler(ori_data_a)
  # Preprocess the dataset
  temp_data_f = []  
  temp_data_a = []   
  max = []
  min = []
  # Cut data by sequence length
  for i in range(0, len(ori_data_f)-seq_len , seq_len):
    _x = ori_data_f[i:i + seq_len]
    _y = ori_data_a[i:i + seq_len]
    max_x = np.max(_x, 0)*(max1-min1)+min1
    min_x = np.min(_x, 0)*(max1-min1)+min1
    if len(_x)==seq_len:
      temp_data_f.append(_x)
      temp_data_a.append(_y)
      max.append(max_x)
      min.append(min_x)    
  
  return temp_data_f, temp_data_a, max, min, max1, min1

def real_data_loading1 (seq_len):
  """Load and preprocess real-world datasets.
  
  Args:
    - data_name: stock or energy
    - seq_len: sequence length
    
  Returns:
    - data: preprocessed data.
  """  
  #ori_data_a = np.loadtxt('data/sin_noise_20Hz_10Hz.txt', delimiter = "\t")
  #ori_data_a = np.loadtxt('data/EEG_artifacted_clear_10Hz.txt', delimiter = "\t")
  ori_data_a = np.loadtxt('data/2-CoStim_Result_Subjectjtb3_Sess3_Stim2000mA.txt', delimiter = "\t")
  #ori_data_a = np.loadtxt('data/3-CoStim_Result_Subjectlad2_Sess2_Stim2000mA.txt', delimiter = "\t")
  #ori_data_a = np.loadtxt('data/4-CoStim_Result_Subjectlad3_Sess3_Stim2000mA.txt', delimiter = "\t")
  #ori_data_a = np.loadtxt('data/5-CoStim_Result_Subjectlla2_Sess2_Stim2000mA.txt', delimiter = "\t")
  #ori_data_a = np.loadtxt('data/real_EEG_clear.txt', delimiter = "\t")
  #ori_data_a = np.loadtxt('data/sin_a.txt', delimiter = "\t")
  # Flip the data to make chronological data
  # ori_data = ori_data[::-1]
  # Normalize the data
  ori_data_a = MinMaxScaler(ori_data_a)  
  # Preprocess the dataset 
  temp_data_a = []    
  # Cut data by sequence length
  for i in range(0, len(ori_data_a)-seq_len , seq_len ):
    _y = ori_data_a[i:i + seq_len]
    if len(_y)==seq_len:
     temp_data_a.append(_y)    

  return temp_data_a