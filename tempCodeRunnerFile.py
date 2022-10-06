 def accion1():
            print('Introduce la letra del texto que deseas modificar:')
            letra=input()
            print('Introduce la letra con la que la quieras sustituir:')
            sustituta=input()
            #print(mensaje)
            modificacion=mensaje.replace(letra,sustituta)
            print(modificacion)
            
        def accion2():
            print('Introduce todas los caracteres ya ajustados:')
            frec=input()
            #print(mensaje)
            ajustado=texto.maketrans(Alfabeto,frec)
            ajustado=texto.translate(ajustado)
            print(ajustado)
            

        def salir():
            print('Has salido')
            
        opciones = {
        '1': ('Reemplazar caracteres', accion1),
        '2':('Reemplazar todos los caracteres',accion2),
        '3': ('Salir', salir)
        }
        
        def mostrar_menu(opciones):
            print('Seleccione una opción:')
        for clave in sorted(opciones):
            print(f' {clave}) {opciones[clave][0]}')
        
        def leer_opcion(opciones):
            while (a := input('Opción: ')) not in opciones:
             print('Opción incorrecta, vuelva a intentarlo.')
            return a
        def ejecutar_opcion(opcion, opciones):
            opciones[opcion][1]()
        
        def generar_menu(opciones, opcion_salida):
            opcion = None
            while opcion != opcion_salida:
                mostrar_menu(opciones)
                opcion = leer_opcion(opciones)
                ejecutar_opcion(opcion, opciones)
                print() # se imprime una línea en blanco para clarificar la salida por pantalla
                
        generar_menu(opciones, '2')