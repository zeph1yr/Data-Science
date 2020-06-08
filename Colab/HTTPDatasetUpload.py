from google.colab import drive 
drive.mount('/content/gdrive') 

import requests  
file_url = "http://1.droppdf.com/files/5iHzx/automate-the-boring-stuff-with-python-2015-.pdf"
    
r = requests.get(file_url, stream = True)  
  
with open("/content/gdrive/My Drive/python.pdf", "wb") as file:  
    for block in r.iter_content(chunk_size = 1024): 
         if block:  
             file.write(block)  
