# -*- coding: utf-8 -*-
# Sistema de clasificación climática de Köppen, modificado por Enriqueta García.    #
# Programacion por Pablo Leautaud-Valenzuela Copyright 2012,2013  [v2.1]            #
# Mas informacion en: http://www.pablo-leautaud.com/home/proyectos/python/clima     #
# Contacto: leautaudp@igg.unam.mx                                                   #
#####################################################################################
#                                                                                   #
# Este programa es software libre. Puede redistribuirlo y/o modificarlo bajo los    #
# términos de la Licencia Pública General de GNU según es publicada por la Free     #
# Software Foundation, en su versión 3 o posterior.                                 # 
#                                                                                   #
# Este programa se distribuye con la esperanza de que sea útil, pero SIN NINGUNA    #
# GARANTÍA, incluso sin la garantía MERCANTIL implícita o sin garantizar la         #
# CONVENIENCIA PARA UN PROPÓSITO PARTICULAR. Véase la Licencia Pública General de   #
# GNU para más detalles.                                                            #
#                                                                                   #
# Debería haber recibido una copia de la Licencia Pública General junto con este    #
# programa. Si no ha sido así, visite http://www.gnu.org/licenses/.                 #
#####################################################################################


import os
import webbrowser

#Ajuste del tamaño de ventana en Windows
os.system("mode 80,35");

