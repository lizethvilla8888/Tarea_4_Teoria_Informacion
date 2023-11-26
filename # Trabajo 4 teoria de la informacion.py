# Trabajo 4 teoria de la informacion 

# _  
# c = codigo {c0,c1,...,cn-1} 

# _  
# m = mensaje {m0,m1,...,mn-1}

# _  
# b = bits de pariedad {b0,b1,...,b n-k-1}
# _  
# b = n-k = bits de pariedad, 6-3= 3 bits de  pariedad 

# _   _   _
# b = m * P 

#B. Código <6,3>    <n,k>   , n>k 
# donde n = filas, columnas? ¿tamaño palabra?, k = bits de pariedad 

# 𝑏0 = 𝑚1 + 𝑚2
# 𝑏1 = 𝑚0 + 𝑚2
# 𝑏2 = 𝑚0 + 𝑚1
#                                  _
# De b0, 1, b2 obtenemos la matriz P 
# _ 
# P = matriz de coeficientes 
#       bo b1 b2 
# _   | 0  1   1 | mo
# P = | 1  0   1 | m1
#     | 1  1   0 | m2 

# Ik = matriz identidad 3*3 

#      | 1  0  0 | 
# Ik = | 0  1  0 | 
#      | 0  0  1 |   

# _    _   __
# E = [p : Ik ]    (:) concatenado 

# _   | 0 1 1 | 1 0 0 | 
# E = | 1 0 1 | 0 1 0 |
#     | 1 1 0 | 0 0 1 |

# con esto pomos decir que el 
#_   _   _  _
#c = m *[P:Ik]

# _   _   _ 
# c = m * E

# _                                             _ T
# H = Matriz verificadora de pariedad = [In-k : P ]  

# _   | 1 0 0 | 0 1 1 | 
# H = | 0 1 0 | 1 0 1 |
#     | 0 0 1 | 1 1 0 |

def leer_archivo():
    with open('ejemplo1.txt', 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
    return contenido

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
    
    return partes

def ejemplo_uso(caracter):
    # Convierte el mensaje a binario
    codigo_binario = mensaje_a_binario(caracter)
    
    print("Mensaje original:", caracter)
    print("Código binario:", codigo_binario)
    
    # Divide el código binario en tres partes
    partes_binarias = binario_a_tres_partes(codigo_binario)
    
    print("Partes binarias:", partes_binarias)
    return partes_binarias

texto = leer_archivo()
print (texto)







