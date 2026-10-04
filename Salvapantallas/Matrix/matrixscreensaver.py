import random, sys, time

ancho=100 #nro de columnas
try:
    #para cada columna cuando el contador es 0 no muestra nada
    #de lo contrario actua como un contadora de veces a mostrarse
    #un 1 o 0 en la columna
    columna=[0]*ancho
    while True:
        #bucle de columnas
        for i in range(ancho):
            if random.random() <0.02:
                #reinicia el contador para la columna
                #la longitud que vamos e elegir es entre 4 y 14
                columna[i]=random.randint(4,14)
            #imprime un caracter en la columna
            if columna[i]==0:
                # ' ' son espacios en blanco, '.' para verlos
                print(' ', end='')
            else:
                #imprime 1 o 0
                print(random.choice([0,1]),end='')
                columna[i] -= 1 #disminuye el contador
        print() #crea una linea nueva
        time.sleep(0.1) #espera una decima de segundo
except KeyboardInterrupt:
    sys.exit() #se finaliza con control + c