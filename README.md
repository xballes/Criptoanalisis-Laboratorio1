# Criptoanálisis-Laboratorio
Este programa, calcula la frecuencia de las letras más repetidas en el texto introducido por el usuario y sustituye en el texto, su carácter más frecuente con el carácter más frecuente del Castellano y así sucesivamente.

Una vez hecho eso, puede que el texto no este descifrado completamente, así que, se muestra un menú con 2 opciones.

```python
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
```

La primera permite sustituir uno por uno los caracteres que se introduzcan en la terminal.(Esto sería más óptimo en caso de que haya que realizar pocos cambios.)

La segunda permite sustituir una lista de caracteres que se introduzcan en la terminal(Esto sería más óptimo si hay que realizar muchas sustituciones y se conoce la solución).