#Diccionarios y listas preliminares
meses = {1:'Enero', 2:'Febrero', 3:'Marzo', 4:'Abril', 5:'Mayo', 6:'Junio', 7:'Julio', 8:'Agosto', 9:'Septiembre', 10:'Octubre', 11:'Noviembre', 12:'Diciembre'}
mes_lis = [1,2,3,4,5,6,7,8,9,10,11,12]
D1 = {1:"(w2)(w),",2:"(w2),",3:"(w2)(x'),",4:"(x')(w2),",5:"x',",6:"s(x'),",7:"s,"}
D2 = {1:"(w1)(w),",2:"(w1),",3:"(w1)(x'),",4:"(x')(w1),",5:"x',",6:"s(x'),",7:"s,"}
D3 = {1:"(w0)(w),",2:"(w0),",3:"(w0)(x'),",4:"(x')(w0),",5:"x',",6:"s(x'),",7:"s,"}
D4 = {1:"w2(w),",2:"w2,",3:"w2(x'),",4:"x'(w2),",5:"x',",6:"s(x'),",7:"s,"}
D5 = {1:"w1(w),",2:"w1,",3:"w1(x'),",4:"x'(w1),",5:"x',",6:"s(x'),",7:"s,"}
D6 = {1:"w0(w),",2:"w0,",3:"w0(x'),",4:"x'(w0),",5:"x',",6:"s(x'),",7:"s,"}
D7 = {1:"w(w),",2:"w,",3:"w(x'),",4:"x'(w),",5:"x',",6:"s(x'),",7:"s,"}
dic_clima = {"A":"calido","A(C)":"semicalido","(A)Ca":"semicalido a templado con verano calido","(A)Cb":"semicalido a templado con verano fresco largo","BW":"muy arido","BS1":"semiarido","BS0":"arido","Ca":"templado con verano calido","Cb":"templado con verano fresco largo","Cb'":"semifrio con verano fresco larco","Cc":"semifrio con verano fresco corto","E(F)":"muy frio","EF":"muy frio","E(T)C":"frio (mes frio sobre cero)","E(T)":"frio (mes frio bajo cero)","(h')":"calido (t. mes frio sobre 18*C)","(h')h":"calido (t. mes frio bajo 18*C)","h'(h)":"semicalido (t. mes frio sobre 18*C)","h":"semicalido (t. mes frio bajo 18*C)","k":"templado con verano calido","k'":"templado con verano fresco","k''":"semifrio","w":"con lluvias en verano (lluvia invernal menor al 5%)","f":"con lluvias todo el año (lluvia invernal mayor al 10%)","(fm)":"lluvia invernal hasta 18%","(f)":"humedo con lluvias todo el año (lluvia invernal supera 18%)","f(m)":"humedo con lluvias todo el año (lluvia invernal hasta 18%)","m(w)":"humedo con lluvias en verano (lluvia invernal menor al 5%)","m":"humedo con lluvias en verano (lluvia invernal entre 5 y 10%)","m(f)":"humedo con lluvias en verano (lluvia invernal supera el 10%)","(m)(w)":"humedo con lluvias en verano (lluvia invernal menor al 5%)","(m)(f)":"humedo con lluvias en verano (lluvia invernal supera el 10%)","H":"frio de altura (+3,000 m.s.n.m)","(i)":"temperatura anual isotermal","(i')":"temperatura anual con poca oscilacion","(e)":"temperatura anual extremosa","(e')":"temperatura anual muy extremosa","g":"marcha de temperatua anual tipo Ganges","w''":"presenta canicula","(w2)(w)":"subhumedo con lluvias en verano (lluvia invernal menor al 5% )","(w2)":"subhumedo con lluvias en verano (lluvia invernal entre 5 y 10% )","(w2)(x')":"subhumedo con lluvias en verano (lluvia invernal supera el 10% )","(x')(w2)":"subhumedo con lluvias todo el año (lluvia invernal menor al 18%)","x'":"con lluvias todo el año (lluvia invernal supera el 18%)","s(x')":"con lluvias en invierno (lluvia invernal menor al 36%)","s":"con lluvias en invierno (lluvia invernal mayor al 36%)","(w1)(w)":"subhumedo con lluvias en verano (lluvia invernal menor al 5% )","(w1)":"subhumedo con lluvias en verano (lluvia invernal entre 5 y 10% )","(w1)(x')":"subhumedo con lluvias en verano (lluvia invernal supera el 10% )","(x')(w1)":"subhumedo con lluvias todo el año (lluvia invernal menor al 18%)","(w0)(w)":"subhumedo con lluvias en verano (lluvia invernal menor al 5% )","(w0)":"subhumedo con lluvias en verano (lluvia invernal entre 5 y 10% )","(w0)(x')":"subhumedo con lluvias en verano (lluvia invernal supera el 10% )","(x')(w0)":"subhumedo con lluvias todo el año (lluvia invernal menor al 18%)","w2(w)":"subhumedo con lluvias en verano (lluvia invernal menor al 5% )","w2":"subhumedo con lluvias en verano (lluvia invernal entre 5 y 10% )","w2(x')":"subhumedo con lluvias en verano (lluvia invernal supera el 10% )","x'(w2)":"subhumedo con lluvias todo el año (lluvia invernal menor al 18%)","w1(w)":"subhumedo con lluvias en verano (lluvia invernal menor al 5% )","w1":"subhumedo con lluvias en verano (lluvia invernal entre 5 y 10% )","w1(x')":"subhumedo con lluvias en verano (lluvia invernal supera el 10% )","x'(w1)":"subhumedo con lluvias todo el año (lluvia invernal menor al 18%)","w0(w)":"subhumedo con lluvias en verano (lluvia invernal menor al 5% )","w0":"subhumedo con lluvias en verano (lluvia invernal entre 5 y 10% )","w0(x')":"subhumedo con lluvias en verano (lluvia invernal supera el 10% )","x'(w0)":"subhumedo con lluvias todo el año (lluvia invernal menor al 18%)","w(w)":"con lluvias en verano (lluvia invernal menor al 5% )","w(x')":"con lluvias en verano (lluvia invernal supera el 10% )","x'(w)":"con lluvias todo el año (lluvia invernal menor al 18%)"}

