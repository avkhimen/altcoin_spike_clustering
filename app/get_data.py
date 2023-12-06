import gdown
import os 
  
# path of the directory 
path = os.getcwd() + "/data"
  
# Getting the list of directories 
dir = os.listdir(path)
  
# Checking if the list is empty or not 
if len(dir) == 0: 
    gdown.download("https://drive.google.com/uc?id=16YKyFkYlvawCHv3W7WuTFzM8RYgMRWMt&export=download")

