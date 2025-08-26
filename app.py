#VARIABLES FIJAS
vocal="aeiou"
vocaltilde = "áéíóú"
consonante="bcdfghjklmnñpqrstvwxyz"

texto0 = "Bienvenido a Calculadora de texto @lukitasdtd"
#TEXTOS DESPEDIDA
textod1 = "Gracias por utilizar Calculadora de texto @lukitasdtd"
textod2 = "@lukitasdtd te agradece"

#TEXTO SOLICITUDES
textos0_1 = "Ingrese opción: "
textos0 = "Ingresa la palabra o frase: "
textos1 = "¿Desea realizar una tarea en especifico?"
textos1_0 = "¿Desea realizar otra tarea en especifico?"
textos1_3 = "¿Desea re-ingresar al programa?"
textos1_2 = "¿Desea ingresar al programa?"
textos1_1 = "Si (1) o No (2): "
textos2 = "Contabilizar vocales (1)"
textos3 = "Contabilizar Consonantes (2)"
textos4 = "Contabilizar vocales y consonantes (3)"
textos5 = "Conoce si tu palabra es palindromo (se lee igual si esta invertida) (4)"
textos6 = "Salir (0)"
#TEXTO RESULTADOS
textor0 = "La palabra ingresada no es Palindromo"
textor1 = "La palabra ingresada si es Palindromo"
textor2 = "La palabra ingresada al parecer es un numero"
textor3 = "No has ingresado al parecer una palabra"


#funcion universal de contar caracteres
def contador (palabra,caracter):
    contador=0
    total = 0
    dict = {}
    for c0 in caracter:
        #c0 variable temporal de caracteres a entregar (vocales,consonantes)
        for c1 in palabra:
            #c1 variable temporal de el caracter individual de la palabra entregada
            #minusculas
            if c0 == c1:
                if c0 not in dict:
                    contador = 1
                    total += 1
                    dict[c0] = contador
                else:
                    contador += 1
                    total += 1
                dict [c0] = contador
            #mayusculas
            elif c0.upper() == c1:
                if c0.upper() not in dict:
                    contador = 1
                    total += 1
                    dict[c0.upper()] = contador
                else:
                    contador += 1
                    total += 1
                dict [c0.upper()] = contador        
    #tilde
    for c0 in vocaltilde:
        for c1 in palabra:
            #minusculas
            if c0 == c1:
                if c0 not in dict:
                    contador = 1
                    total += 1
                    dict[c0] = contador
                else:
                    contador += 1
                    total += 1
                dict [c0] = contador
                #mayusculas
            elif c0.upper() == c1:
                if c0.upper() not in dict:
                    contador = 1
                    total += 1
                    dict[c0.upper()] = contador
                else:
                    contador += 1
                    total += 1
                dict [c0.upper()] = contador              
    dict ["Total"] = total
    if dict ["Total"]== 0:
        return textor2
    else: 
        return dict                  

# Funciones principales, contadores de caracteres y palindromo
def principal(palabra,operacion):
#Solo vocales
    if operacion == 1:
        r = f"Vocales: {contador (palabra,vocal)}"
        # r es la variable del resultado a solicitar
        return r
    # retorno de resultado
#Solo consonantes
    elif operacion == 2:
        r = f"Consonantes: {contador (palabra,consonante)}"
        # r es la variable del resultado a solicitar
        return r 
        # retorno de resultado
#Ambos
    elif operacion == 3:
        r1 = f"Consonantes: {contador (palabra,consonante)}"
        r2 = f"Vocales: {contador (palabra,vocal)}"
        # r es la variable del resultado a solicitar, r1 siendo consonantes y r2 siendo vocales
        return (r1,r2)
        # retorno de ambos resultado
#palindromo
#palindromos le leen igual al reverso y derecho
    elif operacion == 4:
        palabra_r = palabra[::-1]
        #realiza el reverso de una palabra
        print (palabra_r)
        if palabra == palabra_r:
            return textor1
        return textor0

#---------------------PROGRAMA PRINCIPAL------------------------------------------------------------------------#
def ejecucion ():
    print (f"\n{texto0}\n{textos1_2}\n{textos1_1}")
    operacion = int(input(textos0_1))
    while operacion == 1:
        print (f"\n{textos1}\n{textos2}\n{textos3}\n{textos4}\n{textos5}\n{textos6}")
        # formato de texto con saltos de linea (\n)
        op_interna = int(input (textos0_1))
        if op_interna >=1 and op_interna <=4:
            palabra = input (textos0)
            while len(palabra) == 0:
                print (textor3)
                palabra = input (textos0)
            print (principal (palabra,op_interna))
        else:
            operacion = 2
    if operacion == 2:
        print (f"\n{textod1}\n{textod2}")

ejecucion()