#Definicion de variables 
estacion = 'Sin nombre'
altura = 1234
temp_mes_lis = ['1,2,3']
temp_mes_dic = 1
pres_mes_lis = ['1,2,3']
pres_mes_dic = 1
PreD = ''
PL2 = ''
PS2 = ''
TC2 = ''
TF2 = ''
PL1 = ''
PS1 = ''
TC1 = ''
TF1 = ''
mes_humedo = ''
mes_seco = ''
mes_calido = ''
mes_frio = ''
PA = ''
TA = ''
PT = ''
PPI = ''
PPV = ''
MD = ''
OS = ''
RL = ''
RS = ''
RH = ''
GF = ''
H = ''
X1 = ''
texto = ''
continua = 'si'
opcion = 0
mescan = 'Sin canicula'
ww = 0

#Reset de variables
def reset():
    global estacion
    global altura
    global temp_mes_lis
    global temp_mes_dic
    global pres_mes_lis
    global pres_mes_dic
    global PreD
    global PL2
    global PS2
    global TC2
    global TF2
    global PL1
    global PS1
    global TC1
    global TF1
    global mes_humedo
    global mes_seco
    global mes_calido
    global mes_frio
    global PA
    global TA
    global PT
    global PPI
    global PPV
    global MD
    global OS
    global RL
    global RS
    global RH
    global GF
    global H
    global X1
    global texto
    global continua
    global opcion
    global mescan
    global ww
    ##
    estacion = 'Sin nombre'
    altura = 1234
    temp_mes_lis = ['1,2,3']
    temp_mes_dic = 1
    pres_mes_lis = ['1,2,3']
    pres_mes_dic = 1
    PreD = ''
    PL2 = ''
    PS2 = ''
    TC2 = ''
    TF2 = ''
    PL1 = ''
    PS1 = ''
    TC1 = ''
    TF1 = ''
    mes_humedo = ''
    mes_seco = ''
    mes_calido = ''
    mes_frio = ''
    PA = ''
    TA = ''
    PT = ''
    PPI = ''
    PPV = ''
    MD = ''
    OS = ''
    RL = ''
    RS = ''
    RH = ''
    GF = ''
    H = ''
    X1 = ''
    texto = ''
    continua = 'si'
    opcion = 0
    mescan = 'Sin canicula'
    ww = 0


#Menu principal
def menu():
    os.system('CLS')
    global continua
    print '-------------------------------------------------------------------------------'
    print 'Sistema de clasificacion climatica de Koppen, modificado por Enriqueta Garcia.'
    print 'Programacion por Pablo Leautaud-Valenzuela, Copyright 2012,2013 GNU GPL v3.'
    print 'v 2.3  [28/01/2013]'
    print ' '
    print 'Cualquier comentario a leautaudp@igg.unam.mx*'
    print '*Por limitaciones del sistema no se pueden incluir acentos o caracteres \nespeciales en este programa.'
    print '-------------------------------------------------------------------------------'
    print ' '
    print ' '
    print 'Que desea hacer?'
    print ' '
    print '1. Clasificar el clima de una estacion.'
    print '2. Clasificar el clima de una estacion (verboso).'
    print '3. Consultar datos climatologicos'
    print '4. Salir'
    print ' '
    print ' '
    opcion = raw_input('Indique el numero de opcion: ')
    comp = opcion.isdigit()
    if comp == False:
        os.system('CLS')
        print 'Tienes que escribir un numero...'
        print ' '
        raw_input('Intenta de nuevo, presiona <ENTER> para continuar.')
        opcion = 0
        return opcion
    else:
        opcion = int(opcion)
        return opcion

