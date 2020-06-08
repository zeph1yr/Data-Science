from google.colab import drive
drive.mount('/content/gdrive')

import urllib.request

file_url = "ftp://lhcftp.nlm.nih.gov/Open-Access-Datasets/Malaria/cell_images.zip" 
    
r = urllib.request.urlopen(file_url)  
  
with open("/content/gdrive/My Drive/Colab Notebooks/cell_images.zip", "wb") as file:  
    for block in r: 
         if block:  
             file.write(block)  
