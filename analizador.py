import sys

estadosRealEN=[[1,4,7,7],[1,4,2,7],[3,7,7,7],[3,4,7,7]] #Tabla de transicion del automata para formar reales y enteros numero/operando/punto/otro(Error)

Estadospalabra = [[1,2,2],[1,1,2]] #Tabla de transicion para formar palabras con numeros: Letra/ Numero / otro (error)

EstadosLiteral = [[1,3,3],[2,1,3]] #Tabla de transicion para formar literales:  comillas/Caracter ASCII valido/ Otro(Error)

operandos=["+","-","*","/","^","%","<",">","!","&","|","="] #Este representa un automata, con un estado final al elegir una opcion

operandosDobles=["<=",">=","==","!=","&&","||","++","--","//","+="]

puntuadores = [";",".","#",",","(",")","[","]","{","}"] #Este representa un automata, con un estado final al elegir una opcion

palabrasClave = ["auto","else","long","switch","break","enum","registrer",
"typedef","case","extern","return","union","char","float","short",
"unsigned","const","for","signed","void","continue","goto","sizeof","volatile",
"default","if","static","while","do","int","struct","double","_Packed"] #Palabras reservadas en C

def automataNumeros(x, i):  # Se mantiene igual
    estado, soy, numero = 0, 0, ""
    resultados = []
    contador = 0
    while (estado != 4 and i < len(x) - 1):
        if (x[i].isdigit()):
            numero = numero + x[i]
            estado = estadosRealEN[estado][0]
            soy = estado
        elif (x[i] == "."):
            numero = numero + x[i]
            estado = estadosRealEN[estado][2]
        elif (x[i] in operandos or x[i] in puntuadores or x[i] == " "):
            soy = estado
            i = i - 1
            estado = estadosRealEN[estado][1]
        else:
            numero = numero + x[i]
            estado = estadosRealEN[estado][3]
        if (estado == 7):
            resultados.append(f"Error, se encontro algo inapropiado en el numero: {numero}, en el caracter {i-1}")
            return -1, resultados, contador
        i = i + 1
    if (soy == 1):
        resultados.append(f"Es un numero entero: {numero}")
    elif (soy == 3):
        resultados.append(f"Es un numero real: {numero}")
    contador += 1
    return i, resultados, contador

def automataPalabra(x, i):  # Se mantiene igual
    estado, pala = 0, ""
    resultados = []
    contador = 0
    while (estado != 2 and i <= len(x) - 1):
        if (x[i].isalpha()):
            pala = pala + x[i]
            estado = Estadospalabra[estado][0]
        elif (x[i].isdigit()):
            pala = pala + x[i]
            estado = Estadospalabra[estado][1]
        else:
            estado = Estadospalabra[estado][2]
        i = i + 1
    contador += 1
    return i - 1, pala, resultados, contador

def automataLiteral(x, i):  # Se mantiene igual
    estado = 0
    literal, comiOsim = "", x[i]
    resultados = []
    contador = 0
    while (estado != 2):
        if (i == len(x) - 1):
            resultados.append(f"Literal guardada: {literal}, Balance inapropiado de comillas")
            return -1, resultados, contador
        if (x[i] == comiOsim):
            estado = EstadosLiteral[estado][0]
        elif (ord(x[i]) >= 0 and ord(x[i]) <= 126):
            literal = literal + x[i]
            estado = EstadosLiteral[estado][1]
        else:
            estado = EstadosLiteral[estado][2]
        if (estado == 3):
            resultados.append(f"Se encontro algo inapropiado en la literal: {literal}, numero de caracter: {i}")
            return -1, resultados, contador
        i = i + 1
    resultados.append(f"Es una literal: {literal}")
    contador += 1
    return i, resultados, contador

def analisis(codigo):  # Procesa todas las líneas
    lineas = codigo.splitlines()  # Divide el código en varias líneas
    contador = 0
    resultados = []
    
    for linea in lineas:
        i = 0
        while i < len(linea):
            if linea[i].isdigit():
                i, res, c = automataNumeros(linea, i)
                resultados.extend(res)
                contador += c
                if i == -1:
                    return -1, resultados, contador
            elif linea[i].isalpha():
                lo1 = automataPalabra(linea, i)
                i, palabra, res, c = lo1[0], lo1[1], lo1[2], lo1[3]
                if palabra not in palabrasClave:
                    resultados.append(f"Es un identificador: {palabra}")
                else:
                    resultados.append(f"Es una palabra clave: {palabra}")
                contador += c
            elif linea[i] in puntuadores:
                resultados.append(f"Es un puntuador: {linea[i]}")
                i += 1
                contador += 1
            elif linea[i] in operandos:
                ko = linea[i]
                if i + 1 < len(linea) and (linea[i] + linea[i + 1]) in operandosDobles:
                    i += 1
                    ko += linea[i]
                resultados.append(f"Es un operando: {ko}")
                i += 1
                if ko == "//":  # Ignora el resto de la línea si es un comentario
                    resultados.append(f"Es un comentario: {linea[i:]}")
                    break
                contador += 1
            elif linea[i] == "\"" or linea[i] == "\'":
                i, res, c = automataLiteral(linea, i)
                resultados.extend(res)
                contador += c
                if i == -1:
                    return -1, resultados, contador
            elif linea[i] == " " or linea[i] == "\t":
                i += 1
            else:
                resultados.append(f"Error inesperado en la línea: {linea}")
                return -1, resultados, contador
    return 0, resultados, contador