#Ingreso de los datos climatologicos
def datos():
    global estacion
    global altura
    global temp_mes_lis
    global pres_mes_lis
    global temp_mes_dic
    global pres_mes_dic
    temp = 1
    prec = 1
    
    #Ingreso datos estacion
    estacion = raw_input('Cual es el nombre de la estacion? ')
    if estacion == '':
        estacion = 'Sin nombre'
    print ' ' 
    altura = raw_input('Cual es la altitud (en metros) de la estacion? ')
    if altura == '':
        altura = 1234
    elif altura.endswith("m") or altura.endswith("."):
        altura = altura[:-1]
        altura = int(altura)
    else:
        altura = int(altura)
    os.system('CLS')

    #Ingreso datos temperatura
    while temp == 1:
        print "Introduce los datos de temperatura media mensual (en centigrados) separados por comas (,) y en manera consecutiva (sin espacios) e.g. \"18.5,22,33.1,...n\", donde 18.5 grados son para enero, 22 para febrero, 33.1 para marzo, etc."
        print ' ' 
        temp_mes_lis = raw_input('Datos temperatura: ')
        if temp_mes_lis == '':
            os.system('CLS')
            temp = 1
            print 'Este campo no puede quedar en blanco'
            print ''
            raw_input('Intentalo de nuevo <ENTER>')
            os.system('CLS')
        else:
            try:
                temp_mes_lis = [float(i) for i in temp_mes_lis.split(',')]
                if len(temp_mes_lis) != 12:
                    os.system('CLS')
                    temp = 1
                    print 'Tienes que introducir 12 datos!'
                    print ''
                    raw_input('Intentalo de nuevo <ENTER>')
                    os.system('CLS')
                else:
                    temp_mes_dic = dict(zip(mes_lis, temp_mes_lis))
                    temp = 0
                    os.system('CLS')
            except ValueError:
                os.system('CLS')
                temp = 1
                print 'Oh no! Hay un error en los datos introducidos'
                print ''
                raw_input('Intentalo de nuevo <ENTER>')
                os.system('CLS')

    #Ingreso datos precipitacion
    while prec == 1:
        print "Introduce los datos de precipitacion total mensual (en milimetros) separados por comas (,) y en manera consecutiva (sin espacios) e.g. \"750,300,1050,...n\", donde 750 mm de precipitacion son para enero, 300 para febrero, 1050 para marzo, etc."
        print ' ' 
        pres_mes_lis = raw_input('Datos precipitacion: ')
        if pres_mes_lis == '':
            os.system('CLS')
            prec = 1
            print 'Este campo no puede quedar en blanco'
            print ''
            raw_input('Intentalo de nuevo <ENTER>')
            os.system('CLS')
        else:
            try:
                pres_mes_lis = [float(i) for i in pres_mes_lis.split(',')]
                if len(pres_mes_lis) != 12:
                    os.system('CLS')
                    prec = 1
                    print 'Tienes que introducir 12 datos!'
                    print ''
                    raw_input('Intentalo de nuevo <ENTER>')
                    os.system('CLS')
                else:
                    pres_mes_dic = dict(zip(mes_lis, pres_mes_lis))
                    prec = 0
                    os.system('CLS')
            except ValueError:
                os.system('CLS')
                prec = 1
                print 'Oh no! Hay un error en los datos introducidos'
                print ''
                raw_input('Intentalo de nuevo <ENTER>')
                os.system('CLS')

    

##################################################################

#Calculos iniciales
def calculos():
    global PL2
    global PS2
    global TC2
    global TF2
    global PL1
    global PS1
    global TC1
    global TF1
    global mes_humedo
    global mes_seco
    global mes_calido
    global mes_frio
    global PA
    global TA
    global PT
    global PPI
    global PPV
    global MD
    global OS
    global X1
    
    PL2 = max(pres_mes_dic, key=pres_mes_dic.get) #Mes mas lluvioso (humedo)
    PS2 = min(pres_mes_dic, key=pres_mes_dic.get) #Mes menos lluvioso (seco)
    TC2 = max(temp_mes_dic, key=temp_mes_dic.get) #Mes mas calido
    TF2 = min(temp_mes_dic, key=temp_mes_dic.get) #Mes mas frio

    PL1 = pres_mes_dic [PL2]#Precipitacion mes mas lluvioso (pres_max)
    PS1 = pres_mes_dic [PS2] #Precipotacion mes menos lluvioso (pres_min)
    TC1 = temp_mes_dic [TC2] #Temperatura mes mas calido (temp_max)
    TF1 = temp_mes_dic [TF2] #Temperatura mes frio (temp_min)

    mes_humedo = meses [PL2]
    mes_seco = meses [PS2]
    mes_calido = meses [TC2]
    mes_frio = meses [TF2]

    PA = sum(pres_mes_lis) #Precipitacion total anual
    PA = round(PA,1)
    TA = (sum(temp_mes_lis)/12)#Temperatura media anual 
    TA = round(TA,1) 
    PT = PA/TA #Cociente P/T o indice Lang
    PT = round(PT,1)
    PPI = ((pres_mes_dic[1]+pres_mes_dic[2]+pres_mes_dic[3])/PA)*(100.0)#Porcentaje lluvia invernal
    PPI = round(PPI,1)
    PPV = ((pres_mes_dic[6]+pres_mes_dic[7]+pres_mes_dic[8]+pres_mes_dic[9])/PA)*(100.0)#Porcentaje lluvia en verano
    PPV = round(PPV,1)
    MD = 0
    for i in temp_mes_lis:
        if i > 10:
            MD = MD + 1 #Meses con temperatura superior a los 10 grados
    OS = TC1 - TF1
    OS = round(OS,1)

    X1 = (60-((PA-1000)/31)) #/31 no impreso

