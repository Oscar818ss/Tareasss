def ingresar_puntuacion():
    """Función para ingresar puntuaciones y comentarios."""
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        point = input()
        
        if point.isdecimal():
            point = int(point)
            if point <= 0 or point > 5:
                print('Indíquelo en una escala de 1 a 5')
            else:
                print('Por favor, introduzca un comentario')
                comment = input()
                post = f'punto: {point} comentario: {comment}'
                
                # Usar with para manejar el archivo automáticamente
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{post}\n')
                print('Puntuación y comentario guardados.')
                break
        else:
            print('Por favor, introduzca la puntuación en números')


def mostrar_resultados():
    """Función para mostrar los resultados almacenados."""
    print('Resultados hasta la fecha:')
    try:
        with open("data.txt", "r") as read_file:
            contenido = read_file.read()
            if contenido:
                print(contenido)
            else:
                print('No hay resultados almacenados.')
    except FileNotFoundError:
        print('No se encontraron resultados. Asegúrese de haber ingresado al menos una puntuación.')


def main():
    """Función principal que gestiona el flujo del programa."""
    while True:
        print('Seleccione el proceso que desea aplicar')
        print('1: Ingresar puntuación y comentario')
        print('2: Comprueba los resultados obtenidos hasta ahora.')
        print('3: Finalizar')
        num = input()
        
        if num.isdecimal():
            num = int(num)
            if num == 1:
                ingresar_puntuacion()
            elif num == 2:
                mostrar_resultados()
            elif num == 3:
                print('Finalizando')
                break
            else:
                print('Introduzca un número del 1 al 3')
        else:
            print('Introduzca un número del 1 al 3')


if __name__ == "__main__":
    main()
