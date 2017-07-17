#!/usr/bin/python

from alexico import *

position = 0
listadeTokens = []
lex

def init():
    
    global listadeTokens
    #listadeTokens = getTokenList('teste1.bob')
    #listadeTokens = getTokenList('teste2.bob')
    #listadeTokens = getTokenList('teste3.bob')
    #listadeTokens = getTokenList('teste4.bob')
    listadeTokens = getTokenList('teste5.bob')


def consome():
    global lex
    global position
    token = listadeTokens[position]
    position = position + 1
    return token.get_token()

def verifyToken(token):
    global lex
    if (lex == token):
        lex = consome()
        print '------------->',lex
    else:
        print 'error!!! Linha: '+ str(listadeTokens[position].get_linha()) + ". " + token + ' era esperado,  mas ' + lex + ' encontrado'
        quit()


def goal():
    print '[goal]'
    global lex
    lex = consome()
    print lex
    print 'call definitions_list > goal'
    definitions_list()
    

def definitions_list():
    print '[definitions_list]'
    global lex
    print 'call defi > definitions_list'
    defi()
    print 'call R_definitions_list > definitions_list'
    R_definitions_list()

def defi(): #first = class, ident
    print '[defi]'
    global lex

    if(lex == 'CLASS'):
        print 'call class_def > defi'
        class_def()

    elif((lex == 'IDENT') or (lex == 'IDFUNC')):
        print 'call function_def > defi'
        function_def()

def R_definitions_list():
    print '[R_definitions_list]'
    global lex

    if(lex == 'CLASS') or (lex == 'IDENT') or (lex == 'IDFUNC'):
        print 'call definitions_list > R_definitions_list'
        definitions_list()
    else:
        pass


def class_def():
    print '[class_def]'
    global lex

    verifyToken('CLASS')
    verifyToken('IDENT')

    print 'call class_base > class_def'
    class_base()

    verifyToken('ABRECHAVE')

    print 'call member_def_list > class_def'
    member_def_list()

    verifyToken('FECHACHAVE')

def class_base():
    print '[class_base]'
    global lex

    if (lex == 'DOISPTO'):
        verifyToken('DOISPTO')
        verifyToken('IDENT')
    else:
        pass

def member_def_list(): # member-def-list -> member-def R-member-def-list
    print '[member_def_list]'
    global lex

    print 'call member_def > member_def_list'
    member_def()
    print 'call r_member_def_list > member_def_list'
    R_member_def_list()

def R_member_def_list(): # R-member-def-list -> member-def-list | LAMBDA 
    print '[r_member_def_list]'             
    global lex

    if ((lex == 'STATIC') or (lex == 'IDFUNC') or (lex == 'IDENT')):
        print 'call member_def_list > r_member_def_lis'
        member_def_list()

    else:
        pass

def member_def(): #member-def -> op-static R-member-defs
    print '[member_def]'
    global lex

    print 'call op_static > member_def'
    op_static()

    print 'call R_member_def > member_def'
    R_member_def()


def R_member_def(): # R-member-def -> var-name-list ; | IDFUNC ( op-formal-arg-list ) ;
    print '[R_member_def]'
    global lex

    if (lex == 'IDENT'):
        print 'call var_name_list > R_member_def'
        var_name_list()
        verifyToken('PTOVIR')

    elif (lex == 'IDFUNC'):
        verifyToken('IDFUNC')
        verifyToken('ABREPAR')

        print 'call op_formal_arg_list > R_member_def'
        op_formal_arg_list()

        verifyToken('FECHAPAR')
        verifyToken('PTOVIR')    


def op_static():
    print '[op_static]'
    global lex

    if(lex == 'STATIC'):
        verifyToken('STATIC')

    else:
        pass
    
def var_name_list(): # var-name-list -> IDENT op-vector R-var-name-list
    print '[var_name_list]'
    global lex

    verifyToken('IDENT')

    print 'call op_vector > var_name_list'
    op_vector()

    print 'call R_var_name_list > var_name_list'
    R_var_name_list()
    
def R_var_name_list():
    print '[R_var_name_list]'
    global lex

    if (lex == 'VIRG'):
        verifyToken('VIRG')
        print 'call var_name_list > R_var_name_list'
        var_name_list()
    else:
        pass
    
