from google.colab import drive, files
drive.mount('/content/gdrive') 

files.upload() #this will prompt you to update the json

!pip install --upgrade pip
!pip install -q kaggle==1.5.6
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!ls ~/.kaggle
!chmod 600 /root/.kaggle/kaggle.json

!kaggle competitions download -c <Competition Name> -p /content/gdrive/My\ Drive/ <Folder Name>
