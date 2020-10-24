import pygame, sys

#SETUP
pygame.init()
clock=pygame.time.Clock()

screen_width = 1080 #LE DAMOS DIMENSION A LA PANTALLA DEL JUEGO
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mi juego u.u")

#RECTANGLES
#POSICION DE ELEMENTOS
ball = pygame.Rect(screen_width/2 -11, screen_height/2 -11,22,22)
player = pygame.Rect(screen_width-20, screen_height/2-60, 120)
enemy = pygame.Rect(10, screen_height/2 -60,10,120)

#COLORES 
bgColor= (25,25,25) #RGB -> ROJO, AMARILLO, AZUL
objetColor = (115,115,155) 

#LOOP
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: #ESTA SIRVE PARA QUE
			pygame.quit()			  #CUANDO CIERRA Y PICA X
			sys.exit()				  #CIERRA LA PESTANA

	#METERLE LOS COLORES A LOS ELEMENTOS DEL JUEGO
	screen.fill (bgColor)
	pygame.draw.rect (screen, objetColor, player) #DIBUJA PLAYER
	pygame.draw.rect (screen, objetColor, enemy) #DIBUJAR ENEMIGO
	pygame.draw.ellipse (screen, objetColor, ball) #DIBUJAR PELOTA
		pygame.draw.aaline(screen, objetColor, (screen_width/2), (screen_width/2 screen_height/2))


	pygame.display.flip()
	clocl.tick(60) #60FPS
