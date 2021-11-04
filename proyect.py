#Importación de recursos
import cv2
import numpy as np

#Iniciamos camara
vc = cv2.VideoCapture(0)
#Primer Rango
#redBajo01 = np.array([0,100,20],np.uint8)   
#redAlto01 = np.array([8,255,255],np.uint8)   
#Segundo Rango
#redBajo02 = np.array([175,100,20],np.uint8)   
#redAlto02 = np.array([179,255,255],np.uint8)   
azulBajo02 = np.array([100,100,20],np.uint8)   
azulAlto02 = np.array([125,255,255],np.uint8) 
while True:
  #Capturamos video frame a frame
  ret, frame = vc.read()
  if ret==True:
    #Convertimos a escala de grises
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frameHSV,azulBajo02,azulAlto02)
    #Deteccion de contornos
    contornos,_ = cv2.findContours(mask,cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    #Dibujar las contornos
    #cv2.drawContours (frame, contornos, -1, (255,0,0), 3)
    #Eliminado algunos contornos no deseados
    for i in contornos:
      area=cv2.contourArea(i)
      if area>3000:
        nuevoContorno=cv2.convexHull(i)
        cv2.drawContours(frame,[nuevoContorno],0,(125,0,0),3)
    #En la imagen frameHSV vamos a encontrar los rango bajo01 y alto 1 los mismo para 2
    #firstRed1=cv2.inRange(frameHSV,redBajo01,redAlto01)
    #secondRed2=cv2.inRange(frameHSV,redBajo02,redAlto02)
    #Adicionar las dos para convertirla en una solo y me detecte el rojo
    #unity=cv2.add(firstRed1,secondRed2)
    #En vez de blanco mostrar el color real 
    #unityOriginal=cv2.bitwise_and(frame,frame,mask=unity)
    #cv2.imshow("unityOriginal",unityOriginal)
    #Visualiazacion detección de los colores
    #cv2.imshow("Mascara",mask)
    #Mostramos el frame capturado
    cv2.imshow('Video', frame)

    #Si pulsamos q finalizamos'
    if  cv2.waitKey(1) & 0xFF==ord("q"):
      break;
#Finalizamos camara  y cerramos ventana
vc.release()
cv2.destroyAllWindows()

