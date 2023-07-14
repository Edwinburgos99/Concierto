# Librerias
import matplotlib.pyplot as plt
import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as tkfont
import subprocess

# Creamos la ventana principal del programa 
window = tk.Tk()
window.title("Minizinc")
window.geometry("800x600")

# Cargar y redimensionar la imagen de fondo
background_image = Image.open("C:\\Users\\Edwin\\Desktop\\Concert.png")
background_image = background_image.resize((800, 600))  # Ajusta el tamaño según tus necesidades

# Crear un objeto PhotoImage a partir de la imagen
photo = ImageTk.PhotoImage(background_image)

# Crear un widget Label para mostrar la imagen de fondo
background_label = tk.Label(window, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Creacion de un widget en la ventana
title_label = tk.Label(window, text="¿Donde pongo mi concierto?", font=('Arabic Transparent', 24), fg="white", bg="#000000")
title_label.place(x=200, y=10)

# Creacion de los titulos que apareceran encima del campo de texto
title_label = tk.Label(window, text="DATOS DE ENTRADA", font=("Arabic Transparent", 14), fg="white", bg="#000000")
title_label.place(x=72, y=65)
title_label = tk.Label(window, text="DATOS DE SALIDA", font=("Arabic Transparent", 14), fg="white", bg="#000000")
title_label.place(x=495, y=65)

# Creamos los campos de texto
text_area = tk.Text(window, height=26, width=35)
text_area.place(x=30, y=100)
text_area_resultados = tk.Text(window, height=26, width=45)
text_area_resultados.place(x=400, y=100)

# Obtener lista de familias de fuentes disponibles en Tkinter
font_families = tkfont.families()

# Función para calcular la distancia Manhattan entre dos ciudades
def distancia_manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

# Funcion para obtener los datos de entrada ingresados en el campo de texto
def obtener_datos_entrada():
    datos_entrada = []
    texto_entrada = text_area.get("1.0", tk.END) # se obtiene el texto ingresado en el campo de texto de entrada.
    lineas = texto_entrada.strip().split("\n")  # Dividir el texto en líneas y eliminar espacios en blanco

    try:
        N = int(lineas[0])  # Obtener el valor de tamaño del cuadro
        num_ciudades = int(lineas[1])  # Obtener el número de ciudades

        for linea in lineas[2:]:
            datos = linea.split()  # Dividir la línea en palabras
            ciudad = datos[0]
            x = int(datos[1])
            y = int(datos[2])
            datos_entrada.append({"Ciudad": ciudad, "X": x, "Y": y}) # agrega un nuevo elemento a la lista datos_entrada, Cada elemento de
            # la lista es un diccionario que almacena la información de una ciudad específica.

        return datos_entrada, N, num_ciudades
    
    except ValueError:
        # Mostrar mensaje de advertencia
        text_area_resultados.delete("1.0", tk.END)  # Borrar el contenido anterior
        text_area_resultados.insert(tk.END, "¡Error! Los valores de N y num_ciudades deben ser números enteros.")

        return None, None, None

def calcular_ubicacion_optima(datos_entrada, N, num_ciudades):
    ciudades = [] # se almacena los datos de cada ciudad
    for i in range(num_ciudades):
        ciudad = datos_entrada[i]["Ciudad"]
        x = datos_entrada[i]["X"]
        y = datos_entrada[i]["Y"]
        ciudades.append({'Ciudad': ciudad, 'X': x, 'Y': y})

    ubicaciones = [(x, y) for x in range(N) for y in range(N)]
    minima_distancia_total = float("inf")
    ubicacion_optima = None

    for ubicacion in ubicaciones:
        distancia_total = sum(distancia_manhattan(ubicacion[0], ubicacion[1], ciudad['X'], ciudad['Y']) for ciudad in ciudades)# Calcula la distancia_total sumando
        # las distancias de Manhattan entre la ubicación actual y cada una de las ciudades
        
        if ubicacion_no_ciudad(ubicacion, ciudades) and distancia_equitativa(distancia_total, ubicacion, ciudades): # función que verifica si la ubicación actual
            # no coincide con ninguna de las coordenadas de las ciudades, función que verifica si la distancia total calculada es equitativa
            # en comparación con las distancias de todas las ciudades
            if distancia_total < minima_distancia_total:
                minima_distancia_total = distancia_total
                ubicacion_optima = ubicacion

    return ubicacion_optima


# verifica si una determinada ubicación no coincide con ninguna de las ciudades en la lista ciudades.
# Recorre cada ciudad y compara las coordenadas X y Y de la ubicación con las coordenadas de la ciudad.
# Si encuentra una coincidencia, devuelve False, lo que significa que la ubicación es una ciudad existente.
# Si no encuentra ninguna coincidencia, devuelve True, lo que indica que la ubicación no es una ciudad existente.
def ubicacion_no_ciudad(ubicacion, ciudades):
    for ciudad in ciudades:
        if ubicacion[0] == ciudad['X'] and ubicacion[1] == ciudad['Y']:
            return False
    return True

# verifica si las distancias de cada ciudad a la ubicación óptima son equitativas,
# es decir, si la diferencia entre cada distancia y el promedio de las distancias es menor o igual a 1.
def distancia_equitativa(distancia_total, ubicacion_optima, ciudades):
    promedio_distancia = distancia_total / len(ciudades)
    for ciudad in ciudades:
        distancia_ciudad = distancia_manhattan(ciudad['X'], ciudad['Y'], ubicacion_optima[0], ubicacion_optima[1])
    if abs(distancia_ciudad - promedio_distancia) > 1:
        return False
    return True

def calcular_solucion():
    # Obtener datos de entrada
    datos_entrada, N, num_ciudades = obtener_datos_entrada()

    # Calcular ubicación óptima
    ubicacion_optima = calcular_ubicacion_optima(datos_entrada, N, num_ciudades)

    modelo_minizinc = mostrar_resultados(datos_entrada, ubicacion_optima, N, num_ciudades)

    # Mostrar la ubicación óptima en el campo de texto de resultados
    text_area_resultados.delete("1.0", tk.END)  # Borrar el contenido anterior
    text_area_resultados.insert(tk.END, f"Ubicación óptima: {ubicacion_optima}")

    # Mostrar el código MiniZinc en el campo de texto de resultados
    text_area_resultados.insert(tk.END, "\nCódigo MiniZinc:\n")
    text_area_resultados.insert(tk.END, modelo_minizinc)

def graficar_coordenadas(ciudades, ubicacion_optima, N):
    # Crear listas separadas para las coordenadas X e Y
    x_coords = [ciudad['X'] for ciudad in ciudades]
    y_coords = [ciudad['Y'] for ciudad in ciudades]

    # Crear figura y ejes
    fig, ax = plt.subplots(figsize=(N, N))

    # Configurar el fondo del gráfico
    fig.set_facecolor('black')
    ax.set_facecolor('black')

    # Configurar cuadrícula
    ax.grid(True, color='white')

    # Graficar las coordenadas de las ciudades
    ax.scatter(x_coords, y_coords, color='blue', label='Ciudades')

    # Graficar la ubicación óptima
    ax.scatter(ubicacion_optima[0], ubicacion_optima[1], color='white', label='Ubicación óptima')

    # Establecer límites del gráfico
    ax.set_xlim(0, N)
    ax.set_ylim(0, N)

    # Configurar el color de los límites del gráfico
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['right'].set_color('white')

    # Agregar etiquetas a las ciudades
    for i, ciudad in enumerate(ciudades):
        ax.annotate(ciudad['Ciudad'], (ciudad['X'], ciudad['Y']), textcoords="offset points", xytext=(0,10), ha='center', fontsize=12, fontname='Times New Roman', color='white')

    # Configurar color de los números de las coordenadas
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    
    # Configurar etiquetas de los ejes
    ax.set_xlabel('Coordenada X', color='white')
    ax.set_ylabel('Coordenada Y', color='white')

    # Agregar titulo del grafico
    ax.legend()
    ax.set_title('Ubicación del concierto', color='white')

    # Mostrar el gráfico
    plt.show()

def generar_modelo_minizinc(coord_x, coord_y, N, num_ciudades): # genera un modelo en el lenguaje MiniZinc para resolver un problema de optimización

    variables = "var int: x;\nvar int: y;\n"
    restricciones = "constraint x >= 0;\nconstraint y >= 0;\n"
    tamanio = f"constraint x <= {N};\nconstraint y <= {N};\n"
    index_set = f"set of int: CIUDADES = 1..{num_ciudades};\n"
    funcion = f"function var int: distancia_manhattan(var int: x1,var int: y1,var int: x2,var int: y2) = abs(x1 - x2) + abs(y1 - y2);\n"
    solve = ""
    show= 'output["x=",show(x),"y=",show(y)];'

    for i in range(num_ciudades):
        solve += f"var int: distancia{i+1} = distancia_manhattan({coord_x[i]}, {coord_y[i]}, x, y);\n"
    
    solve += "solve minimize distancia1;\n"
    

    modelo_minizinc = variables + restricciones + tamanio + index_set + funcion + solve + show

    return modelo_minizinc


def mostrar_resultados(datos_entrada, ubicacion_optima, N, num_ciudades):
    # Obtener datos de entrada
    ciudades = datos_entrada[:]
    
    # Mostrar ubicación óptima en el campo de texto de resultados
    text_area_resultados.delete("1.0", tk.END)  # Borrar el contenido anterior
    text_area_resultados.insert(tk.END, f"Ubicación óptima: {ubicacion_optima}\n")

    # Mostrar gráfico de coordenadas
    graficar_coordenadas(datos_entrada, ubicacion_optima, N)

    # Generar código MiniZinc
    coord_x = [ciudad['X'] for ciudad in ciudades] # coordenadas de x de cada ciudad 
    coord_y = [ciudad['Y'] for ciudad in ciudades] # coordenadas de y de cada ciudad 
    modelo_minizinc = generar_modelo_minizinc(coord_x, coord_y, N, num_ciudades)

    # Mostrar el código MiniZinc en el campo de texto de resultados
    text_area_resultados.insert(tk.END, "\nCódigo MiniZinc:\n")
    text_area_resultados.insert(tk.END, modelo_minizinc)

    return modelo_minizinc

def enviar_a_minizinc():
    datos_salida = text_area_resultados.get("1.0", tk.END)  # Obtener el texto del campo de salida

    # Guardar los datos en un archivo temporal
    with open("datos_salida.mzn", "w") as file:
        file.write(datos_salida)
    
    # Ruta al archivo MiniZinc
    ruta_minizinc = "C:\\Users\\Edwin\\AppData\\Local\\Programs\\MiniZinc\\MiniZincIDE.exe"  # Reemplaza con la ruta correcta al acceso directo de MiniZinc en tu escritorio
    
    # Abrir el programa MiniZinc y pasarle el archivo de datos como argumento
    subprocess.Popen([ruta_minizinc, "datos_salida.mzn"])

def cerrar_programa():
    window.destroy()

Solucion = tk.Button(window, text="SOLUCIÓN", width=20, height=2, font=("Arabic Transparent", 12), fg="white", bg="#070B0A", bd=2, relief="solid", command=calcular_solucion,)
Solucion.place(x=77, y=530)

Salir = tk.Button(window, text="X", width=3, height=1, font=("Arabic Transparent", 12), fg="black", bg="#f0ffff", bd=2, relief="solid", command=cerrar_programa,)
Salir.place(x=762, y=565)

minizinc_button = tk.Button(window, text="MiniZinc", width=20, height=2, font=("Arabic Transparent", 12), fg="white", bg="#070B0A", bd=2, relief="solid", command=enviar_a_minizinc)
minizinc_button.place(x=495, y=530)

# Mostramos la ventana en ejecución
window.mainloop()
