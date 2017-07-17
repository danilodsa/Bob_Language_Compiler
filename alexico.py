#!/usr/bin/python
from Lexema import *

#Abre arquivo texto. Recebe nome do arq
def arqOpen(archive):
	arq = open(archive, 'r')
	return arq

#Fecha arquivo. Recebe nome do arq
def arqClose(archive):
	archive.close()

#Analisador lexico
def lex(pos, code, line):
	ident = ''
	num = ''
	state = 1
	string = ''
	flag = True
	if (pos >= len(code)):
		pos = pos + 1
		state = 47

	while(True): #state 1
		print pos, len(code)
		#Verifica se chegou ao fim do arquivo	
		if (state == 1):
			if (code[pos] == '\n'):
				line = line+1
				pos = pos + 1
				if (pos >= len(code)):
					state = 47
			elif (code[pos] == ' ') or (code[pos] == '\t'): #Olhar os tab
				pos = pos + 1
				if (pos >= len(code)):
					state = 47			
			elif (code[pos].isalpha()):
				state = 2
				ident = ident+code[pos]
				pos = pos + 1
			elif (code[pos].isdigit()):
				state = 6
				num = num+code[pos]
				pos = pos + 1
			elif (code[pos] == '='):
				if (code[pos+1] == '='):
					state = 26
					pos = pos+2
				else:
					state = 4
					pos = pos + 1
			elif (code[pos] == '*'):
				if (code[pos+1] == '='):
					state = 28
					pos = pos + 2
				else:
					state = 5
					pos = pos + 1
			elif (code[pos] == '/'):  # /
				if (code[pos+1] == '='):
					state = 29
					pos = pos + 2
				elif(code[pos+1] == '/'): # //
					pos = pos + 2
					flag = True
					while (flag):
						if(pos >= len(code)):
							state = 47
							flag = False
						elif(code[pos] == '\n'):
							line = line + 1
							pos = pos + 1
							flag = False
							state = 1
						else:
							pos = pos + 1
				elif(code[pos+1] == '*'): # /*
					pos = pos + 2
					flag = True	
					while (flag):
						if (pos >= len(code)):
							state = 47
							flag = False
						elif ((code[pos] == '*') and (code[pos+1] == '/')): # */
							flag = False
							pos = pos + 2
							state = 1
						elif (code[pos] == '\n'):
							line = line + 1
							pos = pos + 1
						else:
							pos = pos + 1
				else:
					state = 10
					pos = pos + 1
			elif (code[pos] == '+'):
				if (code[pos+1] == '='):
					state = 24
					pos = pos+2
				elif (code[pos+1] == '+'):
					state = 25
					pos = pos+2
				else:		
					state = 11
					pos = pos + 1
			elif (code[pos] == '-'):
				if (code[pos+1] == '='):
					state = 27
					pos = pos+2
				elif (code[pos+1] == '-'):
					state = 30
					pos = pos+2	
				elif (code[pos+1] == '>'):
					state = 48
					pos = pos+2	
				else:
					state = 12
					pos = pos + 1
			elif (code[pos] == ';'):
				state = 13
				pos = pos + 1
			elif (code[pos] == '('):
				state = 14
				pos = pos + 1
			elif (code[pos] == ')'):
				state = 15
				pos = pos + 1
			elif (code[pos] == '{'):
				state = 16
				pos = pos + 1
			elif (code[pos] == '}'):
				state = 17
				pos = pos + 1								
			elif (code[pos] == '['):
				state = 18
				pos = pos + 1
			elif (code[pos] == ']'):
				state = 19
				pos = pos + 1
			elif (code[pos] == ','):
				state = 20
				pos = pos + 1
			elif (code[pos] == ':'):
				if(code[pos+1] == ':'):
					state = 22
					pos = pos + 2
				else:
					state = 21
					pos = pos + 1
			elif (code[pos] == '?'):
				state = 23
				pos = pos + 1
			elif (code[pos] == '|'):
				if (code[pos+1] == '|'):
					state = 31
					pos = pos + 2
				else:
					state = 32
					pos = pos + 1
			elif (code[pos] == '&'):
				if (code[pos+1] == '&'):
					state = 33
					pos = pos + 2
				else:
					state = 34
					pos = pos + 1
			elif (code[pos] == '^'):
				state = 35
				pos = pos + 1
			elif (code[pos] == '!'):
				if (code[pos+1] == '='):
					state = 36
					pos = pos + 2
				else:
					state = 37
					pos = pos + 1
			elif (code[pos] == '<'):
				if (code[pos+1] == '='): #<=
					state = 38
					pos = pos + 2
				elif (code[pos+1] == '<'): #<<
					state = 39
					pos = pos + 2
				else:
					state = 40
					pos = pos + 1
			elif (code[pos] == '>'):
				if (code[pos+1] == '='): #>=
					state = 41
					pos = pos + 2
				elif (code[pos+1] == '>'): #>>
					state = 42
					pos = pos + 2
				else:
					state = 43
					pos = pos + 1
			elif (code[pos] == '%'):
				state = 44
				pos = pos + 1
			elif (code[pos] == '~'):
				state = 45
				pos = pos + 1
			elif (code[pos] == '"'): #STRING
				state = 46
				pos = pos + 1


		###############################STRING#####################################
		elif (state == 46):
			if (code[pos] == '\\') and (code[pos+1] == '"'):
				string = string + code[pos+1]
				pos = pos + 1
			elif (code[pos] == '\\') and (code[pos+1] == 'n'):
				string = string + '\n'
				pos = pos + 1
			elif (code[pos] == '\n'):
				pos = pos + 1
				state = 999
			elif (code[pos] == '"'):
				pos = pos + 1
				return (pos, string, 'STRING', line)
			else:
				string = string + code[pos]
				pos = pos + 1
		#########################IDENT######################################
		elif (state == 2):
			if ((code[pos].isdigit()) or (code[pos].isalpha())) or (code[pos] == '_'):
				ident = ident+code[pos]
				pos = pos + 1
				state = 2
			else:
				state = 3
		elif (state == 3):
			if (ident == 'class'):
				return (pos, ident, 'CLASS', line)
			elif (ident == 'if'):
				return (pos, ident, 'IF', line)	
			elif (ident == 'while'):
				return (pos, ident, 'WHILE', line)
			elif (ident == 'do'):
				return (pos, ident, 'DO', line)	
			elif (ident == 'for'):
				return (pos, ident, 'FOR', line)		
			elif (ident == 'break'):
				return (pos, ident, 'BREAK', line)	
			elif (ident == 'continue'):
				return (pos, ident, 'CONTINUE', line)
			elif (ident == 'return'):
				return (pos, ident, 'RETURN', line)		
			elif (ident == 'else'):
				return (pos, ident, 'ELSE', line)
			elif (ident == 'static'):
				return (pos, ident, 'STATIC', line)		
			elif (ident == 'new'):
				return (pos, ident, 'NEW', line)
			elif (ident == 'nil'):
				return (pos, ident, 'NIL', line)
			elif (ident == 'print'):
				return (pos, ident, 'PRINT', line)				
			elif (code[pos] == '('):
				return (pos, ident, 'IDFUNC', line)
			elif (code[pos] == ' '):
				while (code[pos] == ' '):
					pos = pos+1
				if (code[pos] == '('):
					return (pos, ident, 'IDFUNC', line)
			else:
				return (pos, ident, 'IDENT', line)
		elif (state == 4):
			return (pos, '=', 'ATRIB', line)
		elif (state == 5):
			return (pos, '*', 'MULT', line)

	##############################NUMERO#############################
		elif (state == 6):
			if (code[pos].isdigit()):
				num = num+code[pos]
				pos = pos + 1
				state = 6
			elif (code[pos] == '.'):
				state = 8
				num = num + code[pos]
				pos = pos + 1
			else:
				state = 7
		elif (state == 7):
			return (pos, num, 'INT', line)
		elif (state == 70):
			return (pos, num, 'FLOAT', line)
		elif (state == 8):
			if (code[pos].isdigit()):
				state = 9
		elif (state == 9):
			if (code[pos].isdigit()):
				num = num+code[pos]
				pos = pos + 1
				state = 9
			elif (code[pos] == 'e') or (code[pos] == 'E'):
				num = num + code[pos]
				pos = pos + 1
				state = 91
			else:
				state = 70
		elif (state == 91):		
			if (code[pos] == '+') or (code[pos] == '-'):
				num = num + code[pos]
				pos = pos + 1
				state = 92
			elif (code[pos].isdigit()):
				num = num + code[pos]
				pos = pos + 1
				state = 92
		elif (state == 92):
			if (code[pos].isdigit()):
				num = num+code[pos]
				pos = pos + 1
			else:
				state = 70	
    ################################################################

		elif (state == 10):
			return (pos, '/', 'DIV', line)
		elif (state == 11):
			return (pos, '+', 'SOMA', line)
		elif (state == 12):
			return (pos, '-', 'SUB', line)
		elif (state == 13):
			return (pos, ';', 'PTOVIR', line)
		elif (state == 14):
			return (pos, '(', 'ABREPAR', line)
		elif (state == 15):
			return (pos, ')', 'FECHAPAR', line)
		elif (state == 16):
			return (pos, '{', 'ABRECHAVE', line)
		elif (state == 17):
			return (pos, '}', 'FECHACHAVE', line)
		elif (state == 18):
			return (pos, '[', 'ABRECOCH', line)
		elif (state == 19):
			return (pos, ']', 'FECHACOCH', line)
		elif (state == 20):
			return (pos, ',', 'VIRG', line)
		elif (state == 21):
			return (pos, ':', 'DOISPTO', line)
		elif (state == 22):
			return (pos, '::', 'DOISPTO2', line)	
		elif (state == 23):
			return (pos, '?', 'INTERROGACAO', line)
		elif (state == 24):
			return (pos, '+=', 'MAISIG', line)
		elif (state == 25):
			return (pos, '++', 'MAISMAIS', line)
		elif (state == 26):
			return (pos, '==', 'IGIG', line)
		elif (state == 27):
			return (pos, '-=', 'MENOSIG', line)			
		elif (state == 28):
			return (pos, '*=', 'MULTIG', line)
		elif (state == 29):
			return (pos, '/=', 'DIVIG', line)
		elif (state == 30):
			return (pos, '--', 'MENOSMENOS', line)
		elif (state == 31):
			return (pos, '||', 'PIPEPIPE', line)	
		elif (state == 32):
			return (pos, '|', 'PIPE', line)	
		elif (state == 33):
			return (pos, '&&', 'COMERCOMER', line)
		elif (state == 34):
			return (pos, '&', 'COMER', line)
		elif (state == 35):
			return (pos, '^', 'ACIR', line)
		elif (state == 36):
			return (pos, '!=', 'EXCIG', line)
		elif (state == 37):
			return (pos, '!', 'EXC', line)		
		elif (state == 38):
			return (pos, '<=', 'MENORIG', line)
		elif (state == 39):
			return (pos, '<<', 'MENORMENOR', line)
		elif (state == 40):
			return (pos, '<', 'MENORQ', line)
		elif (state == 41):
			return (pos, '>=', 'MAIORIG', line)
		elif (state == 42):
			return (pos, '>>', 'MAIORMAIOR', line)
		elif (state == 43):
			return (pos, '>', 'MAIORQ', line)				
		elif (state == 48):
			return (pos, '->', 'SETA', line)
		elif (state == 44):
			return (pos, '%', 'MOD', line)
		elif (state == 45):
			return (pos, '~', 'TIL', line)	
		elif (state == 47):
			return (pos, '', 'EOF', line)
		elif (state == 999):
			return (pos, '', 'ERRO', line)			

				


######################MAIN#########################
def getTokenList(folder):

	arq = arqOpen(folder)
	code = arq.read()

	pos = 0
	token = ''
	line = 0
	listadeTokens = []


	while (pos <= len(code)):
		(pos, lexema, token, line) = lex(pos, code, line)
		x = Lexema()
		x.set_lexema(lexema)
		x.set_token(token)
		x.set_linha(line+1)
		listadeTokens.append(x)
	for i in listadeTokens:
		i.toString()
	arqClose(arq)
	return listadeTokens
###################################################