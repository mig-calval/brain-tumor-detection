def resizer(origin, destiny, size): 
  """
  Resizes the MRIs in origin folder 
  Arguments:
    origin: original MRI path. e. g. "/content/original/*"
    destiny: path where resized MRI will be stored.  e. g. "/content/resized/"
    size: size of the new size x size images
  Returns:
    Resized size x size MRIs in the destiny path 
    """
  import glob 
  import cv2
  # Path con Resonancias originales
  path = origin
  save_path = destiny
  img_number = 1 

  for file in glob.glob(path):
    image = cv2.imread(file)
    image = cv2.resize(image, (size, size))
    cv2.imwrite(save_path+str(img_number)+".jpg", image)
    img_number += 1
