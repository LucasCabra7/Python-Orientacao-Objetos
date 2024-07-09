from modelos.cardapio.item_cardapio import ItemCardapio
from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    #Atributos ou Objetos de uma Classe
    def __init__(self, nome, categoria,): #metodos especial
        self._nome = nome.title() #Função para deixar a primeira letra maiuscula
        self._categoria = categoria.upper() #Função para deixar todas as letras maiusculas
        self._ativo = False # o _ serve para deixar o atributo 'privado'
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod #Metodos que não estão referenciados aos objetos das instancias e sim a classe (metodo de classe).
    def lista_restaurantes(cls): #metodos próprios
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')


        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    @property #É um decorador usado para criar propriedades de acesso para atributos de uma classe. Serve que você trate um metodo como se fosse atributo, facilitando a leitura e a escrita desses valores.
    def ativo(self):
            return '✔' if self._ativo else '✘'
    
    def alternar_estado(self): #Metodo para os objetos, então não é metodo da classe (metodo da instancia)
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 'Nenhuma avaliação'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
    
    #def adicionar_bebida_no_cardapio(self, bebida):
        #self._cardapio.append(bebida)

    #def adicionar_prato_no_cardapio(self, prato):
        #self._cardapio.append(prato)

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardápio do Restaurante {self._nome}\n')

        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem_prato = (f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}')
                print(mensagem_prato)
            else:
                mensagem_bebida = (f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}')
                print(mensagem_bebida)
            