##################################################################

####Modulo de inicio
##Se obtienen valores para RL, RH, RS, GF y H

def inicio():
    global RL
    global RH
    global RS
    global GF
    global H
    
    #Valor para RL
    if PL2 >= 5 and PL2 <= 10:
        if PL1 >= (PS1*10):
            RL = 1
        else: RL = 2
    elif (PL1/(PS1+1)) > 3:
        RL = 3
    else: RL = 2

    #Valores cuando RL = 1
    if RL == 1:
        if PPI <= 5:
            RH = (2*TA)+28
            RS = RH/2
            GF = 1
        elif PPI < 10.2:
            RH = (2*TA)+28
            RS = RH/2
            GF = 2
        else:
            RH = (2*TA)+21
            RS = RH/2
            GF = 3

    #Valores cuando RL = 2
    if RL == 2:
        if PPI < 18:
            RH = (2*TA)+14
            RS = RH/2
            GF = 4
        else:
            RH = (2*TA)+14
            RS = RH/2
            GF = 5

    #Valores cuando RL = 3
    if RL == 3:
        if PPI < 36:
            RH = (2*TA)
            RS = RH/2
            GF = 6
        else:
            RH = (2*TA)
            RS = RH/2
            GF = 7

    #Valor de H
    if RH < (PA/10):
        H = 1
    else:
        H = 0
################################

####Definicion de los modulos
#Modulo 1A - Determinacion de los climas aridos (BW) y semisecos (BS), y de los muy frios [E(F)]
def modulo1A():
    if -2 < TA < 5:
        salida = modulo2()
    elif TC1 < 0:
        salida = texto + "E(F)," + modulo10pre()
    elif H == 0:
        if RS > (PA/10):
            salida = texto + "BW," + modulo1B()
        elif PT > 22.9:
            salida = texto + "BS1," + modulo1B()
        else:
            salida = texto + "BS0," + modulo1B()
    else:
        salida = modulo4A()
    return salida

#Modulo 1B - Determinacion de subtipos para climas secos [B]
def modulo1B():
    if TA > 22:
        if TF1 > 18:
            salida = texto + "(h')," + modulo6()
        else:
            salida = texto + "(h')h," + modulo6()
    elif TA > 18:
        if TF1 > 10:
            salida = texto + "h'(h)," + modulo6()
        else:
            salida = texto + "h," + modulo6()
    elif TA > 12:
        if TF1 > -3:
            if TC1 < 18:
                salida = texto + "k'," + modulo6()
            else:
                salida = texto + "k," + modulo6()
        else:
            salida = modulo3A()
    else:
        salida = texto + "k''," + modulo6()
    return salida

#Modulo 2 - Determinacion y diferencia de los climas frios [E]
def modulo2():
    if TF1 > 0 and 0 < TC1 < 6.5:
        salida = texto + "E(T)C," + modulo10pre()
    else:
        salida = texto + "E(T)," + modulo10pre()
    return salida

