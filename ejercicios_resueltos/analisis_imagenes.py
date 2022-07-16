import cv2
import tkfilebrowser
from time import sleep
import numpy as np
from math import ceil

# Preguntamos la ruta para guardar el video al usuario
video_direction = tkfilebrowser.asksaveasfilename(title="Seleccione donde guardar el video", filetypes=[("Videos", "*.avi")])

# Inicializamos el objeto CascadeClassifier para detectar rostros
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture('example.mp4')  # Inicializamos el objeto VideoCapture para grabar
fps = cap.get(cv2.CAP_PROP_FPS)
size = (int(cap.get(3)), int(cap.get(4)))  # Obtenemos la resolución del video
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Esto es el codec para escribir el video
out = cv2.VideoWriter(video_direction, fourcc, fps, (1280, 720))

while True:
    ret, frame = cap.read()  # Leemos un frame del video
    if not ret:
        break
    fr = cv2.resize(frame, (1280, 720))  # Redimensionamos el frame
    blurred_img = cv2.GaussianBlur(fr, (0, 0), 20)  # Creamos una versión pixelada de todo el frame

    # Creamos una máscara de la misma resolución pero completamente negra
    # Añadiremos caras en la máscara y luego la usaremos como filtro para mezclar el frame con el frame pixelado
    mask = np.zeros((720, 1280, 3), dtype=np.uint8) 

    gray = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)  # Versión blanco y negro del frame, necesaria para las detecciones con haarcascades
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for (x, y, w, h) in faces:  # Las caras vienen en formato (x de la esquina superior izquierda, y de la esquina superior izquierda, ancho, alto)
        # Como lo vamos a cubrir con un círculo, tomamos el mayor radio
        if w > h:
            may = w
        else:
            may = h
        # Creamos un círculo blanco sobre el espacio de la cara, pero en la máscara
        mask = cv2.circle(mask, (ceil((x + x + w) / 2), ceil((y + y + h) / 2)), ceil(may / 2), (255, 255, 255), -1)
    
    # Mezclamos el frame con el frame pixelado usando la máscara
    # Donde la máscara sea blanca, implica que hay una cara y por tanto tomaremos el frame pixelado, donde no, tomaremos el frame
    fr_ = np.where(mask != (255, 255, 255), fr, blurred_img)
    cv2.imshow('frame', fr_)  # Enseñamos el frame al usuario
    out.write(fr_)  # Escribimos el frame en el video
    if cv2.waitKey(1) == 27:  # Si se presiona la tecla ESC se sale del ciclo
        break
    sleep(0.00001)
cv2.destroyAllWindows()
out.release()
cap.release()
