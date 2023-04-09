import pyautogui as pg
import time

numero=int(input("Introduce el número de mensajes a enviar:"))
mensaje=str(input("Introduce el mensaje a enviar:"))

time.sleep(5)

for i in range (numero):
    pg.write(mensaje)
    pg.press('Enter')
   

