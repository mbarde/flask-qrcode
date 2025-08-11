import os


path = '/home/mbarde/projects/flask-qrcode/codes/'
sizeInBytes = sum(os.path.getsize(path + f) for f in os.listdir(path) if os.path.isfile(path + f))
sizeInMB = sizeInBytes / 1000000
print(sizeInMB)