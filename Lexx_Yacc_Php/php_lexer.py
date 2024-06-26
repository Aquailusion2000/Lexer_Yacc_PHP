import sys
import ply.lex as lex

# TOKENS
tokens = (

    # TAG de apertura y cerradura
    'OPENTAG','CLOSETAG',

    # Lista de palabras reservadas
    '__HALT_COMPILER','ABSTRACT','AND','ARRAY','AS','BREAK','CALLABLE','CASE',
    'CATCH','CLASS','CLONE','CONST','CONTINUE','DECLARE','DEFAULT','DIE','DO',
    'ECHO','ELSE','ELSEIF','EMPTY','ENDDECLARE','ENDFOR','ENDFOREACH','ENDIF',
    'ENDSWITCH','ENDWHILE','EVAL','EXIT','EXTENDS','CLOSETAGAL','FOR','FOREACH',
    'FUNCTION','GLOBAL','GOTO','IF','IMPLEMENTS','INCLUDE','INCLUDE_ONCE',
    'INSTANCEOF','INSTEADOF','INTERFACE','ISSET','LIST','NAMESPACE','NEW','OR',
    'PRINT','PRIVATE','PROTECTED','PUBLIC','REQUIRE','REQUIRE_ONCE','RETURN',
    'STATIC','SWITCH','THROW','TRAIT','TRY','UNSET','USE','VAR','WHILE','XOR',

    #boolean
    'TRUE','FALSE',

    # Simbolos
    'PLUS','PLUSPLUS','PLUSEQUAL','MINUS','MINUSMINUS','MINUSEQUAL','TIMES',
    'TIMESTIMES','DIVIDE','LESS','LESSEQUAL','GREATER','GREATEREQUAL','EQUAL',
    'DEQUAL','DISTINT','ISEQUAL','SEMI','COMMA','LPAREN','RPAREN','LBRACKET',
    'RBRACKET','LBLOCK','RBLOCK','COLON','AMPERSANT','HASHTAG','DOT','QUOTES',
    'APOSTROPHE','DOT_DOT',

    # Otros
    'COMMENTS','COMMENTS_C99','ID','IDVAR','NUM','STRING','VOID',
)


# Tokens Expresiones Regulares

# Caracteres ignorados
t_ignore = " \t"

def t_VOID(t):
    r'VOID|void'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print ("ERROR: Caracter ilegal")
    print ("\t\tLine: "+str(t.lexer.lineno)+"\t=> " + t.value[0])
    t.lexer.skip(1)


# Expresion regular de tag de apertura y cerradura
def t_OPENTAG(t):
    r'(<\?(php)?)'
    return t

def t_CLOSETAG(t):
    r'\?>'
    return t


# Lista de expresiones regulares de palabras reservadas
def t___HALT_COMPILER(t):
    r'__halt_compiler'
    return t

def t_ABSTRACT(t):
    r'abstract'
    return t

def t_AND(t):
    r'and|AND|\&\&'
    return t

def t_ARRAY(t):
    r'array'
    return t

def t_AS(t):
    r'as'
    return t

def t_BREAK(t):
    r'break'
    return t


def t_CASE(t):
    r'case'
    return t

def t_CATCH(t):
    r'catch'
    return t

def t_CLASS(t):
    r'class'
    return t

def t_CLONE(t):
    r'clone'
    return t

def t_CONST(t):
    r'const'
    return t

def t_CONTINUE(t):
    r'continue'
    return t

def t_DECLARE(t):
    r'declare'
    return t

def t_DEFAULT(t):
    r'default'
    return t

def t_DO(t):
    r'do'
    return t

def t_ECHO(t):
    r'echo'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_ELSEIF(t):
    r'elseif'
    return t

def t_EMPTY(t):
    r'empty'
    return t

def t_ENDFOR(t):
    r'endfor'
    return t

def t_ENDFOREACH(t):
    r'endforeach'
    return t

def t_ENDIF(t):
    r'endif'
    return t

def t_ENDSWITCH(t):
    r'endswitch'
    return t

def t_ENDWHILE(t):
    r'endwhile'
    return t

def t_EVAL(t):
    r'eval'
    return t

def t_EXIT(t):
    r'exit'
    return t

def t_EXTENDS(t):
    r'extends'
    return t