#Modulo 3A - Determinacion de climas boreales [D] no hay en Mexico
def modulo3A():
    if TF1 < -38:
        salida = texto + "Dd," + modulo3B()
    elif TC1 > 22:
        salida = texto + "Da," + modulo3B()
    elif MD < 4:
        salida = texto + "Dc," + modulo3B()
    else:
        salida = texto + "Db," + modulo3B()
    return salida

#Modulo 3B - Asignacion de regimen de lluvia [w] y [f]
def modulo3B():
    if RL == 1:
        salida = texto + "w," + modulo5()
    else:
        salida = texto + "f," + modulo5()
    return salida

#Modulo 4A - Determinacion de climas calidos (tropicales) [A] y semicalidos [A(C)]
def modulo4A():
    if TF1 > 18:
        if TA > 22:
            salida = texto + "A," + modulo8A()
        else:
            salida = texto + "A(C)," + modulo8A()
    else:
        salida = modulo4B()
    return salida

#Modulo 4B - Modulo de transito
def modulo4B():
    if TF1 > -3:
        if TC1 > 6.5:
            salida = modulo4C()
        else:
            salida = modulo2()
    else:
        salida = modulo3A()
    return salida

#Mudulo 4C - Determinacion y diferencia de climas calidos [A] y templados [C]
def modulo4C():
    if TA > 18:
        if TC1 > 22:
            salida = texto + "(A)Ca," + modulo4D()
        else:
            salida = texto + "(A)Cb," + modulo4D()
    elif TA > 12:
        if TC1 > 22:
            salida = texto + "Ca," + modulo4D()
        else:
            salida = texto + "Cb," + modulo4D()
    elif TA > 5:
        if MD < 4:
            salida = texto + "Cc," + modulo4D()
        else:
            salida = texto + "Cb'," + modulo4D()
    else:
        salida = texto + "EF," + modulo4D()
    return salida

#Modulo 4D - Regimen de lluvias invernales en climas humedos [A o C]
def modulo4D():
    if PS1 > 40:
        if PPI < 18:
            salida = texto + "(fm)," + modulo5()
        else:
            salida = texto + "(f)," + modulo5()
    else:
        salida = modulo9()
    return salida


#Modulo 5 - Nivel de oscilacion en la temperatura
def modulo5():
    if OS <= 5:
        salida = texto + "(i)," + modulo7()
    elif OS <= 7:
        salida = texto + "(i')," + modulo7()
    elif OS <= 14:
        salida = texto + "(e)," + modulo7()
    else:
        salida = texto + "(e')," + modulo7()
    return salida

#Modulo 6 - Asignacion de subtipos para climas secos [b]
def modulo6():
    salida = texto + D7[GF] + modulo5()
    return salida

#Modulo 7 - Marcha anual de temperatura [Ganges]
def modulo7():
    if TC2 <= 6:
        salida = texto + "g," + modulo11()
    else:
        salida = texto + modulo11()
    return salida

#Modulo 8A - Determinacion de tipos para climas calidos y templados [A o C]
def modulo8A():
    if PS1 > 60:
        if PPI < 18:
            salida = texto + "f(m)," + modulo5()
        else:
            salida = texto + "f," + modulo5()
    if PS1 > X1: #/31 no impreso
        if PPI < 5:
            salida = texto + "m(w)," + modulo5()
        elif PPI < 10.2:
            salida = texto + "m," + modulo5()
        else:
            salida = texto + "m(f)," + modulo5()
    else:
        salida = modulo8B()
    return salida

#Modulo 8B - Determinacion de subtipos para climas calidos y templados [A o C]
def modulo8B():
    if PT > 55.3:
        salida = texto + D4[GF] + modulo5()
    elif PT > 43.2:
        salida = texto + D5[GF] + modulo5()
    else:
        salida = texto + D6[GF] + modulo5()
    return salida