def op_formal_arg_list():
    print '[op_formal_arg_list]'
    global lex

    if (lex == 'IDENT'):
        print 'call formal_arg_list > op_formal_arg_list'
        formal_arg_list()
    else:
        pass
    
def formal_arg_list():
    print '[formal_arg_list]'
    global lex

    verifyToken('IDENT')
    print 'call R_formal_arg_list > formal_arg_list'
    R_formal_arg_list()
    
def R_formal_arg_list():
    print '[R_formal_arg_list]'
    global lex

    if (lex == 'VIRG'):
        verifyToken('VIRG')
        print 'call formal_arg_list > R_formal_arg_list'
        formal_arg_list()
    else:
        pass
    
def function_def():
    print '[function_def]'
    global lex

    print 'call op_class_owner > function_def'
    op_class_owner()
    verifyToken('IDFUNC')
    verifyToken('ABREPAR')
    print 'call op_parameters > function_def'
    op_parameters()
    verifyToken('FECHAPAR')
    verifyToken('ABRECHAVE')
    print 'call statement_list > function_def'
    statement_list()
    verifyToken('FECHACHAVE')
    
def op_class_owner():
    print '[op_class_owner]'
    global lex

    if(lex == 'IDENT'):
        verifyToken('IDENT')
        verifyToken('DOISPTO2')
    else:
        pass
    
def op_parameters():
    print '[op_parameters]'
    global lex

    print 'call op_formal_arg_list > op_parameters'
    op_formal_arg_list()
    print 'call op_temp_list > op_parameters'
    op_temp_list()
    
def op_temp_list():
    print '[op_temp_list]'
    global lex

    if(lex == 'PTOVIR'):
        verifyToken('PTOVIR')
        print 'call temp_list > op_temp_list'
        temp_list()
    else:
        pass
    
def temp_list():
    print '[temp_list]'
    global lex

    verifyToken('IDENT')
    print 'call R_temp_list > temp_list'
    R_temp_list()
    
def R_temp_list():
    print '[R_temp_list]'
    global lex

    if (lex == 'VIRG'):
        verifyToken('VIRG')
        print 'call temp_list > R_temp_list'
        temp_list()

    else:
        pass
    
def statement_list():
    print '[statement_list]'
    global lex

    if (lex == 'IF') or (lex == "PRINT") or (lex == 'DO') or (lex == 'WHILE') or (lex == 'ABRECHAVE') or (lex == 'FOR') or (lex == 'BREAK') or (lex == 'CONTINUE') or (lex == 'RETURN')  or (lex == 'SOMA')  or (lex == 'SUB')  or (lex == 'EXC')  or (lex == 'MAISMAIS')  or (lex == 'MENOSMENOS')  or (lex == 'IDENT')  or (lex == 'ABREPAR')  or (lex == 'NEW')  or (lex == 'INT') or (lex == 'FLOAT')  or (lex == 'STRING')  or (lex == 'NIL'):
        print 'call statement > statement_list'
        statement()
        print 'call statement_list > statement_list'
        statement_list()
    else:
        pass

