import pytest
from analizador import automataNumeros, automataPalabra, automataLiteral, analisis

# Pruebas para números
def test_automataNumeros_entero():
    cadena = "1234 "
    resultado = automataNumeros(cadena, 0)
    assert resultado == 4  # El índice final debe ser 4

def test_automataNumeros_real():
    cadena = "12.34 "
    resultado = automataNumeros(cadena, 0)
    assert resultado == 5  # El índice final debe ser 5

def test_automataNumeros_error():
    cadena = "12a34 "
    resultado = automataNumeros(cadena, 0)
    assert resultado == -1  # Debería dar error por un caracter inapropiado en el número

# Pruebas para palabras e identificadores
def test_automataPalabra_identificador():
    cadena = "miVariable1 "
    resultado = automataPalabra(cadena, 0)
    assert resultado == (10, "miVariable1")  # Debe detectar el identificador correctamente

def test_automataPalabra_palabra_clave():
    cadena = "int "
    resultado = automataPalabra(cadena, 0)
    assert resultado == (2, "int")  # Debe identificar correctamente la palabra clave "int"

# Pruebas para literales


def test_automataLiteral_comillas_dobles():
    cadena = "'literal'"
    resultado = automataLiteral(cadena, 0)
    assert resultado == 8  # Longitud total de la literal

# Pruebas para operadores y puntuadores
def test_analisis_operadores():
    cadena = "++ -- == != <= >= "
    resultado = analisis(cadena)
    assert resultado == 0  # Debe procesar los operadores sin errores

def test_analisis_puntuadores():
    cadena = "; , . # "
    resultado = analisis(cadena)
    assert resultado == 0  # Debe procesar los puntuadores sin errores

# Pruebas para comentarios
def test_analisis_comentarios():
    cadena = "// Este es un comentario\n"
    resultado = analisis(cadena)
    assert resultado == 0  # Debe procesar el comentario correctamente y no generar error

def test_analisis_cadena_compleja():
    cadena = "int a = 10; float b = 12.34; // Declaraciones de variables"
    resultado = analisis(cadena)
    assert resultado == 0  # Debe procesar correctamente toda la cadena sin errores

def test_analisis_error_lexico():
    cadena = "int a = 12..34;"
    resultado = analisis(cadena)
    assert resultado == -1  # Debería devolver error por el número mal formado

def test_analisis_arreglo_unidimensional():
    cadena = "int arr[10];"
    resultado = analisis(cadena)
    assert resultado == 0  # Debe procesar correctamente el arreglo unidimensional

def test_analisis_matriz_bidimensional():
    cadena = "float matrix[5][10];"
    resultado = analisis(cadena)
    assert resultado == 0  # Debe procesar correctamente la matriz bidimensional

def test_analisis_arreglo_con_inicializacion():
    cadena = "int arr[3] = {1, 2, 3};"
    resultado = analisis(cadena)
    assert resultado == 0  # Debe procesar correctamente el arreglo con inicialización

def test_analisis_arreglo_de_variables():
    cadena = "int arr[5] = {a, b, c, d, e};"
    resultado = analisis(cadena)
    assert resultado == 0  # Debe procesar correctamente el arreglo con variables

def test_analisis_matriz_con_operaciones():
    cadena = "matrix[2][3] = a + b * 5;"
    resultado = analisis(cadena)
    assert resultado == 0  # Debe procesar correctamente una matriz con operaciones

def test_analisis_acceso_a_arreglo():
    cadena = "arr[2] = 10;"
    resultado = analisis(cadena)
    assert resultado == 0  # Debe procesar correctamente el acceso y asignación en un arreglo

def test_analisis_acceso_a_matriz():
    cadena = "matrix[3][4] = 12.5;"
    resultado = analisis(cadena)
    assert resultado == 0  # Debe procesar correctamente el acceso y asignación en una matriz

def test_analisis_arreglo_error_sintaxis():
    cadena = "int arr[3] = {1, 2,};"
    resultado = analisis(cadena)
    assert resultado == -1  # Debe detectar error en la sintaxis del arreglo
def test_analisis_error_matriz_faltante_corchete():
    cadena = "int arr[5;"
    resultado = analisis(cadena)
    assert resultado == -1  # Debería dar error por corchete faltante

def test_analisis_error_acceso_matriz():
    cadena = "matrix[3] = 10;"
    resultado = analisis(cadena)
    assert resultado == -1  # Debe dar error por número incorrecto de índices en la matriz