#Modulo 9 - Determinacion de tipos para climas calidos [A]
def modulo9():
    if PS1 > (-1)*((PA-1740)/31): # (-1) puede ser 60-
        if PPI < 5:
            salida = texto + "(m)(w)," + modulo5()
        elif PPI < 10.2:
            salida = texto + "m(f)," + modulo5()
        else:
            salida = texto + "(m)(f)," + modulo5()
    else:
        salida = modulo10()
    return salida

#Modulo 10 - Determinacion de subtipos para climas frios [E]
def modulo10():
    if PT > 55:
        salida = texto + D1[GF] + modulo5()
    elif PT > 43.2:
        salida = texto + D2[GF] + modulo5()
    else:
        salida = texto + D3[GF] + modulo5()
    return salida

#Modulo 10 pre - Estaciones arriba de 3000 msnm para climas frios [E]
def modulo10pre():
    if altura >= 4000:
        salida = texto + "H," + modulo10()
    else:
        salida = modulo10()
    return salida

#Modulo 11 - Determinacion de la canicula
def modulo11():
    global mescan
    global ww
    PreD = pres_mes_dic
    if RL == 1 or RL == 2:
        if PreD [7] < (PreD [6]):
            if PreD [7] <= PreD [8]:
                salida = texto + "w''"
                mescan = 'julio'
                ww = 1
            elif PreD [7] <= PreD [9]:
                salida = texto + "w''"
                mescan = 'julio'
                ww = 1
            else:
                salida = texto
        elif PreD [8] < (PreD [9]):
            if PreD [8] <= PreD [7]:
                salida = texto + "w''"
                mescan = 'agosto'
                ww = 1
            elif PreD [8] <= PreD [6]:
                salida = texto + "w''"
                mescan = 'agosto'
                ww = 1
            else:
                salida = texto
        elif PreD [9] < (PreD [10]):
            if PreD [9] <= PreD [8]:
                salida = texto + "w''"
                mescan = 'septiembre'
                ww = 1
            elif PreD [9] <= PreD [7]:
                salida = texto + "w''"
                mescan = 'septiembre'
                ww = 1
            else:
                salida = texto
        else:
            salida = texto
    else:
        salida = texto
    return salida



################################
###Presentacion de resultados
def resultados():
    global texto
    if texto.endswith(","):
        texto = texto[:-1]
        
    clima_list = [str(i) for i in texto.split(',')]
    clima = ''
    clima = clima.join(clima_list)

    des = ' ' 
    for i in clima_list:
        des = des + dic_clima[i] + ", "
    if ww == 1:
        des = des[:-2]
        des = des + " en " + mescan + "  "
    des = des[:-2] + "."

    print 'La climatologia para la estacion ' + estacion + ' es la sigiente:'
    print ' '
    print 'Clima: ' + clima
    print 'Detalle: ' + str(clima_list)
    print ' '
    print 'Descripcion: Clima ' + des
    print ' '
    print "Mes mas lluvioso: "+ mes_humedo + ' (' + "%.1f" % (PL1) + ' mm)'
    print "Mes mas seco: "+ mes_seco + ' (' + "%.1f" % (PS1) + ' mm)'
    print "Mes mas calido: "+ mes_calido + ' (' + "%.1f" % (TC1) + ' C)'
    print "Mes mas frio: "+ mes_frio + ' (' + "%.1f" % (TF1) + ' C)'
    print ' '
    print "Precipitacion anual total: "+ "%.1f" % (PA) + ' mm'
    print "Temperatura media anual: "+ "%.1f" % (TA) + ' C'
    print "Indide Lang (PA/TA): "+ "%.1f" % (PT)
    print "% Precip. Invierno: "+ "%.1f" % (PPI)
    print "% Precip. Verano: "+ "%.1f" % (PPV)
    print "Meses con temp. >10*C: "+ `MD` 
    print "Oscilacion anual temp.: "+ "%.1f" % (OS)
    print ' '
    texto = ''