def statement():
    print '[statement]'
    global lex

    if (lex == 'IF'):
        verifyToken('IF')
        verifyToken('ABREPAR')
        print 'cal exp > statement'
        exp()
        verifyToken('FECHAPAR')
        print 'call statement > statement'
        statement()
        print 'call op_else > statement'
        op_else()
    elif (lex == 'WHILE'):
        verifyToken('WHILE')
        verifyToken('ABREPAR')
        print 'cal exp > statement'
        exp()
        verifyToken('FECHAPAR')
        print 'call statement > statement'
        statement()
    elif (lex == 'DO'):
        verifyToken('DO')
        print 'call statement > statement'
        statement()
        verifyToken('WHILE')
        verifyToken('ABREPAR')
        print 'cal exp > statement'
        exp()
        verifyToken('FECHAPAR')
        verifyToken('PTOVIR')
    elif (lex == 'ABRECHAVE'):
        verifyToken('ABRECHAVE')
        print 'call statement_list > statement'
        statement_list()
        verifyToken('FECHACHAVE')
    elif (lex == 'SOMA') or (lex == 'SUB') or (lex == 'EXC') or (lex == 'MAISMAIS') or (lex == 'MENOSMENOS') or (lex == 'IDENT') or (lex == 'IDFUNC') or (lex == 'ABREPAR') or (lex == 'INT') or (lex == 'FLOAT') or (lex == 'NEW') or (lex == 'NIL') or (lex == 'STRING'):
        print 'call op_expression > statement'
        op_expression() 
        verifyToken('PTOVIR')
    elif (lex == 'FOR'):
        verifyToken('FOR')
        verifyToken('ABREPAR')
        print 'call exp > statement'
        exp()
        verifyToken('PTOVIR')
        print 'call exp > statement'
        exp()
        verifyToken('PTOVIR')
        print 'call exp > statement'
        exp()
        verifyToken('FECHAPAR')
        print 'call statement > statement'
        statement()
    elif (lex == 'BREAK'):
        verifyToken('BREAK')
        verifyToken('PTOVIR')
    elif (lex == 'CONTINUE'):
        verifyToken('CONTINUE')
        verifyToken('PTOVIR')
    elif (lex == 'RETURN'):
        verifyToken('RETURN')
        print 'call op_expression > statement'
        op_expression()
        verifyToken('PTOVIR')
    elif(lex == 'PRINT'):
        verifyToken('PRINT')
        verifyToken('ABREPAR')
        print 'call print_param_list > statement'
        print_param_list()
        verifyToken('FECHAPAR')
        verifyToken('PTOVIR')

def op_else():
    print '[op_else]'
    global lex

    if (lex == 'ELSE'):
        verifyToken('ELSE')
        print 'call statement > op_else'
        statement()
    else:
        pass
    
def op_expression():
    print '[op_expression]'
    global lex

    if(lex == 'SOMA') or (lex == 'SUB') or (lex == 'EXC') or (lex == 'MAISMAIS') or (lex == 'MENOSMENOS') or (lex == 'IDENT') or (lex == 'IDFUNC') or (lex == 'ABREPAR') or (lex == 'INT') or (lex == 'FLOAT') or (lex == 'NEW') or (lex == 'NIL') or (lex == 'STRING'):
        print 'call exp > op_expression'
        exp()
    else:
        pass

def op_arguments():
    print '[op_arguments]'
    global lex

    if(lex == 'ABREPAR') or (lex == 'NIL') or (lex == 'NEW') or (lex == 'INT') or (lex == 'FLOAT') or (lex == 'STRING') or (lex == 'IDFUNC') :
        print 'call arg_list > op_arguments'
        arg_list()
    else:
        pass

def arg_list():
    print '[arg_list]'
    global lex

    print 'call valor > arg_list'
    valor()
    print 'call R_arg_list > arg_list'
    R_arg_list()
    
def R_arg_list():
    print '[R_arg_list]'
    global lex

    if (lex == 'VIRG'):
        verifyToken('VIRG')
        print 'call arg_list > R_arg_list'
        arg_list()
    else:
        pass
    
def lvalue():
    print '[lvalue]'
    global lex

    verifyToken('IDENT')
    print 'call op_vector > lvalue'
    op_vector()
    
def exp():
    print '[exp]'
    global lex

    print 'call atrib > exp'
    atrib()

    print 'call R_exp > exp'
    R_exp()
    
def R_exp():
    print '[R_exp]'
    global lex

    if(lex == 'VIRG'):
        verifyToken('VIRG')
        print 'call atrib > R_exp'
        atrib()

        print 'call R_exp > R_exp'
        R_exp()

    else:
        pass    
    
def atrib():
    flag = False
    print '[atrib]'
    global lex
                    #Modificar

    print 'call f_or > atrib'    
    
    flag = f_or()
    print 'call R_atrib > atrib'
    R_atrib(flag)
    
def R_atrib(flag):
    aux = False
    print '[R_atrib]'
    global lex

    if (lex == 'ATRIB'):
        if (flag == False):
            print 'Erro: Atribuicao nao permitida na linha ' + str(listadeTokens[position-2].get_linha())
            print 'IDENT era esperado, mas ' + listadeTokens[position-2].get_token() + ' foi recebido.'
            quit()
        verifyToken('ATRIB')
        print 'call f_or > R_atrib'    
        aux = f_or()
        print 'call R_atrib > R_atrib'
        R_atrib(aux)
    else:
        pass

    
