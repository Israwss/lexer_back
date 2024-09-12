# Importaciones necesarias
import sys

# Tabla de transiciones para reales y enteros
estadosRealEN = [[1, 4, 7, 7], [1, 4, 2, 7], [3, 7, 7, 7], [3, 4, 7, 7]] 

# Tabla de transiciones para formar palabras
Estadospalabra = [[1, 2, 2], [1, 1, 2]]

# Tabla de transiciones para formar literales
EstadosLiteral = [[1, 3, 3], [2, 1, 3]]

# Operandos y puntuadores
operandos = ["+", "-", "*", "/", "^", "%", "<", ">", "!", "&", "|", "="]
operandosDobles = ["<=", ">=", "==", "!=", "&&", "||", "++", "--", "//", "+="]
puntuadores = [";", ".", "#", ",", "(", ")", "[", "]", "{", "}"]
palabrasClave = ["auto", "else", "long", "switch", "break", "enum", "registrer", 
                 "typedef", "case", "extern", "return", "union", "char", "float", 
                 "short", "unsigned", "const", "for", "signed", "void", 
                 "continue", "goto", "sizeof", "volatile", "default", "if", 
                 "static", "while", "do", "int", "struct", "double", "_Packed"]

# Funciones del analizador
def automataNumeros(x, i):
    estado, soy, numero = 0, 0, ""
    resultados = []
    while estado != 4 and i < len(x) - 1:
        if x[i].isdigit():
            numero += x[i]
            estado = estadosRealEN[estado][0]
            soy = estado
        elif x[i] == ".":
            numero += x[i]
            estado = estadosRealEN[estado][2]
        elif x[i] in operandos or x[i] in puntuadores or x[i] == " ":
            soy = estado
            i -= 1
            estado = estadosRealEN[estado][1]
        else:
            numero += x[i]
            estado = estadosRealEN[estado][3]
        if estado == 7:
            resultados.append(f"Error, se encontro algo inapropiado en el numero: {numero}, en el caracter {i-1}")
            return -1, resultados
        i += 1
    if soy == 1:
        resultados.append(f"Es un numero entero: {numero}")
    elif soy == 3:
        resultados.append(f"Es un numero real: {numero}")
    return i, resultados

def automataPalabra(x, i):
    estado, pala = 0, ""
    resultados = []
    while estado != 2 and i < len(x) - 1:
        if x[i].isalpha():
            pala += x[i]
            estado = Estadospalabra[estado][0]
        elif x[i].isdigit():
            pala += x[i]
            estado = Estadospalabra[estado][1]
        else:
            estado = Estadospalabra[estado][2]
        i += 1
    return i - 1, pala, resultados

def automataLiteral(x, i):
    estado = 0
    literal, comiOsim = "", x[i]
    resultados = []
    while estado != 2:
        if i == len(x) - 1:
            resultados.append(f"Literal guardada: {literal}, Balance inapropiado de comillas")
            return -1, resultados
        if x[i] == comiOsim:
            estado = EstadosLiteral[estado][0]
        elif ord(x[i]) >= 0 and ord(x[i]) <= 126:
            literal += x[i]
            estado = EstadosLiteral[estado][1]
        else:
            estado = EstadosLiteral[estado][2]
        if estado == 3:
            resultados.append(f"Se encontro algo inapropiado en la literal: {literal}, numero de caracter: {i}")
            return -1, resultados
        i += 1
    resultados.append(f"Es una literal: {literal}")
    return i, resultados

def analisis(ca):
    linea, i, contador = 0, 0, 0
    resultados = []
    while i < len(ca) - 1:
        if ca[i].isdigit():
            i, res = automataNumeros(ca, i)
            resultados.extend(res)
            if i == -1:
                return -1, resultados
            contador += 1
        elif ca[i].isalpha():
            lo1 = automataPalabra(ca, i)
            i = lo1[0]
            if lo1[1] not in palabrasClave:
                resultados.append(f"Es un identificador: {lo1[1]}")
            else:
                resultados.append(f"Es una palabra clave: {lo1[1]}")
            contador += 1
        elif ca[i] in puntuadores:
            resultados.append(f"Es un puntuador: {ca[i]}")
            i += 1
            contador += 1
        elif ca[i] in operandos:
            ko = ca[i]
            if (ca[i] + ca[i + 1]) in operandosDobles:
                i += 1
                ko += ca[i]
            resultados.append(f"Es un operando: {ko}")
            i += 1
            if ko == "//":
                resultados.append(f"Es un comentario: {ca[i:]}")
                break
            contador += 1
        elif ca[i] == "\"" or ca[i] == "\'":
            i, res = automataLiteral(ca, i)
            resultados.extend(res)
            if i == -1:
                return -1, resultados
            contador += 1
        elif ca[i] == " " or ca[i] == "\t":
            i += 1
        else:
            return -1, resultados
    return 0, resultados, contador


		


