import datetime
from datetime import date
def crear_escenario(escenario): # Creación de la matriz que contiene los asientos del 1 al 50 (escenario)
    
    for contador_externo in range(1,51,10):
        lista_asientos = []
        for contador_interno in range(10):
            lista_asientos.append(contador_externo+contador_interno) # Valores se guardan como Int
        escenario.append(lista_asientos)

def matriz_compradores(compradores): # Creación de la matriz de compradores
    
    for contador_externo in range(1,51,10):
        lista_rut = []
        for contador_interno in range(10):
            lista_rut.append(0) # Se incializa la matriz con Ceros tipo de dato Int
        compradores.append(lista_rut)

def mostrar_escenario(escenario):
    print("\t\t\t\t\t\t Escenario\n") # Tabulación para que palabra "Escenario" se muestre en la mitad frente a primera fila
    for fila in range(5):
        imprimir = " " # String vacío que permite ir almacenando valores para poder formatearlo y que salgan ordenados
        for columna in range (10):
            imprimir = imprimir +"\t " + str(escenario[fila][columna])
        print("\t",imprimir,"\t")

def comprar_entrada(escenario, compradores, asiento, rut):
    
    for fila in range(5):
        for columna in range(10):
            if(escenario[fila][columna] == asiento and escenario[fila][columna] != "X"):
                escenario[fila][columna] = "X"
                compradores[fila][columna] = rut

def listar_compradores(compradores):
    
    print("Rut")
    for fila in range(5):
        compradores[fila].reverse()
        for columna in range (10):
            if(compradores[fila][columna] != 0): # Validación para evitar imprimir valores de la matriz que no contengan un Rut ingresado por el usuario
                print(f"Rut:{compradores[fila][columna]}")

def validacion_asiento(escenario, asiento_seleccionado):
    asiento_ocupado = False
    for fila in range(5):
        for columna in range(10):
            asiento_string = f"{fila}{columna}" # Obtengo la posición del asiento usando fila como decena y columna como unidad.
            asiento = int(asiento_string)+1 # Como valores parten de 0, se suma 1 para cuadrar valor y se convierte a int para  poder sumarle 1.
            if(asiento_seleccionado == asiento and escenario[fila][columna] == "X"):
                asiento_ocupado = True
    return asiento_ocupado

# Definición Diccionario de Precios
precios = {1: 100000, 2: 100000, 3: 100000, 4: 100000, 5: 100000,
            6: 100000, 7: 100000, 8: 100000, 9: 100000, 10: 100000,
            11: 100000, 12: 100000, 13: 100000, 14: 100000, 15: 100000,
            16: 100000, 17: 100000, 18: 100000, 19: 100000, 20: 100000,
            21: 50000, 22: 50000, 23: 50000, 24: 50000, 25: 50000,
            26: 50000, 27: 50000, 28: 50000, 29: 50000, 30: 50000,
            31: 10000, 32: 10000, 33: 10000, 34: 10000, 35: 10000,
            36: 10000, 37: 10000, 38: 10000, 39: 10000, 40: 10000,
            41: 10000, 42: 10000, 43: 10000, 44: 10000, 45: 10000,
            46: 10000, 47: 10000, 48: 10000, 49: 10000, 50: 10000}
# Inicialización de listas vacías para poder generar las respectivas matrices
escenario = [] 
compradores = []
crear_escenario(escenario)
matriz_compradores(compradores)
ganancias_totales = 0 # Variable Global que permitirá acumular valores

try:
    while(True):
        print("\nBienvenido al Sistema de Compra del Concierto de Michael Jackson\n")
        opcion_menu = int(input("Por Favor Seleccione una opción:\n1) Comprar Entrada.\n2) Mostrar Ubicaciones Disponibles.\n3) Ver Listado de Asistentes.\n4) Mostar Ganancias Totales.\n5) Salir.\n"))
        if(opcion_menu==1):
            cantidad_entradas = int(input("¿Cuántas entradas desea adquirir?:"))
            while (cantidad_entradas<1 or cantidad_entradas>2): # Validación para que solo se pueda adquirir 1 o 2 entradas
                cantidad_entradas = int(input("¿Cuántas entradas desea adquirir? Solo puede adquirir 1 o 2 entradas:"))
            for contador in range(cantidad_entradas): # Ciclo for para iterar proceso según cantidad de entradas seleccionadas.
                mostrar_escenario(escenario)
                rut = int(input("Por favor ingrese el Rut de la persona que usará el asiento:"))
                while(rut<1): # Validación de RUT ingresado por usuario sea >=1
                    rut = int(input("Por favor ingrese el Rut de la persona que usará el asiento, debe ser >= 1:"))
                asiento_seleccionado = int(input("Por favor seleccione un asiento:"))
                while(asiento_seleccionado<1 or asiento_seleccionado>50): # Validación que el asiento seleccionado esté dentro del rango de asientos del escenario
                    asiento_seleccionado = int(input("Por favor seleccione un asiento entre el rango 1-50:"))
                asiento_disponible = validacion_asiento(escenario, asiento_seleccionado)
                if(asiento_disponible == False):
                    comprar_entrada(escenario, compradores, asiento_seleccionado, rut)
                    nombre = input(f"Por Favor ingrese el nombre de la persona que usará el asiento {asiento_seleccionado}:")
                    precio = precios[asiento_seleccionado]
                    ganancias_totales = ganancias_totales + precio
                    print(f" Usted compró la entrada a nombre de {nombre} Rut {rut} en el asiento {asiento_seleccionado} por un valor de ${precio}")
                    print(f"¡Entrada comprada exitosamente!")
                else:
                    print(f"¡El asiento {asiento_seleccionado} no está disponible!")
            mostrar_escenario(escenario)
        if(opcion_menu==2):
            mostrar_escenario(escenario)
        if(opcion_menu==3):
            listar_compradores(compradores)
        if(opcion_menu==4):
            print(f"Las ganancias total del concierto ascienden a ${ganancias_totales}")
        if(opcion_menu)==5:
            print(f"Usted eligió la opción salir, adiós")
            print(f"Cristian Valenzuela")
            break
except ValueError:
    print("El tipo de datos ingresado, no es válido.")