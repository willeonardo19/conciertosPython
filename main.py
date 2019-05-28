# -*- coding: utf-8 -*-
## import para limpiar pantalla
from os import system, name
# import para manejar fechas
from datetime import date, timedelta
# import para el ordenamiento de conciertos
from operator import itemgetter

anio = 2019
conciertos = [
    {
        'artista'   : 'ACDC',
        'hora'      : '18:00',
        'fecha'     : '2019-06-01', # ano mes dia
        'precio'    : '150'
    },
    {
        'artista'   : 'MELENDI',
        'hora'      : '18:00',
        'fecha'     : '2019-06-30', # ano mes dia
        'precio'    : '150'
    },
    {
        'artista'   : 'JUANES',
        'hora'      : '18:00',
        'fecha'     : '2019-07-31', # ano mes dia
        'precio'    : '150'
    }
]


# funcion para limpiar pantalla
def clear():
    # para windows
    if name == 'nt':
        _ = system('cls')

        # para mac y linux(here, os.name is 'posix')
    else:
        _ = system('clear')


# validar la que la fecha
# sea de junio a septiembre
def validar_fecha(d, m):
    message = False
    try:
        dia = int(d)
        mes = int(m)
        if dia > 0 and dia <= 30 and mes == 6 or dia > 0 and dia <= 30 and mes == 9:
            message = True
        elif dia > 0 and dia <= 31 and mes == 7 or dia > 0 and dia <= 31 and mes == 8:
            message = True
        return message
    except:
        return message


# validar si la fecha esta ocupada por algun concierto
def validar_disponibilidad(d, m):
    message = False
    try:
        fecha = date(int(anio), int(m), int(d)) #convertimos en fecha
        if(len(conciertos) == 0):
            message = True
        else:
            for concierto in conciertos:
                if str(concierto['fecha']) == str(fecha):
                    message = False
                    break #comentar para ver el error logico
                else:
                    message = True
        return message
    except:
        return message


# obtener el dato para añadirlo al diccionario
def _obtener_datos(item):
    campo = None
    while not campo:
        campo = input("Ingresa {}:.".format(item))
    return campo


# crear un nuevo concierto
def nuevo_concierto(d, m):
    print('Datos del nuevo concierto'.center(50, '-'))
    concierto = {
        'artista':  _obtener_datos('Artista/Grupo').upper(),
        'hora':     _obtener_datos('Hora'),
        'fecha':    str(date(int(anio), int(m), int(d))),
        'precio':   _obtener_datos('Precio')
    }
    conciertos.append(concierto)
    print("Concierto añadido correctamente.")


#listar los conciertos
def _conciertos(lista_conciertos):
    if len(lista_conciertos) > 0:
        conciertos_ordenados = sorted(lista_conciertos, key=itemgetter('fecha'))
        print('No.  | Artista/Grupo | Hora  | Fecha | Precio')
        for idx, concierto in enumerate(conciertos_ordenados):
            print('{cid}    | {artista}    | {hora}    | {fecha}    | {precio}'.format(
                cid=idx,
                artista=concierto['artista'],
                hora=concierto['hora'],
                fecha=concierto['fecha'],
                precio=concierto['precio']
            ))
    else:
        print("No hay conciertos.")


# buscar conciertos de un mes
def _listar_conciertos(m):
    try:
        mes = int(m)
        conciertos_mes = []
        if mes >= 6 and mes <= 9:
            if len(conciertos) > 0:
                for concierto in conciertos:
                    data = str(concierto['fecha']).split('-')
                    month = date(int(data[0]), int(data[1]), int(data[2])).month
                    if  mes == month:
                        conciertos_mes.append(concierto)
                _conciertos(conciertos_mes)
            else:
                print("No existen conciertos para este mes.")

        else:
            print("Mes incorrecto")
    except:
        print("Mes incorrecto..")


# buscar conciertos por artista
def _conciertos_artista(artista):
    conciertos_artista = []
    if len(conciertos) > 0:
        for concierto in conciertos:
            if artista.upper() == concierto['artista']:
                conciertos_artista.append(concierto)
        _conciertos(conciertos_artista)
    else:
        print("No existen conciertos para este artista.")


