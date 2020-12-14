import  pygame
import os
pygame.init()
ancho,largo = 800 , 500 
ventana = pygame.display.set_mode((ancho,largo))
pygame.display.set_caption("HangProf :/")

#Cargamos las imagenes

imagenes = []
for i in range(6):
    imagen = pygame.image.load("hangman" + str(i) + ".png")
    imagenes.append(imagen)
print (imagenes)

#Variables
estado = 0


#Configurar bucle del juego :|
fps = 60
reloj = pygame.time.Clock()
encendido = True
while encendido:
    reloj.tick(fps)

    win.fill(())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            encendido = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos) 
pygame.quit()