def t_CLOSETAGAL(t):
    r'CLOSETAGal'
    return t

def t_FOREACH(t):
    r'foreach'
    return t

def t_FOR(t):
    r'for'
    return t

def t_FUNCTION(t):
    r'function'
    return t

def t_GLOBAL(t):
    r'global'
    return t

def t_GOTO(t):
    r'goto'
    return t

def t_IF(t):
    r'if'
    return t

def t_IMPLEMENTS(t):
    r'implements'
    return t

def t_INCLUDE(t):
    r'include'
    return t

def t_INSTANCEOF(t):
    r'instanceof'
    return t

def t_INSTEADOF(t):
    r'insteadof'
    return t

def t_INTERFACE(t):
    r'interface'
    return t

def t_ISSET(t):
    r'isset'
    return t

def t_LIST(t):
    r'list'
    return t

def t_NAMESPACE(t):
    r'namespace'
    return t

def t_NEW(t):
    r'new'
    return t

def t_OR(t):
    r'or|\|\||OR'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_PRIVATE(t):
    r'private'
    return t

def t_PROTECTED(t):
    r'protected'
    return t

def t_PUBLIC(t):
    r'public'
    return t

def t_REQUIRE(t):
    r'require'
    return t

def t_REQUIRE_ONCE(t):
    r'require_once'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_STATIC(t):
    r'static'
    return t

def t_SWITCH(t):
    r'switch'
    return t

def t_THROW(t):
    r'throw'
    return t

def t_TRAIT(t):
    r'trait'
    return t

def t_TRY(t):
    r'try'
    return t

def t_UNSET(t):
    r'unset'
    return t

def t_USE(t):
    r'use'
    return t

def t_VAR(t):
    r'var'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_XOR(t):
    r'xor'
    return t

def t_TRUE(t):
    r'true'
    return t

def t_FALSE(t):
    r'false'
    return t

# RE SYMBOLS
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_EQUAL     = r'='
t_DISTINT   = r'!'
t_LESS      = r'<'
t_GREATER   = r'>'
t_SEMI      = r';'
t_COMMA     = r','
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACKET  = r'\['
t_RBRACKET  = r'\]'
t_LBLOCK    = r'{'
t_RBLOCK    = r'}'
t_COLON     = r':'
t_AMPERSANT = r'\&'
t_HASHTAG   = r'\#'
t_DOT       = r'\.'
t_QUOTES    = r'\"'
t_APOSTROPHE = r'\''

def t_LESSEQUAL(t):
    r'<='
    return t

def t_GREATEREQUAL(t):
    r'>='
    return t

def t_DEQUAL(t):
    r'!='
    return t

def t_ISEQUAL(t):
    r'=='
    return t

def t_MINUSMINUS(t):
    r'--'
    return t

def t_PLUSPLUS(t):
    r'\+\+'
    return t

def t_TIMESTIMES(t):
    r'\*\*'
    return t

def t_DOT_DOT(t):
    r'::'
    return t


# Expresiones regulares para Otros


def t_COMMENTS(t):
    r'\/\*([^*]|\*[^\/])*(\*)+\/'
    t.lexer.lineno += t.value.count('\n')

def t_COMMENTS_C99(t):
    r'(\/\/|\#)(.)*?\n'
    t.lexer.lineno += 1

def t_IDVAR(t):
    r'\$\w+(\d\w)*'
    return t

def t_NUM(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_ID(t):
    r'\w+(\w\d)*'
    return t

def t_STRING(t):
    r'(("[^"]*")|(\'[^\']*\'))'
    return t


lexer = lex.lex()


if __name__ == '__main__':
    if (len(sys.argv) > 1):
        script = sys.argv[1]

        scriptfile = open(script, 'r')
        scriptdata = scriptfile.read()
        #print (scriptdata)
        lexer.input(scriptdata)

        print ("INICIA ANALISIS LEXICO")
        i = 1
        while True:
            tok = lexer.token()
            if not tok:
                break
            print (str(i)+" - "+"Line: "+str(tok.lineno)+"\t"+str(tok.type)+"\t-->  "+str(tok.value))
            i += 1

        print (chr(27)+("TERMINA ANALISIS LEXICO"))

    else:
        print ("Pase el archivo de script PHP como parametro:")
        print ("python php_lexer.py"+" nombreDeArchivo.php ")
