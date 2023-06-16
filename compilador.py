import ply.lex as lex
import ply.yacc as yacc

# Lista de tokens reconocidos por el lexer
tokens = (
    'COMMAND',
    'OPTION',
    'STRING',
    'SPACE'
)

# Reglas de expresiones regulares para cada token
t_COMMAND = r'mundial'
t_OPTION = r'-[a-z]'
t_STRING = r'\".*?\"'
t_SPACE = r'\s'

# Ignorar espacios en blanco y tabulaciones
t_ignore = ''

# Manejo de errores de tokens no reconocidos
def t_error(t):
    print("Error de sintaxis")
    t.lexer.skip(1)
    exit(0)

# Construcción del lexer
lexer = lex.lex()

# Definición de la gramática y las reglas de precedencia
precedence = ()

# Regla para el comando completo
def p_command(p):
    'command : COMMAND SPACE OPTION SPACE STRING'
    global command, option, string
    command = p[1]
    option = p[3]
    string = p[5][1:-1]  # Remover las comillas del string
    # print(f"Comando: {command}\nOption: {option}\nString: {string}")

    if len(p) > 6:
        print("Error: Caracteres no permitidos después del string")
        return
    
def p_command_error(p):
    'command : COMMAND SPACE OPTION SPACE STRING SPACE'
    print("Error: Caracteres no permitidos después del argumento")
    exit (0)
# Manejo de errores de sintaxis
def p_error(p):
    print("Error de sintaxis")
    exit (0)

# Construcción del parser
parser = yacc.yacc()

# Prueba del intérprete

# input_string = 'mundial -a "ejemplo"'
# print(lexer.input(input_string))
# print(parser.parse(input_string))

def revisar_comando (input_string):
    lexer.input(input_string)
    parser.parse(input_string)
    if lexer.input(input_string) == None and parser.parse(input_string) == None:
        return True, command, option, string
    else:
        return False, None, None, None
    