def f_or():
    print '[f_or]'
    global lex

    aux1 = f_and()
    aux2 = R_or()

    print 'f_and > f_or'
    print 'R_or > f_or'    
    if (aux1 and aux2):
        return True
    else:
        return False

def R_or():
    print '[R_or]'
    global lex

    if (lex == 'PIPEPIPE'):
        verifyToken('PIPEPIPE')
        print 'call f_and > R_or'
        f_and()

        print 'call R_or > R_or'   
        R_or()
        return False
    else:
        return True

    
def f_and():
    print '[f_and]'
    global lex

    aux1 = rel()
    aux2 = R_and()

    print 'call rel > f_and' 
    print 'call R_and > f_and'     
    if (aux1 and aux2):
        return True
    else:
        return False

    
    
    
def R_and():
    print '[R_and]'
    global lex

    if (lex == 'COMERCOMER'):
        verifyToken('COMERCOMER')
        print 'call rel > R_and'    
        rel()

        print 'call R_and > R_and'  
        R_and() 
        return False
    else:
        return True
    
def rel():
    print '[rel]'
    global lex

    aux1 = soma()
    aux2 = R_rel()

    print 'call soma > rel'
    print 'call R_rel > rel'
    if (aux1 and aux2):
        return True
    else:
        return False

    
    
def R_rel():
    print '[R_rel]'
    global lex

    if(lex == 'IGIG'):
        verifyToken('IGIG')
        print 'call soma > R_rel'
        soma()
        return False


    elif(lex == 'EXCIG'):
        verifyToken('EXCIG')
        print 'call soma > R_rel'
        soma()
        return False

    elif(lex == 'MENORQ'):
        verifyToken('MENORQ')
        print 'call soma > R_rel'
        soma()
        return False

    elif(lex == 'MENORIG'):
        verifyToken('MENORIG') 
        print 'call soma > R_rel'
        soma()
        return False

    elif(lex == 'MAIORQ'):
        verifyToken('MAIORQ')
        print 'call soma > R_rel'           
        soma()
        return False

    elif(lex == 'MAIORIG'):
        verifyToken('MAIORIG')
        print 'call soma > R_rel'           
        soma()
        return False
    else:
        return True    
    
def soma():
    print '[soma]'
    global lex
    aux1 = mult()
    aux2 = R_soma()

    print 'call mult > soma'

    print 'call R_soma > soma'
    if (aux1 and aux2):
        return True
    else:
        return False
    
def R_soma():
    print '[R_soma]'
    global lex

    if (lex == 'SOMA'):
        verifyToken('SOMA')
        print 'call mult'
        mult()
        print 'call R_soma'
        R_soma()
        return False
    elif(lex == 'SUB'):
        verifyToken('SUB')
        print 'call mult'
        mult()
        print 'call R_soma'
        R_soma()
        return False
    else:
        return True
    
def mult():
    print '[mult]'
    global lex
    print 'call uno'
    aux1 = uno()
    aux2 = R_mult()


    print 'call R_mult'
    if (aux1 and aux2):
        return True
    else:
        return False


    
def R_mult():
    print '[R_mult]'
    global lex

    if(lex == 'MULT'):
        verifyToken('MULT')
        print 'call uno'
        uno()

        print 'call R_mult'
        R_mult()
        return False
    elif(lex == 'DIV'):
        verifyToken('DIV')
        print 'call uno'
        uno()

        print 'call R_mult'
        R_mult()
        return False
    elif(lex == 'MOD'):
        verifyToken('MOD')
        print 'call uno'
        uno()

        print 'call R_mult'
        R_mult()
        return False
    else:
        return True

def uno():
    print '[uno]'
    global lex
    if(lex == 'SOMA'):
        verifyToken('SOMA')
        print 'call uno'
        uno()
        return False
    elif(lex == 'SUB'):
        verifyToken('SUB')
        print 'call uno'
        uno()
        return False
    elif(lex == 'EXC'):
        verifyToken('EXC')
        print 'call uno'
        uno()
        return False
    elif(lex == 'MAISMAIS'):
        verifyToken('MAISMAIS')
        print 'call lvalue'
        lvalue()
        return False
    elif(lex == 'MENOSMENOS'):
        verifyToken('MENOSMENOS')
        print 'call lvalue'
        lvalue()
        return False
    elif(lex == 'IDENT') or (lex == 'ABREPAR') or (lex == 'IDFUNC') or (lex == 'INT') or (lex == 'FLOAT') or (lex == 'STRING') or (lex == 'NIL') or (lex == 'NEW'):
        print 'call pos'
        return pos()


