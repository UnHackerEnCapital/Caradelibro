import os
import re
import webbrowser

## Banner cabecera del Script ## :)
print("********************************************")
header =(r'''
     _________
    / ======= \
   / __________\
  | ___________ |
  | | -       | |
  | |         | |       OSINT 2021
  | |_________| |________________________
  \=____________/    Cara de Libro       )
  / """"""""""" \      Investigador     /
 / ::::::::::::: \                  =D-'
(_________________)
¬ by Nahuel Sagardoy
°°°°°°°°°°°°°°°°°°°°° ''')
print(header) 
menu = """
Bienvenido a 'Cara De Libro Investigador', un script que te
ayudara a realizar consultas OSINT en la red social facebook.

[1] Obtener ID de Usuario
[2] Realizar Busquedas dentro de un Perfil
[3] Ver Amigos de un Perfil (Amistades , Parientes, Conocidos)
[4] Ver Likes de un Perfil (Gustos, Hobbies)
[5] Ver Amigos en Comun entre dos Perfiles
[6] Salir
"""
idu =0

def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce una opcion del 1 al 6: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
 
    print (menu)
     
    print ("Elige una opcion")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        os.system("cls")
        print(header)
        print("")
        print("Pegue la URL del Usuario y presione Enter: ")
        print("*********************************************")
        print("por ejemplo : https://www.facebook.com/xxxxxx")
        print("")
        usuario= input()
        fburl='fburl'+'='+usuario+'&check=Lookup'
        rcurl= os.popen('curl -X POST https://lookup-id.com/ -H "Content-Type: application/x-www-form-urlencoded" -d' +  '"'+fburl+'"').read()
        idu = re.findall('[>]\d+\d+\d+',rcurl)
        idu= str(idu)
        idu = re.findall('\d+',idu)
        idu= str(idu)[2:-2]
        print("")
        print("******************************")
        print ("El ID del Usuario es: " + idu)
        print("")
        print("presione una tecla para volver al menu")
        input()
        os.system("cls")
        print(header)
        
        



    elif opcion == 2:
        os.system("cls")
        print(header)
        print("")
        print("Este Modulo te ayudara a filtrar por un punto de busqueda especifico")
        print("*******************************************************************")
        print ("Se recomienda buscar palabras como nombre, sobrenombre, gustos, lugares... ")
        print("Relacionados al Usuario en cuestion")
        print("")
        print("Recuerda tener la sesion iniciada de Facebook en tu navegador por defecto")
        if not idu == 0:
                print("Desea Utilizar el Perfil consultado previamente? (1- SI | 2- NO)")
                previo = input()
                if previo == '1':
                    print("Ahora ingrese la palabra a Buscar en el Perfil y presione Enter")
                    palabramagica = input()
                    webbrowser.open('https://www.facebook.com/profile/' + idu + '/search/?q=' + palabramagica)
                    os.system("cls")
                    print(header)
                elif previo == '2':
                        print("Ingrese el ID del Perfil del Usuario ")
                        print("En caso de no tenerlo puede conseguirlo desde el menu anterior opcion 1")
                        idu= input()
                        print("Ahora ingrese la palabra a Buscar en el Perfil y presione Enter")
                        palabramagica = input()
                        webbrowser.open('https://www.facebook.com/profile/' + idu + '/search/?q=' + palabramagica)
                        os.system("cls")
                        print(header)
                else:
                    print("Debe seleccionar 1 o 2") 
                        
        else:
            print("Ingrese el ID del Perfil del Usuario ")
            print("En caso de no tenerlo puede conseguirlo desde el menu anterior opcion 1")
            id= input()
            print("Ahora ingrese la palabra a Buscar en el Perfil y presione Enter")
            palabramagica = input()
            webbrowser.open('https://www.facebook.com/profile/' + idu + '/search/?q=' + palabramagica)
            os.system("cls")
            print(header)
    
        
        
    elif opcion == 3:    
        os.system("cls")
        print(header)
        print("")
        print("Este Modulo te ayudara a Buscar los Amigos de un ¨Perfil")
        print("Se abriran 4 Pestañas que corresponde la Primera a Amigos directos")
        print("Si la primera no aroja resultados el resto permite recolectarlos por medio de :")
        print("Fechas Festivas como Publicaciones del Dia del Amigo, Navidad, Cumpleaños ...:")
        print("*******************************************************************")
        print("")
        print("Recuerda tener la sesion iniciada de Facebook en tu navegador por defecto")
        if not idu == 0:
                print("Desea Utilizar el Perfil consultado previamente? (1- SI | 2- NO)")
                previo = input()
                if previo == '1':
                    webbrowser.open('https://www.facebook.com/' + idu + '/friends')
                    os.system("cls")
                    print("***********************************************")
                    print("")
                    print("SEGUNDO METODO DE BUSQUEDA MANUAL DE RELACIONES")
                    print("")
                    print("***********************************************")
                    print("")
                    print("A Continuacion se abrira una nueva ventana en explorador")
                    print("Presiones CTRL+U o ingrese view-source delante de la pagina para ver el Codigo Fuente ")
                    print("Presione la tecla CTRL+F y busque fbid= , cada resultador correspondera al ID de un perfil")
                    print("correspondiente a amigos de dicho usuario")
                    print("")
                    print("")
                    input("Presione ENTER para Continuar")
                    webbrowser.open('https://www.facebook.com/profile.php?id='+ idu +'&sk=photos_of')
                    os.system("cls")
                    print("")
                    print("**************************************************************")
                    print("")
                    print("Ahora se procedera utilizar filtros por default para maximizar los resultados")
                    print("")
                    print("")
                    input("Presione ENTER para Continuar")
                    webbrowser.open('https://www.facebook.com/profile/' + idu + '/search/?q=' + 'amigos')
                    webbrowser.open('https://www.facebook.com/profile/' + idu + '/search/?q=' + 'navidad')
                    webbrowser.open('https://www.facebook.com/profile/' + idu + '/search/?q=' + 'cumpleaños')
                    os.system("cls")
                    print(header)
                elif previo == '2':
                        print("Ingrese el ID del Perfil del Usuario ")
                        print("En caso de no tenerlo puede conseguirlo desde el menu anterior opcion 1")
                        idu= input()
                        webbrowser.open('https://www.facebook.com/' + idu + '/friends')
                        os.system("cls")
                        print("***********************************************")
                        print("")
                        print("SEGUNDO METODO DE BUSQUEDA MANUAL DE RELACIONES")
                        print("")
                        print("***********************************************")
                        print("")
                        print("A Continuacion se abrira una nueva ventana en explorador")
                        print("Presiones CTRL+U o ingrese view-source delante de la pagina para ver el Codigo Fuente ")
                        print("Presione la tecla CTRL+F y busque fbid= , cada resultador correspondera al ID de un perfil")
                        print("correspondiente a amigos de dicho usuario")
                        print("")
                        print("")
                        input("Presione ENTER para Continuar")
                        webbrowser.open('https://www.facebook.com/profile.php?id='+ idu +'&sk=photos_of')
                        os.system("cls")
                        print("")
                        print("**************************************************************")
                        print("")
                        print("Ahora se procedera utilizar filtros por default para maximizar los resultados")
                        print("")
                        print("")
                        input("Presione ENTER para Continuar")
                        webbrowser.open('https://www.facebook.com/profile/' + idu + '/search/?q=' + 'amigos')
                        webbrowser.open('https://www.facebook.com/profile/' + idu + '/search/?q=' + 'navidad')
                        webbrowser.open('https://www.facebook.com/profile/' + idu + '/search/?q=' + 'cumpleaños')
                        os.system("cls")
                        print(header)
                else:
                    print("Debe seleccionar 1 o 2") 
                        
        else:
            print("Ingrese el ID del Perfil del Usuario ")
            print("En caso de no tenerlo puede conseguirlo desde el menu anterior opcion 1")
            idu=input()
            webbrowser.open('https://www.facebook.com/' + idu + '/friends')
            os.system("cls")
            print("***********************************************")
            print("")
            print("SEGUNDO METODO DE BUSQUEDA MANUAL DE RELACIONES")
            print("")
            print("***********************************************")
            print("")
            print("A Continuacion se abrira una nueva ventana en explorador")
            print("Presiones CTRL+U o ingrese view-source delante de la pagina para ver el Codigo Fuente ")
            print("Presione la tecla CTRL+F y busque fbid= , cada resultador correspondera al ID de un perfil")
            print("correspondiente a amigos de dicho usuario")
            print("")
            print("")
            input("Presione ENTER para Continuar")
            webbrowser.open('https://www.facebook.com/profile.php?id='+ idu +'&sk=photos_of')
            os.system("cls")
            print("")
            print("**************************************************************")
            print("")
            print("Ahora se procedera utilizar filtros por default para maximizar los resultados")
            print("")
            print("")
            input("Presione ENTER para Continuar")
            webbrowser.open('https://www.facebook.com/profile/' + idu + '/search/?q=' + 'amigos')
            webbrowser.open('https://www.facebook.com/profile/' + idu + '/search/?q=' + 'navidad')
            webbrowser.open('https://www.facebook.com/profile/' + idu + '/search/?q=' + 'cumpleaños')
            os.system("cls")
            print(header)
        
    
    
    elif opcion == 4:    
        os.system("cls")
        print(header)
        print("")
        print("Este Modulo te ayudara a Encontrar los Likes de un Perfil")
        print("Ademas de los Likes Simples tambien podras obtener por medio de otros filtros")
        print("Los diferentes Gustos y Hobbies del usuario")
        print("*******************************************************************")
        print("")
        print("Recuerda tener la sesion iniciada de Facebook en tu navegador por defecto")
        if not idu == 0:
                print("Desea Utilizar el Perfil consultado previamente? (1- SI | 2- NO)")
                previo = input()
                if previo == '1':
                    webbrowser.open('https://www.facebook.com/' + usuario + '/likes_all')
                    webbrowser.open('https://www.facebook.com/profile/' + idu + '/search/?q=' + 'gusta')
                    webbrowser.open('https://www.facebook.com/profile/' + idu + '/search/?q=' + 'hobbie')
                    webbrowser.open('https://www.facebook.com/profile/' + idu + '/search/?q=' + 'deporte')
                    webbrowser.open('https://www.facebook.com/profile/' + idu + '/search/?q=' + 'politica')
                    webbrowser.open('https://www.facebook.com/profile/' + idu + '/search/?q=' + 'religion')
                    os.system("cls")
                    print(header)
                elif previo == '2':
                        print("Ingrese el ID del Perfil del Usuario ")
                        print("En caso de no tenerlo puede conseguirlo desde el menu anterior opcion 1")
                        idu= input()
                        print("Ingrese la URL del Perfil del usuario")
                        usuario=input()
                        webbrowser.open('https://www.facebook.com/' + idu + '/likes_all')
                        webbrowser.open('https://www.facebook.com/profile/' + idu + '/search/?q=' + 'gusta')
                        webbrowser.open('https://www.facebook.com/profile/' + idu + '/search/?q=' + 'hobbie')
                        webbrowser.open('https://www.facebook.com/profile/' + idu + '/search/?q=' + 'deporte')
                        webbrowser.open('https://www.facebook.com/profile/' + idu + '/search/?q=' + 'politica')
                        webbrowser.open('https://www.facebook.com/profile/' + idu + '/search/?q=' + 'religion')
                        os.system("cls")
                        print(header)
                else:
                    print("Debe seleccionar 1 o 2") 
                        
        else:
            print("Ingrese el ID del Perfil del Usuario ")
            print("En caso de no tenerlo puede conseguirlo desde el menu anterior opcion 1")
            idu=input()
            print("Ingrese la URL del Perfil del usuario")
            usuario=input()
            webbrowser.open('https://www.facebook.com/' + idu + '/likes_all')
            webbrowser.open('https://www.facebook.com/profile/' + idu + '/search/?q=' + 'gusta')
            webbrowser.open('https://www.facebook.com/profile/' + idu + '/search/?q=' + 'hobbie')
            webbrowser.open('https://www.facebook.com/profile/' + idu + '/search/?q=' + 'deporte')
            webbrowser.open('https://www.facebook.com/profile/' + idu + '/search/?q=' + 'politica')
            webbrowser.open('https://www.facebook.com/profile/' + idu + '/search/?q=' + 'religion')
            os.system("cls")
            print(header)




    elif opcion == 5:    
        os.system("cls")
        print(header)
        print("")
        print("Este Modulo te ayudara a Encontrar Amigos en Comun")
        print("Entre dos Perfiles Solicitados")
        print("*******************************************************************")
        print("")
        print("Recuerda tener la sesion iniciada de Facebook en tu navegador por defecto")
        if not idu == 0:
                print("Desea Utilizar el Perfil consultado previamente? (1- SI | 2- NO)")
                previo = input()
                if previo == '1':
                    print("")
                    print("Ingrese el ID del Perfil a Comparar")
                    compara = input()
                    webbrowser.open('https://facebook.com/browse/mutual_friends/?uid='+ idu +'&node='+ compara)
                    os.system("cls")
                    print(header)
                elif previo == '2':
                        print("Ingrese el ID del Perfil del Usuario ")
                        print("En caso de no tenerlo puede conseguirlo desde el menu anterior opcion 1")
                        idu= input()
                        print("")
                        print("Ingrese el ID del Perfil a Comparar")
                        compara = input()
                        webbrowser.open('https://facebook.com/browse/mutual_friends/?uid='+ idu +'&node='+ compara)
                        os.system("cls")
                        print(header)
                else:
                    print("Debe seleccionar 1 o 2") 
                        
        else:
            print("Ingrese el ID del Perfil del Usuario ")
            print("En caso de no tenerlo puede conseguirlo desde el menu anterior opcion 1")
            idu=input()
            print("")
            print("Ingrese el ID del Perfil a Comparar")
            compara = input()
            webbrowser.open('https://facebook.com/browse/mutual_friends/?uid='+ idu +'&node='+ compara)
            os.system("cls")
            print(header)


    
    elif opcion == 6:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 6")

os.system("cls") 
print(header)
print("")
print("******************************************")
print("")
print ("Gracias por Haber Utilizado 'Cara De Libro Investigador'")
print("")
print("*******************")    
print("**************")    
print("********")    






