class Lexema(object):
	__lexema = ""
	__token  = ""
	__linha  = ""

	def get_lexema(self):
		return self.lexema

	def get_token(self):
		return self.token

	def get_linha(self):
		return self.linha

	def set_lexema(self,lexema):
		self.lexema = lexema

	def set_token(self,token):
		self.token = token

	def set_linha(self,linha):
		self.linha = linha

	def toString(self):
		print str(self.get_token()) + " " + str(self.get_lexema()) + " " + str(self.get_linha())



