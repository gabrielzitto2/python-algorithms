class Transporte:

	def __init__(self, nome, peso, preco):
		self.nome = nome
		self.peso = peso
		self.preco = preco

	def getNome(self):
		return self.nome

	def getPeso(self):
		return self.peso

	def getPreco(self):
		return self.preco


class Carro(Transporte):

	def __init__(self, nome, peso, preco, preco_seguro):
		#superclasse
		Transporte.__init__(self, nome, peso, preco)
		self.preco_seguro = preco_seguro

	def getPrecoSeguro(self):
		return self.preco_seguro


carro = Carro('Fusca', 300.78, 3500.00, 800)
print(carro.getNome())
print(carro.getPeso())
print(carro.getPreco())
print(carro.getPrecoSeguro())