# eliminar concierto
def eliminar_concierto(d,m):
    message = None
    try:
        fecha = date(int(anio), int(m), int(d))  # convertimos en fecha
        for concierto in conciertos:
            if str(concierto['fecha']) == str(fecha):
                index = conciertos.index(concierto)
                conciertos.pop(index)
                print('Concierto eliminado')
                break  # comentar para ver el error logico

    except:
        return print('Nada para eliminar')


# funcion para el menu del programa
def menu():
    clear()
    # op = None
    print('Conciertos'.center(50, '*'))
    op = input("""
    A. Introducir Concierto.
    B. Buscar Concierto por Nombre de Grupo/Solista.
    C. Listar Conciertos de un Mes.
    D. Borrar Concierto.
    E. Estudio de Mercado.
    X. Salir del Programa.
    ::""")
    return op


# funcion para el estudio del mercado
def _obtener_fecha():
    if len(conciertos) > 0:
        mayor = 0
        fecha = None
        if len(conciertos) > 1:
            for i in range(len(conciertos)):

                if i == (len(conciertos) - 1):
                    break
                fecha_i = conciertos[i]['fecha'].split('-')
                fecha_f = conciertos[i + 1]['fecha'].split('-')
                inicio = date(int(fecha_i[0]), int(fecha_i[1]), int(fecha_i[2]))
                fin = date(int(fecha_f[0]), int(fecha_f[1]), int(fecha_f[2]))
                diferencia = (fin - inicio).days
                if diferencia > mayor:
                    mayor = (fin - inicio).days
                    data_i = inicio
                    dias = mayor
                    medio = dias // 2
                    fecha = data_i + timedelta(days = medio)
        return fecha


if __name__ == '__main__':
    option = menu()
    while True:
        conciertos = sorted(conciertos, key=itemgetter('fecha'))
        if option.upper() == 'A':
            print('Nuevo Concierto'.center(50, '-'))
            dia = input('Ingresa día:.')
            mes = input('Ingresa mes:.')
            if validar_fecha(dia, mes):
                if validar_disponibilidad(dia, mes):
                    nuevo_concierto(dia, mes)
                else:
                    print('Ya existe un concierto en esa fecha')
            else:
                print('fecha no disponible')

        elif option.upper() == 'B':
            print('Buscar Concierto'.center(50, '-'))
            artista = input('Ingresa el nombre del Artista/Grupo:.')
            _conciertos_artista(artista)

        elif option.upper() == "C":
            print('Listar Concierto por Mes'.center(50, '-'))
            mes = input('Ingresa mes:.')
            _listar_conciertos(mes)

        elif option.upper() == "D":
            print('Borrar Concierto'.center(50, '-'))
            dia = input('Ingresa día:.')
            mes = input('Ingresa mes:.')
            if validar_fecha(dia, mes):
                if not validar_disponibilidad(dia, mes):
                    eliminar_concierto(dia, mes)
                else:
                    print('No existe un concierto en esa fecha')
            else:
                print('fecha no disponible')

        elif option.upper() == "E":
            fecha = None
            print('Estudio de Mercado'.center(50, '-'))
            fecha = _obtener_fecha()
            if fecha != None:
                print('Fecha:. {} - {}'.format(fecha.day, fecha.month))
                print('Nuevo Concierto'.center(50, '-'))
                if validar_fecha(str(fecha.day), str(fecha.month)):
                    if validar_disponibilidad(str(fecha.day), str(fecha.month)):
                        nuevo_concierto(str(fecha.day), str(fecha.month))
                    else:
                        print('Ya existe un concierto en esa fecha')
                else:
                    print('fecha no disponible')
            else:
                print("No puede utilizar esta funcion por el momento, ingrese otro concierto")

        elif option.upper() == "X":
            print('Salir'.center(50, '-'))
            salir = input('Pulse 0 para salir')
            if salir == '0':
                input('Adios, pulse enter para continuar')
                break

        else:
            print('Opcion no valida.')

        input('Pulse enter para continuar.')
        option = menu()




