import ply.lex as lex
import ply.yacc as yacc

reserved = {
    'mundial': 'MUNDIAL',
    '-j': 'LISTAR_PARTIDOS',
    '-h': 'LISTAR_GOLES',
    '-f': 'ESTADISTICAS_MUNDIAL',
    '-p': 'JUGADORES_PAIS',
    '-t': 'CANTIDAD_VICTORIAS',
    '-g': 'TOTAL_GOLES',
    '-c': 'CAMPEON_MUNDIAL',
    '-m': 'PROMEDIO_GOLES',
    '-e': 'GOLES_CONTRA'
}

tokens = [
    'ID',
    'STRING'
] + list(reserved.values())

t_STRING = r'\".*?\"'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

t_ignore = ' \t'

def t_error(t):
    print("Carácter inválido: %s" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

variables = {}

def p_mundial(t):
    '''mundial : MUNDIAL opcion'''
    print(t[2])

def p_opcion(t):
    '''opcion : LISTAR_PARTIDOS STRING
              | LISTAR_GOLES STRING
              | ESTADISTICAS_MUNDIAL STRING
              | JUGADORES_PAIS STRING
              | CANTIDAD_VICTORIAS STRING
              | TOTAL_GOLES STRING
              | CAMPEON_MUNDIAL STRING
              | PROMEDIO_GOLES STRING
              | GOLES_CONTRA STRING'''
    t[0] = t[1] + ' ' + t[2]

def p_error(t):
    print("Error de sintaxis en la entrada: %s" % t.value)

parser = yacc.yacc()

while True:
    try:
        data = input()
    except EOFError:
        break
    parser.parse(data)
