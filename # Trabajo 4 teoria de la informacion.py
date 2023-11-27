import os
import numpy as np
import random

def leer_contenido_archivo(nombre_archivo):
    try:
        # Abre el archivo en modo lectura
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            # Lee el contenido del archivo
            contenido = archivo.read()
        return contenido
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None
    
def obtener_ruta_absoluta(nombre_archivo):
    # Obtiene la ruta absoluta del archivo
    ruta_absoluta = os.path.abspath(nombre_archivo)
    return ruta_absoluta


#pasa los caracteres a codigo ascii, y este numero lo representa en binario 
def mensaje_a_binario(caracter):
    # Convierte el mensaje a su representación ASCII
    ascii_codes = [ord(char) for char in caracter]
    
    # Convierte cada código ASCII a binario y completa con ceros a la izquierda
    binarios = [format(code, '08b') for code in ascii_codes]
    
    # Concatena los códigos binarios y toma los primeros 8 dígitos
    binario_resultante = ''.join(binarios)[:8]
    
    # Agrega un "0" al inicio
    binario_resultante = '0' + binario_resultante
    
    return binario_resultante

def binario_a_tres_partes(codigo_binario):
    # Divide el código binario en tres partes de 3 dígitos cada una
    partes = [codigo_binario[i:i+3] for i in range(0, len(codigo_binario), 3)]
    
    # Retorna una lista de listas
    return [list(parte) for parte in partes]

def xor_tres_entradas(a, b, c):
    return int(a) ^ int(b) ^ int(c)

def mult(x, y):
    if x == '1' and y == 1:
        return 1 
    else:
        return 0

def Codigo (m):
    codigo = [0,0,0,0,0,0]
    codigo[0] = xor_tres_entradas(mult(m[0], G[0, 0]), mult(m[1], G[1, 0]), mult(m[2], G[2, 0]))
    codigo[1] = xor_tres_entradas(mult(m[0], G[0, 1]), mult(m[1], G[1, 1]), mult(m[2], G[2, 1]))
    codigo[2] = xor_tres_entradas(mult(m[0], G[0, 2]), mult(m[1], G[1, 2]), mult(m[2], G[2, 2]))
    codigo[3] = xor_tres_entradas(mult(m[0], G[0, 3]), mult(m[1], G[1, 3]), mult(m[2], G[2, 3]))
    codigo[4] = xor_tres_entradas(mult(m[0], G[0, 4]), mult(m[1], G[1, 4]), mult(m[2], G[2, 4]))
    codigo[5] = xor_tres_entradas(mult(m[0], G[0, 5]), mult(m[1], G[1, 5]), mult(m[2], G[2, 5]))
    #print (codigo)
    return codigo 
#Punto 1 
#_________________________________________________________________________________________________________________________________________________

def generar_secuencia_errores(longitud, probabilidad_error):
    secuencia_errores = [1 if random.random() > probabilidad_error else 0 for _ in range(longitud)]
    return secuencia_errores

#Punto 2
#_________________________________________________________________________________________________________________________________________
G= np.array([[0, 1, 1, 1, 0, 0],
             [1, 0, 1, 0, 1, 0],
             [1, 1, 0, 0, 0, 1]])


codigo_texto = []

# Abrir archivo 
nombre_archivo = 'ejemplo1.txt'
ruta_absoluta = obtener_ruta_absoluta(nombre_archivo)
contenido_archivo = leer_contenido_archivo(ruta_absoluta)

contenido_archivo = "Hola"

print (len (contenido_archivo)) #45.394* 18 digitos de codigo = 817.092 

for i, caracter in enumerate(contenido_archivo):
    binario = mensaje_a_binario(caracter)
    #print(f"i = {i}, caracter = {caracter}, binario = {binario}")
    m = binario_a_tres_partes(binario)
    #print ("Binario: ",binario)
    for i in range (3):
        codigo_c = Codigo(m[i])
        #print ('m',i,':',m[i])
        codigo_texto = codigo_texto + codigo_c
    
print ("codigo sin errores : ", codigo_texto,"\n")
#Punto 1 
#_____________________________________________________________________________________________________________________________________________

probabilidad_error = 0.01  
secuencia_errores = generar_secuencia_errores(len(codigo_texto), probabilidad_error)


secuencia_con_errores = [a ^ b for a, b in zip(codigo_texto, secuencia_errores)]

# Imprime resultados (ajusta según tus necesidades)
print("Secuencia de errores:", secuencia_errores,"\n")
print("Secuencia con errores:", secuencia_con_errores,"\n")

#________________________________________________________________________________________________________________________________________
# Matriz de verificación de paridad (H)

H = np.array([[1, 0, 0, 0, 1, 1],
              [0, 1, 0, 1, 0, 1],
              [0, 0, 1, 1, 1, 0]])


print ("punto 3")