def resultados2():
    global texto
    if texto.endswith(","):
        texto = texto[:-1]
        
    clima_list = [str(i) for i in texto.split(',')]
    clima = ''
    clima = clima.join(clima_list)

    des = ' ' 
    for i in clima_list:
        des = des + dic_clima[i] + ", "
    if ww == 1:
        des = des[:-2]
        des = des + " en " + mescan + "  "
    des = des[:-2] + "."

    reg = ''
    if RL == 1:
        reg = '(Verano)'
    if RL == 2:
        reg = '(Intermedio)'
    if RL == 3:
        reg = '(Invierno)'

    print 'La climatologia para la estacion ' + estacion + ' es la sigiente:'
    print ' '
    print 'Clima: ' + clima
    print 'Detalle: ' + str(clima_list)
    print ' '
    print 'Descripcion: Clima ' + des
    print ' '
    print "[PL1] Mes mas lluvioso: "+ mes_humedo + ' (' + "%.1f" % (PL1) + ' mm)'
    print "[PS1] Mes mas seco: "+ mes_seco + ' (' + "%.1f" % (PS1) + ' mm)'
    print "[TC1] Mes mas calido: "+ mes_calido + ' (' + "%.1f" % (TC1) + ' C)'
    print "[TF1] Mes mas frio: "+ mes_frio + ' (' + "%.1f" % (TF1) + ' C)'
    print ' '
    print "[PA] Precipitacion anual total: "+ "%.1f" % (PA) + ' mm'
    print "[TA] Temperatura media anual: "+ "%.1f" % (TA) + ' C'
    print "[PT] Indide Lang (PA/TA): "+ "%.1f" % (PT)
    print "[PPI] % Precip. Invierno: "+ "%.1f" % (PPI)
    print "[PPV] % Precip. Verano: "+ "%.1f" % (PPV)
    print "[MD] Meses con temp. >10*C: "+ `MD` 
    print "[OS] Oscilacion anual temp.: "+ "%.1f" % (OS)  
    print ' '
    print "[RL] Regimen de lluvia: "+ `RL` + reg
    print "[rH] Limite climas secos, humedos y subhumedos: "+ "%.1f" % (RH)
    print "[rS] Limite climas aridos y muy aridos: "+ "%.1f" % (RS)
    print "[GF] Tipo de de clima segun grupo/subgrupo: "+ `GF`
    print "[H] Indicador de climas aridos/muy aridos (1): "+ `H`
    print "[X1] Calculo para separar climas humedos: "+ "%.1f" % (X1)
    print ' '
    texto = ''

#####################################
####
#Ejecucion del programa
while continua == 'si':
    os.system('CLS')
    opcion = menu()
    if opcion == 1:
        os.system('CLS')
        reset()
        datos()
        calculos()
        inicio()
        texto = texto + modulo1A()
        resultados()
        continua = 'si'
        print ' '
        print ' '
        print ' '
        raw_input('Presiona <ENTER> para regresar al menu principal.')
    elif opcion == 2:
        os.system('CLS')
        reset()
        datos()
        calculos()
        inicio()
        texto = texto + modulo1A()
        resultados2()
        continua = 'si'
        print ' '
        print ' '
        print ' '
        raw_input('Presiona <ENTER> para regresar al menu principal.')
    elif opcion == 3:
        os.system('CLS')
        url='http://smn.cna.gob.mx/index.php?option=com_content&view=article&id=42&Itemid=75'
        webbrowser.open(url,new=2,autoraise=True)
        print "Se esta abriendo una pagina de internet donde puedes consultar las normales climatologicas en linea, e incluso descargar un archivo para consultarlas via Google Earth. En caso contrario una busqueda 'smn normales climatologicas' en Google te llevara a la liga correcta."
        print ' '
        print ' '
        raw_input('Presiona <ENTER> para regresar al menu principal.')
        continua == 'si'
    elif opcion == 4:
        break
    elif opcion == 0:
        continua == 'si'
    else:
        os.system('CLS')
        print ' '
        raw_input('Intenta de nuevo, presiona <ENTER> para continuar.')
        continua == 'si'       