def pos():
    print '[pos]'
    global lex

    if(lex == 'IDENT'):
        verifyToken('IDENT')
        print 'call pos_pos'
        pos_pos()
        return True
    elif(lex == 'ABREPAR') or (lex == 'IDFUNC') or (lex == 'FLOAT') or (lex == 'INT') or (lex == 'STRING') or (lex == 'NIL') or (lex == 'NEW'): 
        print 'call valor'
        valor()
        return False

    
def pos_pos():
    print '[pos_pos]'
    global lex

    if(lex == 'ABRECOCH') or (lex == 'MENOSMENOS') or (lex == 'MAISMAIS'):
        print 'call ini_vector'
        ini_vector()
        print 'call R_pos'
        R_pos()
    elif(lex == 'SETA'):
        R_var_name()
    else:
        pass
    
def R_ini_vector():
    print '[R_ini_vector]'
    global lex

    if(lex == 'INT'):
        verifyToken('INT')
        verifyToken('FECHACOCH')

def R_pos():
    print '[R_pos]'
    global lex
    
    if (lex == 'MAISMAIS'):
        verifyToken('MAISMAIS')
    elif (lex == 'MENOSMENOS'):
        verifyToken('MENOSMENOS')

def valor():
    print '[valor]'
    global lex

    if(lex == 'ABREPAR'):
        verifyToken('ABREPAR')
        print 'call exp'        
        exp()

        verifyToken('FECHAPAR')

    elif(lex == 'NEW'):
        verifyToken('NEW')
                
        verifyToken('IDFUNC')
        
        verifyToken('ABREPAR')
        print 'call op_arguments'        
        op_arguments()

        verifyToken('FECHAPAR')

    elif(lex == 'IDFUNC'):
        verifyToken('IDFUNC')
        
        verifyToken('ABREPAR')
        print 'call op_arguments'        
        op_arguments()

        verifyToken('FECHAPAR')

    elif(lex == 'INT'):
        verifyToken('INT')

    elif(lex == 'FLOAT'):
        verifyToken('FLOAT')

    elif(lex == 'STRING'):
        verifyToken('STRING')
        
    elif(lex == 'NIL'):
        verifyToken('NIL')
    
def op_vector():
    print '[op_vector]'
    global lex

    if (lex == 'ABRECOCH'):
        verifyToken('ABRECOCH')
        verifyToken('INT')
        verifyToken('FECHACOCH')
    else:
        pass
    
def R_var_name(): # R-var-name -> TKSETA IDFUNC ( op-arguments )
    print '[R_var_name]'
    global lex

    if (lex == 'SETA'):
        verifyToken('SETA')
        verifyToken('IDFUNC')
        verifyToken('ABREPAR')
        print 'call op_arguments'
        op_arguments()
        verifyToken('FECHAPAR')
    
def ini_vector():
    print '[ini_vector]'
    global lex

    if (lex == 'ABRECOCH'):
        verifyToken('ABRECOCH')
        print 'call exp'
        exp()
        verifyToken('FECHACOCH')
        return False
    else:
        return True

###########PRINT####################

def print_param_list():
    print '[print_param_list]'
    global lex
    print 'call print_param'
    print_param()
    print 'call r_print_param_list'
    r_print_param_list()

def r_print_param_list():
    global lex


    if(lex == 'VIRG'):
        verifyToken('VIRG')
        print 'call print_param_list'
        print_param_list()
    else:
        pass

def print_param():
    print '[print_param]'
    global lex

    if(lex == "STRING"):
        verifyToken("STRING")

    elif(lex == "IDENT"):
        verifyToken("IDENT")

    elif(lex == "IDFUNC"):
        verifyToken("IDFUNC")

        verifyToken("ABREPAR")
        print 'call exp'
        exp()

        verifyToken("FECHAPAR")

init()
goal()
print '---------------------------'
print 'NENHUM ERRO ENCONTRADO \o/'