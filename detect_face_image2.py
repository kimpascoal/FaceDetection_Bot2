import sys
import cv2
import base64
def exportImage():
# Carregar a cascata
# Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Leia a imagem de entrada
# Read the input image
    img = cv2.imread('test2.jpg')

# Converter em escala de cinza
# Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detectar rostos
# Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
   # faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# Desenhe um retângulo ao redor das faces
# Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)


   # for (x, y, w, h) in faces:
       # cv2.rectangle(img1, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Exibe a saída
# Display the output return img
#     cv2.imshow('img', img)
    # cv2.waitKey()

#if args.get("video", None) is None:
	#vs = VideoStream(src=0).start()
	#time.sleep(2.0)

#else:
#	vs = cv2.VideoCapture(args["video"])
    path = 'new_image.jpg'
    cv2.imwrite(path, img)

   # path = 'new_image.jpg'
    #cv2.imwrite(path, img1)

    return path
