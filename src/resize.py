import glob 
import cv2
# Path con Resonancias originales
path = "/content/original/*"
save_path = "/content/resized/"
img_number = 1 
size = 200

for file in glob.glob(path):
  image = cv2.imread(file)
  image = cv2.resize(image, (size, size))
  cv2.imwrite(save_path+str(img_number)+".jpg", image)
  img_number += 1
