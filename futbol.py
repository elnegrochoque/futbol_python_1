import csv


def opcion1(data):
    pais_buscado = input("Ingrese el pais que desea buscar \n(primera letra con mayuscula y nombre en ingles)")
    victorias = 0
    cantidad_filas = len(data)
    for i in range(cantidad_filas):
        row = data[i]
        try:
            if pais_buscado == (row.get("home_team")):
                if ((row.get("home_score")) > (row.get("away_score"))):
                    victorias += 1
            if pais_buscado == (row.get("away_team")):
                if ((row.get("home_score")) < (row.get("away_score"))):
                    victorias += 1
        except:
            print('problema con la busqueda')
    print("Pais:",pais_buscado," tuvo ", victorias," victorias")

def opcion2(data):
    pais_buscado = input("Ingrese el pais que desea buscar \n(primera letra con mayuscula y nombre en ingles)")
    perdidos = 0
    cantidad_filas = len(data)
    for i in range(cantidad_filas):
        row = data[i]
        try:
            if pais_buscado == (row.get("home_team")):
                if ((row.get("home_score")) < (row.get("away_score"))):
                    perdidos += 1
            if pais_buscado == (row.get("away_team")):
                if ((row.get("home_score")) > (row.get("away_score"))):
                    perdidos += 1
        except:
            print('problema con la busqueda')
    print("Pais:",pais_buscado," tuvo ", perdidos," partidos perdidos")

def opcion3(data):
    pais_buscado = input("Ingrese el pais que desea buscar \n(primera letra con mayuscula y nombre en ingles)")
    npartidos = int(input("Ingrese cantidad de partidos"))
    ganados=0
    perdidos=0
    empatados=0
    cantidad_filas = len(data)
    for i in range(cantidad_filas-1,0,-1):
        row = data[i]
        if npartidos==0:
            break
        try:
            if pais_buscado == (row.get("home_team")):
                npartidos-=1
                if ((row.get("home_score")) > (row.get("away_score"))):
                    ganados += 1
                if ((row.get("home_score")) < (row.get("away_score"))):
                    perdidos += 1
                if ((row.get("home_score")) == (row.get("away_score"))):
                    empatados += 1
            if pais_buscado == (row.get("away_team")):
                npartidos-=1
                if ((row.get("home_score")) < (row.get("away_score"))):
                    ganados += 1
                if ((row.get("home_score")) > (row.get("away_score"))):
                    perdidos += 1
                if ((row.get("home_score")) == (row.get("away_score"))):
                    empatados += 1
        except:
            print('problema con la busqueda')
    print(pais_buscado, "tuvo:", ganados,"partidos ganados",empatados,"partidos empatados y",perdidos,"partidos perdidos" )

def opcion4(data):
    pais_buscado = input("Ingrese el pais que desea buscar \n(primera letra con mayuscula y nombre en ingles)")
    nvisitante=1
    nlocal=1
    cantidad_filas = len(data)
    for i in range(cantidad_filas-1,0,-1):
        row = data[i]
        if (nvisitante==0 and nlocal==0):
            break
        try:
            if (pais_buscado == (row.get("home_team"))) and nlocal==1:
                nlocal-=1
                print(pais_buscado,"jugo contra", (row.get("away_team")), "de local el", (row.get("date")))
            if (pais_buscado == (row.get("away_team"))) and nvisitante==1:
                nvisitante-=1
                print(pais_buscado,"jugo contra", (row.get("home_team")), "de visitante el", (row.get("date")))
        except:
            print('problema con la busqueda')

def opcion5(data):
    pais_buscado1 = input("Ingrese el primer pais que desea buscar \n(primera letra con mayuscula y nombre en ingles)")
    pais_buscado2 = input("Ingrese el segundo pais que desea buscar \n(primera letra con mayuscula y nombre en ingles)")
    ganados=0
    perdidos=0
    empatados=0
    cantidad_filas = len(data)
    for i in range(cantidad_filas-1,0,-1):
        row = data[i]
        try:
            if (pais_buscado1 == (row.get("home_team"))) and (pais_buscado2 == (row.get("away_team"))):
                if ((row.get("home_score")) > (row.get("away_score"))):
                    ganados += 1
                if ((row.get("home_score")) < (row.get("away_score"))):
                    perdidos += 1
                if ((row.get("home_score")) == (row.get("away_score"))):
                    empatados += 1
            if (pais_buscado1 == (row.get("away_team"))) and (pais_buscado2 == (row.get("home_team"))):
                
                if ((row.get("home_score")) < (row.get("away_score"))):
                    ganados += 1
                if ((row.get("home_score")) > (row.get("away_score"))):
                    perdidos += 1
                if ((row.get("home_score")) == (row.get("away_score"))):
                    empatados += 1
        except:
            print("error al obtener los datos")
    print('Historicamente', pais_buscado1,"gano",ganados,"empato",empatados,"y perdio",perdidos, "contra", pais_buscado2)

if __name__ == '__main__':
    print("Usted quiere:")
    print("1- Determinar cuántas veces ganó un país de local o de visitante.")
    print("2- Determinar cuántas veces perdió un país de local o de visitante.")
    print("3- Determinar cómo le fue al país en los últimos “N” partidos jugados (ejemplo, resultados de los últimos 10 partidos, ¿ganó la mayoría?")
    print("4- Contra quien jugó el último partido de local o de visitante.")
    print("5- Como le fue al país históricamente jugando contra otro país indicado.")
    print("6- Salir del programa")
    bandera=True
    while bandera:
        opcion=input("Ingrese la opcion deseada")
        with open('partidos.csv', encoding="utf8") as csvfile:
            data=list(csv.DictReader(csvfile))
        if opcion == "1":   
            opcion1(data)
            print("Fin del Programa")
            break
        elif opcion == "2":
            opcion2(data)
            print("Fin del Programa")
            break
        elif opcion == "3":
            opcion3(data)
            print("Fin del Programa")
            break
        elif opcion == "4":
            opcion4(data)
            print("Fin del Programa")
            break
        elif opcion == "5":
            opcion5(data)
            print("Fin del Programa")
            break
        elif opcion == "6":
            print("Fin del Programa")
            break
        else:
            print("No se reconoce la opcion elegida")
