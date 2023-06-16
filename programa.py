from datetime import datetime
import re

class Partido:
    def __init__(self, fecha, equipo_local, goles_local, equipo_visitante, goles_visitante, goles, etapa):
        self.fecha = fecha
        self.equipo_local = equipo_local
        self.goles_local = goles_local
        self.equipo_visitante = equipo_visitante
        self.goles_visitante = goles_visitante
        self.goles = goles
        self.etapa = etapa
    def __str__(self):
        return f"Partido({self.fecha}, {self.equipo_local}, {self.goles_local}, {self.equipo_visitante}, {self.goles_visitante}, {self.goles}, {self.etapa})"

def sacar_goles(string):
    pattern = r'([\w\s]+)\s*\((\d+)\)'
    match = re.match(pattern, string)
    if match:
        name = match.group(1).strip()
        number = int(match.group(2))
        return name, number
    else:
        return None
    
def sacar_nombre_autogol(string):
    pattern = r'([\w\s]+)'
    match = re.match(pattern, string)
    if match:
        name = match.group(1).strip()
        return name
    else:
        return None
     
def sacar_nombre_penal(string):
    pattern = r'([\w\s]+)'
    match = re.match(pattern, string)
    if match:
        name = match.group(1).strip()
        return name
    else:
        return None 

def has_number(string):
    pattern = r'\d+'
    match = re.search(pattern, string)
    return bool(match)   
       
       
#### query: mundial -c "año_mundial" (muestra el campeón del mundial de ese año)* ####

def query_c (partidos, ano_mundial):
    for partido in partidos:
        if partido.fecha.year == int(ano_mundial) and partido.etapa == 'F':
            if partido.goles_visitante > partido.goles_local:
                print(f"El campeon del mundial del {ano_mundial} es {partido.equipo_visitante}")
                return
            else:
                print(f"El campeon del mundial del {ano_mundial} es {partido.equipo_local}")
                return
            
#### query: mundial -g "año_mundial" (muestra la cantidad total de goles anotados en ese mundial)* ####

def query_g (partidos,ano_mundial):
    total_goles_anotados = 0
    for partido in partidos:
        if partido.fecha.year == int(ano_mundial):
            total_goles_anotados += partido.goles_local
            total_goles_anotados += partido.goles_visitante
    
    print(f"En el mundial del ano {ano_mundial} se anotaron {total_goles_anotados} goles")
    return
            
#### query: mundial -t "pais" (muestra la cantidad de veces que el pais ha ganado la Copa del Mundo)* ####

def query_t(partidos,pais):
    cantidad_de_veces = 0
    pais = pais.lower()
    for partido in partidos:
        if partido.etapa == 'F':
            if (partido.goles_local > partido.goles_visitante) and (partido.equipo_local.lower() == pais):
                cantidad_de_veces+=1
            if (partido.goles_local <= partido.goles_visitante) and (partido.equipo_visitante.lower() == pais):
                cantidad_de_veces +=1
    
    if cantidad_de_veces == 1:
        print(f"{pais} ha ganado la copa del mundo {cantidad_de_veces} vez")
    else:
        print(f"{pais} ha ganado la copa del mundo {cantidad_de_veces} veces")
    return   

### mundial -m "pais" (muestra el promedio de goles del pais en los mundiales en los que ha participado)* ###
def query_m(partidos):
    dict_paises_goles = {}
    for partido in partidos:
        if partido.equipo_local.lower() in dict_paises_goles:
            dict_paises_goles[partido.equipo_local.lower()].append(partido.goles_local)
        else:
            dict_paises_goles[partido.equipo_local.lower()] = [partido.goles_local]
            
        if partido.equipo_visitante.lower() in dict_paises_goles:
            dict_paises_goles[partido.equipo_visitante.lower()].append(partido.goles_visitante)
        else:
            dict_paises_goles[partido.equipo_visitante.lower()] = [partido.goles_visitante]
    for pais in dict_paises_goles:
        dict_paises_goles[pais] = sum(dict_paises_goles[pais])/len(dict_paises_goles[pais])
    for pais in dict_paises_goles:
        print(f"El promedio de goles de {pais} es {round(dict_paises_goles[pais],2)}")
       
### mundial -h “jugador” (lista los goles del jugador en mundiales)* """
def query_h(jugador,partidos):
    goles = 0
    for partido in partidos:
        try:
            if jugador in partido.goles:
                goles += partido.goles[jugador]
        except:
            pass
    print(f"El jugador {jugador} ha anotado {goles} goles en mundiales")
    
### mundial -p "jugador" (muestra el mundial donde mas goles ha metido el jugador) * ###
def query_p(jugador,partidos):
    dict_mundiales_goles = {}
    for partido in partidos:
        try:
            if jugador in partido.goles:
                if partido.fecha.year in dict_mundiales_goles:
                    dict_mundiales_goles[partido.fecha.year] += partido.goles[jugador]
                else:
                    dict_mundiales_goles[partido.fecha.year] = partido.goles[jugador]
        except:
            pass
    print(f"El mundial donde mas goles ha metido {jugador} es {max(dict_mundiales_goles, key=dict_mundiales_goles.get)}")

### listo mundial -j "año_mundial" (muestra el goleador del mundial de ese año)* ###
def query_j(partidos,ano_mundial):
    dic_jugador_goles = {}
    for partido in partidos:
        if partido.fecha.year == int(ano_mundial):
            for jugador in partido.goles:
                if jugador in dic_jugador_goles:
                    dic_jugador_goles[jugador] += partido.goles[jugador]
                else:
                    dic_jugador_goles[jugador] = partido.goles[jugador]
    print(f"El goleador del mundial del {ano_mundial} es {max(dic_jugador_goles, key=dic_jugador_goles.get)}")

## MAIN ##       
       
       
file = open('data_automatas.csv','r', encoding="utf8")
next(file)
partidos = []
for row in file:
    linea_parseada = row.split(',')
    Fecha = datetime.strptime(linea_parseada[0], '%d/%m/%Y') 
    EquipoLocal = linea_parseada[1]
    GolesLocal =int(linea_parseada[2])
    EquipoVisitante = linea_parseada[3]
    GolesVisitante = int(linea_parseada[4])
    Goles = {}
    sublistadegoles = linea_parseada[5:-1]
    for autor_del_gol in sublistadegoles:
        if 'autogol' in autor_del_gol:
            jugador = sacar_nombre_autogol(autor_del_gol)
            
            if jugador in Goles:
                Goles[jugador] +=1
            else:
                Goles[jugador] = 1
                
        elif 'penal' in autor_del_gol:
            jugador= sacar_nombre_penal(autor_del_gol)
            
            if jugador in Goles:
                Goles[jugador] +=1
            else:
                Goles[jugador] = 1
            
        elif has_number(autor_del_gol):
            jugador, gol = sacar_goles(autor_del_gol)
            
            if jugador in Goles:
                Goles[jugador] += gol
            else:
                Goles[jugador] = gol
            
        else:
            jugador = autor_del_gol
            
            if jugador in Goles:
                Goles[jugador] +=1
            else:
                Goles[jugador] = 1
    
    etapa = linea_parseada[-1].strip()
    
    partido_actual = Partido(
        Fecha,
        EquipoLocal,
        GolesLocal,
        EquipoVisitante,
        GolesVisitante,
        Goles,
        etapa
    )
    
    partidos.append(partido_actual)
    
    
   
query_c(partidos,2018)
query_g(partidos,2018)
query_t(partidos,"alemania")
query_m(partidos)
query_h("Ronaldo",partidos)
query_p("Neymar",partidos)
query_j(partidos,2014)
            
            

file.close()